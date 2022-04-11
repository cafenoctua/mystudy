#!/bin/bash

declare -i num
num=5
echo $num

declare -a arr1
arr1=(apple banana)
echo ${arr1[0]}
echo ${arr1[1]}

declare -A dict1
dict1=([id]=5 [name]=miyake)
echo ${dict1[id]}
echo ${dict1[name]}