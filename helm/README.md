# コンセプト
3つの大きなコンポーネントがある

1. Chart
   - これには、Kubernetesクラスター内でアプリケーション、ツール、またはサービスを実行するために必要なすべてのリソース定義が含まれています。
2. Repository
   - チャートを収集して共有できる場所です。
3. Release
   -  Kubernetesクラスターで実行されているチャートのインスタンス。
   -  同じクラスターに同一のチャートをインストールできその場合同一のチャートで構築されたリソースがインストールした数だけ作成されます。

HelmはチャートをKubernetesにインストールし、インストールごとに新しいリリースを作成します。また、新しいチャートを見つけるには、Helmチャートリポジトリを検索できます。

# チャートの探し方
helmには2種類の強力なサーチ機能が備わっています。
- `helm serch hub`
  - [Artifact Hub](https://artifacthub.io/)を検索します。Artifact Hubには、数十の異なるリポジトリからのヘルムチャートが一覧表示されます。
- `helm serch repo`
  - ローカルのhelmクライアントに追加したリポジトリを検索します（helm repo addを使用）。
  - この検索はローカルデータを介して行われ、パブリックネットワーク接続は必要ありません。

Artifact hubでwordpressのChartを検索する場合はこのようにすればそれに関する検索結果が表示されます。

`helm search hub wordpress`

ちなみに`helm search hub`を実行すると全てのChartが検索されます。

ChartをRepogitoryに追加するには`helm repo add {resource name} {Chart URL}`で追加できます。</br>
追加した特定のChartの検索は`helm search repo {resource name}`で検索できます。

# パッケージのインストール
新しいパッケージをインストールするには`helm install {resource name} {package name}`を使います。</br>
これでワードプレスチャートがインストールされました。チャートをインストールすると、新しいリリースオブジェクトが作成されることに注意してください。
このリリースはhappy-pandaという名前です。

helmは以下のリソースの順にインストールされます。
- Namespace
- NetworkPolicy
- ResourceQuota
- LimitRange
- PodSecurityPolicy
- PodDisruptionBudget
- ServiceAccount
- Secret
- SecretList
- ConfigMap
- StorageClass
- PersistentVolume
- PersistentVolumeClaim
- CustomResourceDefinition
- ClusterRole
- ClusterRoleList
- ClusterRoleBinding
- ClusterRoleBindingList
- Role
- RoleList
- RoleBinding
- RoleBindingList
- Service
- DaemonSet
- Pod
- ReplicationController
- ReplicaSet
- Deployment
- HorizontalPodAutoscaler
- StatefulSet
- Job
- CronJob
- Ingress
- APIService

Dockerfileが600MBを超えるものについてはインストールに時間がかかるため`helm status {relese name}`でステータスを確認して終了したか確認する必要があります。

## インストール前にチャートをカスタマイズする
チャートの設定値を確認するには`helm show values bitnami/wordpress`を使います。</br>
設定値を確認できたら.yamlファイルを用いて書き換えたい設定値を記述します。
```yaml
{mariadb.auth.database: user0db, mariadb.auth.username: user0}
```
このyamlファイルを参照するように`helm install -f {yaml faile path} {repo name} --generate-name`でインストールすると設定値が反映されたリリースが生成されます。

上記以外にも設定値を書き換える方法があります
- `--values`を使ってコマンドライン
- `--set`コマンドラインでオーバーライドを指定します。


両方を使用する場合、-set値は優先度の高い--valuesにマージされます。--setで指定されたオーバーライドは、ConfigMapに保持されます。 --setされた値は、helm get values <release-name>を使用して特定のリリースで表示できます。--setされた値は、-reset-valuesを指定してhelm upgradeを実行することでクリアできます。

## --setの形式と制限
--setオプションは、0個以上の名前/値のペアを取ります。最も単純な場合、次のように使用されます。--set name = value。これに相当するYAMLは次のとおりです。
```
name: value
```

`--set a=b,c=d`の多入力は以下と同等になります。
```
a: b
c: d
```

ネスト, リストを使ってより複雑な入力値を作ることもできます。

## その他のインストールメソッド

- ローカルチャート (helm install foo foo-0.1.1.tgz)
- ディレクトリにまとまっているチャートを直接 (helm install foo path/to/foo)
- full URL (helm install foo https://example.com/charts/foo-1.2.3.tgz)

# リリースのアップグレード、および障害時の回復
リリースの更新もしくは設定値を変更した場合は`helm upgrade`で更新できます。更新については差分のみ変更する更新方法を取ります。

設定済みの設定値を確認したい場合は`helm get value {release name}`で確認できます。

次に変更をロールバックしたい場合は、`helm rollback {release name} {revision}`で任意の状態にロールバック可能です。

revisionはupgradeするたび1から加算されていきます。

いまreleaseが抱えるrevisionを確認するには`helm history {release name}`を使います。

# 有用なオプション
以下に代表的なオプションを記します。
- `helm {command} --help`
- --timeout
  - Kubernetesコマンドが完了するのを待つGoduration値。これはデフォルトで5m0sです
- --wait
  - すべてのポッドが準備完了状態になり、PVCがバインドされ、デプロイメントに最小（DesiredからmaxUnavailableを差し引いたもの）のポッドが準備完了状態になり、サービスにIPアドレス（およびLoadBalancerの場合はIngress）があり、リリースを成功としてマークするまで待機します。--timeout値まで待機します。タイムアウトに達すると、リリースはFAILEDとしてマークされます。注：ローリング更新戦略の一環として、Deploymentのレプリカが1に設定され、maxUnavailableが0に設定されていないシナリオでは、-waitは、準備完了状態の最小ポッドを満たしたときに準備完了として戻ります。
- --no-hooks
  - これにより、コマンドの実行中のフックがスキップされます
- --recreate-pods
  - （アップグレードとロールバックでのみ使用可能）：このフラグにより​​、すべてのポッドが再作成されます（デプロイメントに属するポッドを除く）。 （Helm 3では非推奨）

# helm uninstall
releaseを削除するには`helm uninstall {release name}`を使います。

release一覧の取得には`helm list`(削除済みのreleaseも含める場合はオプションに`--all`を使います。)

# helm repositories
`helm repo`の後に様々なコマンドを追記することで操作ができます。
- list
  - リポジトリの一覧を取得します
- add
  - 新しいリポジトリを追加します
- update
  - 追加済みのリポジトリの更新を行います
- remove
  - 追加済みのリポジトリの削除を行います

# Chartの作成
サンプルとして以下のコマンドでチャートのテンプレートを作成しましょう。
```
helm create deis-worklflow
```
このコマンドを実行すると直下のディレクトリに`./deis-workflow/`が生成されます。
このテンプレートを編集することでチャートを作成することができます。

コードの整形をするときに`helm lint`を用いると良いです。

作成が終わったら`helm package {chart name}`で.tgzファイルが生成されます。

このチャートをインストールするには`helm install {release name} {chart .tgz file name}`を使います。
インストールすると他のリポジトリ同様にチャートリポジトリに格納されます。

詳細は[Chart作成ガイド](https://helm.sh/docs/topics/charts/)を参照してください。

# Chart開発のトピックとトリック
## テンプレート関数
Helmでは[Goテンプレート](https://pkg.go.dev/text/template)を用いてファイルをテンプレート化します。Goテンプレートを使うことでGoに付属している組み込み関数やその他の関数を使えます。

include関数を使用すると、別のテンプレートを取り込んで、その結果を他のテンプレート関数に渡すことができます。

required関数を使用すると、テンプレートのレンダリングに必要な特定の値のエントリを宣言できます。値が空の場合、テンプレートのレンダリングは失敗し、ユーザーが送信したエラーメッセージが表示されます。

# Charts
Helmは、チャートと呼ばれるパッケージ形式を使用しています。チャートは、関連するKubernetesリソースのセットを説明するファイルのコレクションです。単一のチャートを使用して、memcachedポッドのような単純なものや、HTTPサーバー、データベース、キャッシュなどを備えた完全なWebアプリスタックのような複雑なものをデプロイできます。

チャートは、特定のディレクトリツリーに配置されたファイルとして作成されます。それらは、バージョン管理されたアーカイブにパッケージ化して展開できます。

公開されたチャートのファイルをインストールせずにダウンロードして確認したい場合は、`helm pull chartrepo / chartname`を使用して行うことができます。

## Chartのファイル構造
チャートは、ディレクトリ内のファイルのコレクションとして編成されています。ディレクトリ名はチャートの名前です（バージョン情報なし）。したがって、WordPressを説明するチャートはwordpress /ディレクトリに保存されます。


このディレクトリ内で、Helmはこれに一致する構造を期待します。
```
wordpress/
  Chart.yaml          # A YAML file containing information about the chart
  LICENSE             # OPTIONAL: A plain text file containing the license for the chart
  README.md           # OPTIONAL: A human-readable README file
  values.yaml         # The default configuration values for this chart
  values.schema.json  # OPTIONAL: A JSON Schema for imposing a structure on the values.yaml file
  charts/             # A directory containing any charts upon which this chart depends.
  crds/               # Custom Resource Definitions
  templates/          # A directory of templates that, when combined with values,
                      # will generate valid Kubernetes manifest files.
  templates/NOTES.txt # OPTIONAL: A plain text file containing short usage notes
```

Helmは、charts /、crds /、templates /ディレクトリ、およびリストされたファイル名の使用を予約しています。その他のファイルはそのまま残します。

## Chart.yamlについて
チャートにはChart.yamlファイルが必要です。次のフィールドが含まれています。
```yaml
apiVersion: The chart API version (required)
name: The name of the chart (required)
version: A SemVer 2 version (required)
kubeVersion: A SemVer range of compatible Kubernetes versions (optional)
description: A single-sentence description of this project (optional)
type: The type of the chart (optional)
keywords:
  - A list of keywords about this project (optional)
home: The URL of this projects home page (optional)
sources:
  - A list of URLs to source code for this project (optional)
dependencies: # A list of the chart requirements (optional)
  - name: The name of the chart (nginx)
    version: The version of the chart ("1.2.3")
    repository: (optional) The repository URL ("https://example.com/charts") or alias ("@repo-name")
    condition: (optional) A yaml path that resolves to a boolean, used for enabling/disabling charts (e.g. subchart1.enabled )
    tags: # (optional)
      - Tags can be used to group charts for enabling/disabling together
    import-values: # (optional)
      - ImportValues holds the mapping of source values to parent key to be imported. Each item can be a string or pair of child/parent sublist items.
    alias: (optional) Alias to be used for the chart. Useful when you have to add the same chart multiple times
maintainers: # (optional)
  - name: The maintainers name (required for each maintainer)
    email: The maintainers email (optional for each maintainer)
    url: A URL for the maintainer (optional for each maintainer)
icon: A URL to an SVG or PNG image to be used as an icon (optional).
appVersion: The version of the app that this contains (optional). Needn't be SemVer. Quotes recommended.
deprecated: Whether this chart is deprecated (optional, boolean)
annotations:
  example: A list of annotations keyed by name (optional).
```
### Chartのバージョニング
全てのチャートはバージョンを持つ必要があります。
Chart.yaml内のバージョンフィールドは、CLIを含む多くのHelmツールで使用されます。パッケージを生成する際、helm packageコマンドは、Chart.yaml内で見つけたバージョンをパッケージ名のトークンとして使用します。システムは、chartパッケージ名の中のバージョン番号がChart.yamlの中のバージョン番号と一致することを前提としています。この前提を満たさないとエラーになります。

### apiVersionフィールド
Helm3ではapiVersionはv2を指定する必要があります。(以前のチャートをインストールした場合v1が使われていることがありますがHelm3では引き続き使えます。)

v1とv2の違い
- v1チャート用の別のrequirements.yamlファイルにあるチャートの依存関係を定義する依存関係フィールド（チャートの依存関係を参照）。
- タイプフィールド、アプリケーションチャートとライブラリチャートを区別します（チャートタイプを参照）。

### appVersionフィールド
作成しているアプリケーション自体のバージョンを指します。なのでこのフィールドは任意で管理されるメタ情報です。

### kubeVersionフィールド
サポートしているk8sのバージョンの情報を残せます。

## チャートの依存関係
Helmでは、1つのチャートが他のチャートの数に依存する場合があります。これらの依存関係は、Chart.yamlの依存関係フィールドを使用して動的にリンクするか、charts /ディレクトリに取り込み、手動で管理できます。

### dependenciesフィールドによる依存関係管理
現在のチャートに必要なチャートは、依存関係フィールドのリストとして定義されています。
```yaml
dependencies:
  - name: apache
    version: 1.2.3
    repository: https://example.com/charts
  - name: mysql
    version: 3.2.1
    repository: https://another.example.com/charts
```
- name欄には、ご希望のチャートの名前を入力してください。
- バージョンフィールドは、ご希望のチャートのバージョンです。
- repositoryフィールドには、チャートのリポジトリへの完全なURLを入力します。このリポジトリをローカルに追加するには、helm repo addを使用する必要があることに注意してください。
- URLの代わりにレポの名前を使うこともできます。

`helm dependency update`は定義された依存関係をcharts/ディレクトリにダウンロードします。

### Aliasフィールドの依存関係
上記の他のフィールドに加えて、各要件エントリにはオプションのフィールドエイリアスが含まれる場合があります。

依存関係チャートのエイリアスを追加すると、新しい依存関係の名前としてエイリアスを使用して、依存関係にチャートが配置されます。

他の名前のチャートにアクセスする必要がある場合は、エイリアスを使用できます。

```yaml
# parentchart/Chart.yaml

dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-1
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-2
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
```

### 依存関係のタグと条件フィールド
- tag
  - 各チャートにタグをつけることでグルーピングした制御ができます
- Condition
  - 1つ以上のYAMLパスで構成されこのパス関係に応じた制御ができます

制御関係としてはtagが先に処理されてからConditionが処理されるため以下の設定の場合はsubchart1でfront-endのものは結果的に有効化されます。
```yaml
subchart1:
  enabled: true
tags:
  front-end: false
  back-end: true
```
また、デフォルトは全て`true`が設定されています。

ちなみに--setを使ってCLIで制御も可能性です。

#### TagとConditionの解決
- Condition
  - 常にタグを上書きします。存在する最初の条件パスが優先され、そのチャートの後続の条件パスは無視されます。
- Tag
  - チャートのタグのいずれかがtrueの場合、「チャートを有効にする」と評価されます。

どちらの設定もyamlのトップレベルでのみ扱われます。

#### 子チャートから親チャートへのエクスポート
子チャートの値を反映させたい場合exportsを用いることで親チャートに値を反映できます。

parents.yaml
```yaml
dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    import-values:
      - data
```


child.yaml
```yaml
exports:
  data:
    myint: 99
```

上記の例だと親チャートに子チャートへ依存関係をもたせてdataという値を取得するようにしています。

親キーデータは、親の最終値に含まれていないことに注意してください。親キーを指定する必要がある場合は、「子-親」フォーマットを使用してください。

#### 子-親フォーマット
子チャートの値のエクスポートキーに含まれていない値にアクセスするには、インポートする値のソースキー（子）と親チャートの値の宛先パス（親）を指定する必要があります。

以下の例のimport-valuesは、child：pathで見つかった値を取得し、それらをparent：で指定されたパスの親の値にコピーするようにHelmに指示します。

Chart.yaml
```yaml
dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    ...
    import-values:
      - child: default.data
        parent: myimports
```
上記の例では、subchart1の値のdefault.dataにある値は、以下に詳述するように、親チャートの値のmyimportsキーにインポートされます。


parent.yaml
```yaml
myimports:
  myint: 0
  mybool: false
  mystring: "helm rocks!"
```

child.yaml
```yaml
default:
  data:
    myint: 999
    mybool: true
```

親チャートの値は以下のように書き換わります。
```yaml
myimports:
  myint: 999
  mybool: true
  mystring: "helm rocks!"
```

## テンプレートファイル
Go templatesで.yamlファイルが作成されます。

example.yaml
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: deis-database
  namespace: deis
  labels:
    app.kubernetes.io/managed-by: deis
spec:
  replicas: 1
  selector:
    app.kubernetes.io/name: deis-database
  template:
    metadata:
      labels:
        app.kubernetes.io/name: deis-database
    spec:
      serviceAccount: deis-database
      containers:
        - name: deis-database
          image: {{ .Values.imageRegistry }}/postgres:{{ .Values.dockerTag }}
          imagePullPolicy: {{ .Values.pullPolicy }}
          ports:
            - containerPort: 5432
          env:
            - name: DATABASE_STORAGE
              value: {{ default "minio" .Values.storage }}
```
{{}}で囲われている箇所がテンプレートの機能が使われています。

`.Values`となっているのはvalues.yamlで定義された変数を読み出しています。defaultと記述すると初期値を設定できます。

独自で定義する以外にも定義済みの変数があるためそれらを使うことができます。

## values.yaml
values.yamlは以下のように記述します。
```yaml
imageRegistry: "quay.io/deis"
dockerTag: "latest"
pullPolicy: "Always"
storage: "s3"
```

事前に定義した値を書き換える場合は別の.yamlファイルを作成して`helm install --values {my value}.yaml {release name}`でインストールすると任意の値のみ書き換えることができます。
書き換えなので存在しないキーを入れ込めません。

## スキーマファイル
values.schema.jsonでvalues.yamlの各値の型を定義することができます。

values.schema.json
```json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "properties": {
    "image": {
      "description": "Container Image",
      "properties": {
        "repo": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "name": {
      "description": "Service name",
      "type": "string"
    },
    "port": {
      "description": "Port",
      "minimum": 0,
      "type": "integer"
    },
    "protocol": {
      "type": "string"
    }
  },
  "required": [
    "protocol",
    "port"
  ],
  "title": "Values",
  "type": "object"
}
```
このファイルを作ることで以下のタイミングで値のバリデーションが発生します。
- helm install
- helm upgrade
- helm lint
- helm template

## Custom Resource Definitions(CRDs)
Helmはk8sで使えるCRDsの開発が可能です。

Helm3で構築されるCRDsにはいくつかの制限があります。
- crds/ディレクトリに配置される必要があります。
- 複数のCRD（YAML開始マーカーと終了マーカーで区切られている）を同じファイルに配置できます。
- Helmは、CRDディレクトリ内のすべてのファイルをKubernetesにロードしようとします。
- CRDファイルはテンプレート化できません。プレーンなYAMLドキュメントである必要があります。

CRDsは、Helmが新しいチャートをインストールすると、CRDがアップロードされ、APIサーバーでCRDが利用可能になるまで一時停止してから、テンプレートエンジンを起動し、グラフの残りの部分をレンダリングして、Kubernetesにアップロードします。この順序により、CRD情報はHelmテンプレートの.Capabilitiesオブジェクトで使用でき、HelmテンプレートはCRDで宣言されたオブジェクトの新しいインスタンスを作成する場合があります。

たとえば、チャートのcrds /ディレクトリにCronTabのCRDがある場合、templates /ディレクトリにCronTabの種類のインスタンスを作成できます。

```
crontabs/
  Chart.yaml
  crds/
    crontab.yaml
  templates/
    mycrontab.yaml
```

crontab.yaml
```yaml
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
```

次に、テンプレートmycrontab.yamlが新しいCronTabを作成する場合があります（通常どおりテンプレートを使用）。
```yaml
apiVersion: stable.example.com
kind: CronTab
metadata:
  name: {{ .Values.name }}
spec:
   # ...
```

### CRDsの制限
Kubernetesのほとんどのオブジェクトとは異なり、CRDはグローバルにインストールされます。そのため、HelmはCRDの管理に非常に慎重なアプローチを取っています。 CRDには、次の制限があります。
- CRDは決して再インストールされません。crds/ディレクトリにあるCRDが既に存在するとHelmが判断した場合（バージョンに関わらず）、Helmはインストールやアップグレードを試みません。
- アップグレードやロールバックでは、CRDは決してインストールされません。Helmはインストール操作でのみCRDを作成します。
- CRDは決して削除されません。CRDを削除すると、クラスタ内のすべてのネームスペースでCRDのすべてのコンテンツが自動的に削除されます。そのため、HelmはCRDを削除しません。

そのため、削除したいものは手動で行う必要があります。

