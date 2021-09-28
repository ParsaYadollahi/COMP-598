#!/bin/bash

# The number of lines in the file
wc -l < $1 | sed 's/ //g'

# The first line of the file (i.e., the header row)
sed -n '1p' < $1

# The number of lines in the last 10,000 rows of the file that contain the string “potus” (case-insensitive).
tail -10000 $1 | grep -c -in "potus"

# Of rows 100 – 200 (inclusive), how many of them that contain the word “fake”
sed -n '0,200000p' < $1 | grep -c "fake"
