# BQ連携
1. GCPのサービスアカウントを作成する
2. `digdag secrets --local --set gcp.credential=@{cred}.json`
3. 実行するデータセットとクエリをdigファイルに記述する
4. `digdag run {file name}.dig`でdigファイルを実行する

# Server

メモリにステータスを格納する状態でサーバーを起動する
```
digdag server -m
```

# BQのサンプルデータ
サンプルデータはBigqueryの提供するga4_obfuscated_sample_ecommerceというGoogleのECサイトからGA経由で収集したデータ扱う。

# Refs
- [Docs](http://docs.digdag.io/index.html)
- [ワークフローエンジンDigdagのまとめ](https://qiita.com/hiroysato/items/d0fe5e2d88c267413a82)
- [GA4 schema](https://support.google.com/analytics/answer/7029846?hl=ja)