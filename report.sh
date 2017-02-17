#!/bin/bash
dt=$(date +%Y_%m_%d_%H_%M)
list="${dt// /_}_SUM.txt"
echo $list
wc -l */*.txt > $list
tasks="${dt// /_}_TASKS.txt"

cat */*.txt > $tasks
