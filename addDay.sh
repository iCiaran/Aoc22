#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <Day number>"
    exit 1
fi

if [[ ! ${1} =~ ^[0-9]+$ ]]; then 
    echo "Day number must be an integer" 
    exit 1
fi

if [[ ! ${1} -gt 0 ]] || [[ ! ${1} -le 25 ]] ;then
    echo "Day number must be in the range [1,25]"
    exit 1
fi

DAY=$(printf "%02d" ${1})

if [ -f "solutions/day_${DAY}.py" ]; then
    echo "Day ${DAY} already exists"
    exit 1
fi

sed -e "s/##DAY##/${DAY}/g" day.py.tpl > "solutions/day_${DAY}.py"

mkdir -p inputs/${DAY}
touch inputs/${DAY}/real.txt
