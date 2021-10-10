#!/bin/bash
# -a = amount
# -ULW = Upper Limit Weight
# -LLW = Lower Limit Weight
# -ULV = Upper Limit Value
# -LLV = Lower Limit Value
# -ES (optional) = Exaustive Search
# -ESD (optional) = Exaustive Search and Dynamic Programing
# -b (optional) = begin report
# -c (optional) = continue report
# -e (optional) = end report
# -s (optional) = seed


echo $1 $2 $3 $4 $5
python3 main.py -a $1 -LLW $2 -ULW $3 -LLV $4 -ULV $5 -b

for ((i=1; i<=8; i++))
do
	python3 main.py -a $1 -LLW $2 -ULW $3 -LLV $4 -ULV $5 -c
done

python3 main.py -a $1 -LLW $2 -ULW $3 -LLV $4 -ULV $5 -e


