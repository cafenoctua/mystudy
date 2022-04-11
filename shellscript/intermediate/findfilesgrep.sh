#!/bin/bash

readonly SCRIPT_NAME=${0##*/}

pattern=$1
directory=$2

if [[ -z $pattern ]]; then
    printf '%s\n' "${SCRIPT_NAME}: missing search pattern" 1>&2
    exit 1
fi

if [[ -z $directory ]]; then
    directory=.
fi

if [[ ! -d $directory ]]; then
    printf '%s\n' "${SCRIPT_NAME}: '$directory': No such directory" 1>&2
    exit 2
fi

find -- "$directory" -type f -print0 | xargs -0 grep -e "$pattern" -- /dev/null