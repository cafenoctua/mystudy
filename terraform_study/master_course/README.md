terraformではterraform coreとproviderで構成されます。
terraform coreではterraformで大別されるリソースの指定を行い以降でprovider特有の設定を記述することで構築する指示書を作成します。

```tf
resource "{resource type}" "{local_name}" {
    credentials = ~~~
    project = ~~~

    settings = {
        a = aaa
        b = bbb
    }
}
```
resourceがterraform coreに辺り以降がprovider特有のリソース名や設定を記述します。



providerが使用先のクラウドを指定できます。
providerを指定できたら必ず対象のディレクトリで初期化して使用するproviderの内容をダウンロードする必要があります。

```tf
provider "aws" {
    region = "us-east-2"
}
```

```
terraform init
```

更新する際は`--update=true`をオプションでつけます。

.tfstateで構築するリソースの詳細が記述されます。
このファイルで差分管理がされ追加、変更、削除されるリソースを事前に知ることができます。

```
terraform plan
```

これで.tfstateを元にリソースの状態が表示されます。
また、`--state=".tfstate file name"`のオプションをつけることで任意の.tfstateに対して実行することができます。

```
terraform apply
```

providerに.tfstateを反映させますが事前に`plan`が実行されるためこの時点で再度確認することもできます。

terraform resources

resoucesのメタ引数
- provider
- count
- depends_on
- for_each
- lifecycle
- provisioner and connection

terraform workspaceを使うと同一ディレクトリで扱うワークスペースを切り替えることができます。

構築済みのインフラをterraformに落とし込む際は
- クラウドサービスに接続できるように認証を通す
- 対象のサービスに該当するterraform resourceをドキュメントから参照する
- 選択したオプションをリソース内に書き込む

terraformのコードをフォーマッティングしたい場合
- `terraform fmt`
- [TFlint](https://github.com/terraform-linters/tflint)

のどちらかを使うと良いです
また、vscodeでも拡張機能を提供しているためそれを使うのも良いです。

`terraform console`を使うことで現在の適用しているリソースをインタラクティブに確認できます。