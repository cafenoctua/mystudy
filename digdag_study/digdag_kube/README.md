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

## PostgreSQLと連携してデータを永続化させる
digdagはサーバーモードでプロジェクト、ワークフローの管理ができます。
その際サーバーは主に2つのモードで稼働されます。
- オンメモリ
- PostgreSQL

オンメモリで稼働する場合データはメモリ上で管理されるためサーバーが停止すると同時データが削除されます。

オンメモリサーバーは以下のコマンドで実行されます
```
digdag server -m
```

オンメモリはローカルでテストする分には手軽で良いですが冗長性をもたせた構成を作りたい場合だとそれぞれのノードのメモリでデータ管理されてしまい実現ができないため別のノードでDBを持たせてそこでデータ管理をさせるとデータの永続化と共有が可能となり冗長構成を実現できます。

digdagとPostgresSQLを連携させるにはdigdagのサーバーを設定するファイルとPostgreSQLにdigdag用のDBを作成する必要があります。

まず、設定ファイルから説明します。
```server.properties
server.bind = 0.0.0.0                                   # digdagサーバーの接続先のIPアドレス設定
database.type = postgresql                              # 扱うDBのタイプ
database.user = digdag                                  # DBで用意したユーザー
database.password = digdagpass                          # ユーザーのパスワード
database.database = digdag_db                           # ユーザーが接続できるDB
database.host = 192.168.49.2                            # PostgreSQLの接続先IPアドレス
database.port = 30510                                   # PostgreSQLの接続先ポート
database.maximumPoolSize = 4                            # 使用できるスレッド数
digdag.secret-encryption-key = MDEyMzQ1Njc4OTAxMjM0NQ== # digdagの暗号化をするときに使うキー
```

PostgreSQLには以下のコマンドを使いユーザー、DBの設定をします。
```
CREATE ROLE digdag WITH PASSWORD 'digdagpass' NOSUPERUSER NOCREATEDB NOCREATEROLE LOGIN;
CREATE DATABASE digdag_db WITH OWNER digdag;
CREATE EXTENSION "uuid-ossp";
```
これらの作業が済んだら最後に以下コマンドでdigdagサーバーを起動します
```
digdag server -c server-properties
```

minikubeを扱う場合はPostgreSQLをNodePortで実行するとdigdagがminikubeのIPアドレス経由で接続できるためローカルで容易に接続ができるようになります。

# DigdagをHA構成にする場合
サーバーとして稼働させる場合に以下4つの形式で稼働させることができます。
- UI
- エージェント
- ワークフロー
- スケジューラー

起動自体は`digdag server`で起動しますがその際のオプションを変更することによってそれぞれ独立した役割を持ったものに変更できます。

- UI
  - --disable-executor-loop --disable-local-agent --disable-scheduler
- エージェント
  - --disable-executor-loop --disable-scheduler
- ワークフロー
  - --disable-local-agent --disable-scheduler
- スケジューラー
  - --disable-local-agent

UIは、ローカル(サーバー内)実行とループ処理、スケジュール処理を不可にすることでワークフローとプロジェクトのGUI管理のみを行います。
このようにそれぞれのサーバーの機能を独立させることでそれぞれより細かく設定やリソースの配分を決めることができます。

# ロギング
digdagはserver.propertiesを設定することでローカル、AWS, GCPにロギングができるようになります。
以下GCPのロギング設定になります。
```
log-server.type = gcs
log-server.gcs.bucket = digdag-log
log-server.gcs.credentials.json.path = /secrets/digdag.json
```

全サーバーに設定することでログの永続化ができます。

サーバーの細かい設定については以下のリンクを参照してください。
- [Server-mode commands](https://docs.digdag.io/command_reference.html#server-mode-commands)

# CloudSQLとの連携
ローカルと接続する場合はCloudSQL側認可するIPを登録する必要があります。
CloudSQLを立ち上げてから生成されるIPとデフォルトポート(5432)をserver.propertiesに書き込みます。
CloudSQL側でdigdag_dbを作ればdigadagからデータを書き込めるようになります。
```
CREATE DATEBASE digdag_db;
```

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
- [running digdag server with postgres database ](https://github.com/treasure-data/digdag/issues/1363)
- [DigdagをHA構成にしてみた](https://techblog.zozo.com/entry/digdag_ha)
- [Server-mode commands](https://docs.digdag.io/command_reference.html#server-mode-commands)
- [google_sql_database_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#granular-restriction-of-network-access)