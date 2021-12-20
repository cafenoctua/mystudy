#!/bin/bash

usage()
{
    # シェルスクリプトのファイル名を取得
    local script_name=$(basename "$0")
    # ヒアドキュメントでヘルプを表示
    cat << END
Usage: $script_name PATTERN [PATH] [NAME_PATTERN]
Find file in current directory recursively, and print lines which match PATTERN.
    
    PATH            find file in PATH directory, instead of current directory
    NAME_PATTERN    specify name pattern to find file

Examples:
    $script_name return
    $script_name return ~ '*.txt'
END
}

# コマンドライン引数が0個のとき(何も指定されないとき)
if [ "$#" -eq 0 ]; then
    usage
    exit 1
fi

pattern=$1
directory=$2
name=$3

if [ -z "$directory" ]; then
    directory='.'
fi

if [ -z "$name" ]; then
    name='*'
fi

find "$directory" -type f -name "$name" | xargs grep -nH "$pattern"