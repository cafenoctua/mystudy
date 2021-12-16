# 基礎
シェルとは、カーネルがわかるようにコマンドを実行する環境で現在のスタンダードはbash


cshは欠陥品と呼ばれるレベルでバグを抱えているため絶対に採用してはならない</br>
`#!`はシバンと呼ばれる文字列でスクリプトの実行で使うインタプリタを指定する</br>
シェルスクリプトは思想的にコマンドを羅列しているという理解で進めるとエラーへの対処などがスムーズになる</br>
先達が意識しているポイント
1. シェルスクリプトはすべてコマンドの羅列である
2. シンタックスエラーではなくコマンドエラーとして考える
3. シェルスクリプトはコマンドライン・テンプレートである
4. 最終的にどのようなコマンドが実行されるかイメージする


if statement
```sh
#!/bin/bash

# 標準入力を受け取る
read str

if [ "$str" = "hoge" ]; then
    echo "hoge"
elif [ "$str" = "fuga" ]; then
    echo "fuga"
else
    echo "unknown"
fi
```
if文は上記のように記述されるif文の条件式である`[`もコマンドとして扱われるため必ずスペースが必要となる

case statement
```sh
#!/bin/bash

read str

case "$str" in
    "hoge" ) echo "hoge"
            echo "hoge" ;;
    "fuga" ) echo "" ;;
    * ) echo "unknown" ;;
esac
```
`*`は全文字列と一致するというワイルドカード
`;;`が各コマンド処理の区切り

for statement
```sh
#!/bin/bash

for i in 0 1 2 3
do
    echo $i
done
```

while statement
```sh
#!/bin/bash

while :
do
    read str

    if [ "$str" = "end" ]; then
        break
    fi
done
```


標準出力とエラー
`1`は標準出力で`2`がエラーを意味する

終了ステータスは`$?`で受け取れる

四則演算
```sh
#!/bin/bash

VAR_L=5
VAR_R=5

# 四則演算
echo $(( $VAR_L + $VAR_R ))
echo $(( $VAR_L - $VAR_R ))
echo $(( $VAR_L * $VAR_R ))
echo $(( $VAR_L / $VAR_R ))

```

変数
通常のプログラミング言語同様の命名ルールがある
スコープは基本的にグローバル変数

$を使ったアクセス
- $0　スクリプト名
- $#　渡されたパラメータの個数
- $$　プロセスID
- $1,$2,..$N　パラメータ
- $* クリプト実行時、指定されたパラメータ全てが設定される変数。
- $@　基本的に$*と同じ、“”で囲んだときの展開の動作が異なる

List型
```sh
#!/bin/bash

LIST_1=(aa bb cc)

echo ${LIST_1[0]}
echo ${LIST_1[1]}
echo ${LIST_1[2]}
```

sedを使ってテキストファイルの編集を行える

置換
```sh
sed -e 's/code/script/g' ./test.txt
```

対象行削除
```sh
sed -e 's/code/d' ./test.txt
```

関数
```sh
#!/bin/bash

function hello_world () {
    echo "$1" # arguments are accessible through $1, $2,...
}

hello_world aaa
```
シェルスクリプトの思想上なるべくシンプルなものが求められるため関数ものその思想に則る必要がある
シェルスクリプトの関数の特性
- 戻り値は基本的に存在しない
- 関数内の変数もグローバル変数として扱われる
  - 変数定義時に`local var=1`のように宣言すればスコープをローカルに絞れる
アンチパターンとして関数を複雑にするというのがあるが上記思想に則って考えればわかる

## 学習に使っているもの
- [【1分でわかる】シェルスクリプトとは？](https://eng-entrance.com/linux-shellscript-what)
- [３分間で人に説明できるようになるUnixとLinuxの違い](https://eng-entrance.com/unix_linux)
- [bash シェルスクリプト入門 -シェルスクリプトのいろは-](https://shellscript.sunone.me/tutorial.html)
- [【初心者でもわかる】Linuxシェルスクリプト入門 まとめました](https://eng-entrance.com/category/linux/linux-shellscript)

# 初級
## 標準入出力とエラー
- 0 標準入力
- 1 標準出力
- 2 エラー

シェルスクリプトでは上記の番号で予約されている。
また、標準出力とエラーを同時に出力したい場合は`command > log.txt 2>&1`と記述するとできる。

## リダイレクト
標準出力やエラーを任意の状態で出力したいときに使われる。
ファイル名を指定するとファイルが生成され出力された内容を保存する

出力の種類
- `>` 生成して出力する
- `>>` 末尾に出力する

## パイプライン
2つ以上のコマンドをつないで処理するときに使う。
`|`でコマンドを繋ぐことで直前のコマンドの標準出力を標準入力として受け取ってコマンドが実行される。

## フィルタ
標準出力を特定の条件でフィルタリングするコマンド

- cat そのまま出力
- head 先頭n行を出力
- tail 末尾n行を出力
- grep 指定した検索パターンに一致する行を出力
- sort 順番を並べ替える
- uniq 重複した行を取り除く
- tac 逆順で出力
- wc 行数やバイトを出力

使用例

duでファイルサイズを取得してそこからサイズの大きいものを5行分出力する
```
du -b ./* | sort -n | tac | head -n 5
```

## cut
入力行の区切り文字と列を指定して出力する

`cut -d : -f 7 /etc/passwd`

また、`-f 1,2,3`のように複数列を指定できる

## ファイル監視
ファイル監視で追加分の監視が行われることがある。
`tail -f text.txt`
上記コマンドを実行すると実行状態となりファイルの追加分をどんどん標準出力していく

## サーチパスに独自のシェルスクリプトを配置する
`/dir/bin`任意のディレクトリを選択するそこにシェルスクリプトを配置する
以下のようなディレクトリ構造を作る
```
/dir+
    |
    + bin +
          |
          + shellscript.sh
```
これをサーチパスに設定することで`shellscript.sh`でコマンド実行のように独自のシェルスクリプトを実行できる

サーチパスへの登録方法
```
PATH="$PATH:/dir/bin"
source ~/.bash_profile
```

`$PATH:/dir/bin`はPATH変数に任意のディレクトリを追記している記述となるのでこの変更を.bash_profileに反映させれば後は上述したようにshellscript.shでどこからでも実行できるようになる

## コマンド置換
`$()`を用いることでコマンドの結果を使って任意の形式ものを出力できる。
```sh
#!/bin/bash

today=$(date '+%Y-%m-%d')
echo "$today"
```
