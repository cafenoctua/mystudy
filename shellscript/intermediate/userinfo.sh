#!/bin/bash

readonly SCRIPT_NAME=${0##*/}

user=$1

if [[ -z $user ]]; then
    printf '%s\n' "${SCRIPT_NAME}: missing username" 1>&2
    exit 1
fi

cat /etc/passwd \
    | grep "^${user}:" \
    | {
        IFS=: read -r username password userid groupid \
                        comment homedirectory loginshell

        if [[ $? -ne 0 ]]; then
            printf '%s\n' "${SCRIPT_NAME}: '$user': No such user" 1>&2
            exit 2
        fi

        cat <<END
username = $username
userid = $userid
groupid = $groupid
homedirectory = $homedirectory
loginshell = $loginshell
END
    }