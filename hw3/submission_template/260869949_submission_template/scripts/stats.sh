# #!/bin/bash

# # Word Count
# wordCount=$(wc -l < $1)
# if [[ $wordCount -lt 10000 ]]
# then
#     echo Error: File is less than 10000 lines long
#     exit 1
# fi

# # The number of lines in the file
# wc -l < $1 | sed 's/ //g'

# # The first line of the file (i.e., the header row)
# sed -n '1p' < $1

# # The number of lines in the last 10,000 rows of the file that contain the string “potus” (case-insensitive).
# tail -10000 $1 | grep -c -in "potus"

# # Of rows 100 – 200 (inclusive), how many of them that contain the word “fake”
# sed -n '100,200p' < $1 | grep -c "fake"


#!/bin/bash

fileWordCount=$(wc -l < $1)
if [[ $fileWordCount -lt 10000 ]]
then
    echo Error: File is less than 10000 lines long
    exit 1
fi

wc -l < $1
head -1 $1
tail -10000 $1 | grep -c -i "potus"
head -200 $1 | tail -100 | grep -c "fake"
