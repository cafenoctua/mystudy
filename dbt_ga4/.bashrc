# ~/.bashrc: executed by bash(1) for non-login shells.

eval "`dircolors`"

if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

export PS1='[\[\033[01;32m\]\W\[\033[00m\]] \n\[\033[01;34m\]\$\[\033[00m\] '