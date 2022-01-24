#!/bin/bash

printf '%s\n' "$1" \
    | sed 's/[.*\^$[]/\\&/g'