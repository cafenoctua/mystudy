# k8sでdigdagの実行
## 目的
digdagをスケールさせて高負荷にも耐えられるインフラの構築を目指します

## 使う技術
- GCP
- BigQuery
- k8s
- digdag

## digdagイメージ
k8sで稼働させるにはまずDockerイメージでdigdagを稼働させる必要があります</br>
また、digdagでGCPサービスを使うためgcloudSDKもインストールします

```dockerfile
FROM azul/zulu-openjdk:8

ENV DIGDAG_VERSION=0.10.2

# update and set timezone to Asia/Tokyo
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install locales curl && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

ENV TZ JST-9

RUN curl -o /usr/local/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-${DIGDAG_VERSION}" && \
    chmod +x /usr/local/bin/digdag && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    adduser --shell /sbin/nologin --disabled-password --gecos "" digdag

# Install gcloud
RUN apt-get -y update
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN apt-get install -y apt-transport-https ca-certificates gnupg
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get -y update && apt-get install -y google-cloud-sdk


USER digdag

WORKDIR /home/digdag

RUN alias digdag="java -jar /usr/local/bin/digdag"
```

gcloudはサービスアカウントを認証で登録させるとdigdagのbqコマンドやsdkのbqコマンドを使ってbqを実行できます

Dockerビルドして任意のリポジトリ(今回はDockerHub)にプッシュします
```
docker build . --tag={dockerHub userID}/digdag
```

```
docker push {dockerHub userID}/digdag
```
## digdagマニュフェスト
テスト用に一旦ノードを1個で可動させるマニュフェストを作ります
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: digdag
spec:
  replicas: 1
  selector:
    matchLabels:
      app: digdag
  template:
    metadata:
      labels:
        app: digdag
    spec:
      containers:
      - name: digdag
        image: brubian/digdag
        command: ["sh", "start.sh"]
        ports:
        - containerPort: 65432
        volumeMounts:
          - name: analytics-credentials
            mountPath: /secrets
            readOnly: true
      volumes:
        - name: analytics-credentials
          secret:
            secretName: analytics-credentials

---
apiVersion: v1
kind: Service
metadata:
  name: digdag-service
spec:
  selector:
    app: digdag
  ports:
    - port: 6543
      targetPort: 65432
      protocol: TCP
  type: ClusterIP
```
マニュフェストで接続先のポートとgcloudへの認証設定、最後にdigdagサーバーを実行します</br>
認証はイメージファイルに含まないためk8sのsecretsを使ってサービスアカウントのjsonを扱えるようにします

以下のコマンドでsecretsを簡単に設定できます
```
kubectl create secret generic analytics-credentials --from-file=digdag.json=gcp-service-account-key.json
```

イメージ取得後にコンテナー内にコピーしたshファイルを実行する
```sh
# Set gcp credentials

# Digdag起動前にgcloudをactivate
export GOOGLE_APPLICATION_CREDENTIALS=/secrets/digdag.json
echo $GOOGLE_APPLICATION_CREDENTIALS_JSON >> $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

# Start server
digdag server -m
```
digdagサーバー実行前にgcloudの認証にサービスアカウントを紐つけることで`digdag secrets`を使ったdigdagへの認証情報の登録を回避できます

```
kubectl apply -f digdag.yaml
```
マニュフェストが適用されポッドの稼働されます

## digdagのワークフロー実行
k8s内でdigdagサーバーは可動しているがホスト側からは接続できないためポートフォワーディングして接続するようにします
```
kubectl port-forward $(kubectl get pod -l app=digdag -o jsonpath='{.items[0].metadata.name}') 65432:65432
```
このコマンドを実行すると65432のポートにlocalhostから接続できるようになります</br>
127.0.0.1:65432に接続するとdigdagのUIが表示されるので新規でプロジェクトを作成します

次にpodの中に入りdigdagのワークフローを作成し実行させます
```
kubectl exec -it $(kubectl get pod -l app=digdag -o jsonpath='{.items[0].metadata.name}') /bin/bash
```
ポッドに入るのでdigdagのワークフローを作成します
```
digdag init {workflow name}
cd {workflow name}
digdag push {project name}
```
## digdag ingress対応
ポッドに直接つなげてしまうとk8sのうま味がなくなるためIngressを使ってUIへのアクセス経路を作ります
これで中で複数のUIが立ち上がっても接続先を統一することができます

ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: digdag-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/service-upstream: "true"
    nginx.ingress.kubernetes.io/affinity: 'cookie'
spec:
  rules:
    - http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: digdag-service
              port:
                number: 65432
```
ドメイン名を取得してないため今回はminikubeのIPアドレスから接続するようにしました
そのためhttp接続での設定となっており他の接続先もないため`http://{IP address}`直打ちで接続できます

## digdagサーバーへのpush
ローカルで構築したdigdagをクライアント、minikubeのdigdag serverを実行をするサーバーと見立てた構成を上記までの取り組みで作りました
次にサーバーへクライアントで作ったワークフローをpushできるようにすれば疑似的ですが稼働ができます

そのためにはクライアントのpush先をサーバーに変更します

digdagをインストールすると特にインストールコマンドを変更しない限りインストールしたユーザーのホームディレクトリにdigdagのconfigファイルが生成されます

コンフィグファイルのディレクトリになります`~/.config/digdag/config`
このコンフィグファイルに以下の内容を書き加えるもしくは書き換えるとpush先を変更できます
```
client.http.endpoint = http://{任意のIPアドレスもしくはドメイン名}
```
サーバーが証明書を取得している場合は`https`に書き換えてください


# Ref
- [digdag github](https://github.com/treasure-data/digdag)
- [スケーラブルなワークフロー実行環境を目指して](https://speakerdeck.com/trsnium/embulk-and-digdag-meetup-2020)
- [D2-2-S09: BigQuery を使い倒せ！ DeNA データエンジニアの取り組み事例](https://www.youtube.com/watch?v=k1CpRz0C6B8)
- [digdag中心の生活](https://speakerdeck.com/rikiyaoguchi/digdagzhong-xin-falsesheng-huo?slide=65)
- [Digdag + Embulkをクラウド転生させてデータ基盤運用を圧倒的に楽にした話](https://www.m3tech.blog/entry/2020/12/19/110000)
- [GKEにおけるDigdagでのGCPのクレデンシャルの取り扱い bqオペレータとgcloudコマンドのクレデンシャルのズレ](https://komi.dev/post/2021-03-21-gcp-credential-in-digdag/)
- [EKS(Kubernetes)上にDigdag・Embulk・Redashで分析環境を構築する](https://wapa5pow.com/posts/2019-04-19--build-analytics-environment-on-eks)
- [digdagのコンフィグについて（~/.config/digdag/config）](https://qiita.com/toru-takahashi/items/a7253dec31cb5f36c196)
- [Digdagによる大規模データ処理の自動化とエラー処理](https://www.slideshare.net/frsyuki/digdag-76749443)