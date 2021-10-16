#!/bin/bash
input=$1
output=$2

awk 'BEGIN{FS=","; OFS=","} $2 ~ /2020/' $input > $output
