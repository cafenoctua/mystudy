#!/bin/bash

# 日記データを保存するディレクトリ設定
directory="./diary"

# データ保存のディレクトリがなければ作成する
if [ ! -d "$directory" ]; then
    mkdir "$directory"
fi

vi "${directory}/$(date '+%Y-%m-%d').txt"