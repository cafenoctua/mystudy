#!/bin/bash

read str

if [ "$str" = "hoge" ]; then
    echo "hoge"
elif [ "$str" = "fuga" ]; then
    echo "fuga"
else
    echo "unknown"
fi