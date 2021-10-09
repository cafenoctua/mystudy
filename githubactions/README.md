# workflowの再利用
workflowのコピーアンドペーストを省略し再利用元の状態を保てるため再利用が推奨される。

workflowに再利用するためのアクセス
- 同一のリポジトリにいること
- 再利用元のworkflowはパブリックリポジトリであること

制限について
- 再利用されるworkflowは他の再利用されるworkflowからは呼び出せない
- プライベートリポジトリを採用する場合は同一リポジトリでしか再利用ができない
- 呼び出し先の`env`の環境変数は呼び出し元に引き継がれない

再利用可能なworkflowは`.github/workflows`以下でyamlファイルで定義される

以下がサンプルのyamlファイル
```yaml
name: Reusable workflow example

on:
  workflow_call:
    inputs:
      username:
        required: true
        type: string
    secrets:
      token:
        required: true

jobs:
  example_job:
    name: Pass input and secrets to my-action
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/my-action@v1
        with:
          username: ${{ inputs.username }}
          token: ${{ secrets.token }}
```

再利用する場合は`uses`を使って再利用したいworkflowのパスを記述する

```yaml
name: Call a reusable workflow

on:
  pull_request:
    branches:
      - main

jobs:

  call-workflow-passing-data:
    uses: octo-org/example-repo/.github/workflows/workflow-B.yml@issue31
    with:
      username: mona
    secrets:
      token: ${{ secrets.TOKEN }}
```

# Refs
- [GitHub Actions について学ぶ](https://docs.github.com/ja/actions/learn-github-actions)