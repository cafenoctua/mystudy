#!/bin/bash

list_recursive ()
{
    local filepath=$1
    local indent=$2
    IFS=$'\n'
    echo "${indent}${filepath##*/}"

    if [ -d "$filepath" ]; then
        local fname
        for fname in $(ls "$filepath")
        do
            list_recursive "${filepath}/${fname}" " $indent"
        done
    fi
}

list_recursive "$1" ""