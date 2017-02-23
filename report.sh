#!/bin/bash
dt=$(date +%Y_%m_%d_%H_%M)
list="Log/${dt// /_}_SUM.txt"
wc -l */*.txt > $list
tasks="Log/${dt// /_}_TASKS.txt"

t=$(ls */*.txt)
for f in $t
do
   echo "============================" >> $tasks
   echo $f >> $tasks
   echo "============================" >> $tasks
   cat $f >> $tasks
done
