#!/bin/bash

python3 main.py -a 3 -s 1024 -b

for ((i=1; i<=1000; i++))
do
    python3 main.py -a 3 -s 1024 -c "$i"
done

python3 main.py -a 3 -s 1024 -e
