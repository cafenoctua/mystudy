#!/bin/bash

read str

case "$str" in
    "hoge" ) echo "hoge"
            echo "hoge" ;;
    "fuga" ) echo "" ;;
    * ) echo "unknown" ;;
esac