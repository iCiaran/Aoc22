#!/bin/bash

INIT_PATH="solutions/__init__.py"

echo "from .util import *" > $INIT_PATH

for day in $(ls solutions/day_* 2> /dev/null)
do
    filename=$(basename -- "$day")
    day_number=$(echo "${filename%.*}" | cut -d '_' -f2)
    echo 'from .day_##DAY## import a as _##DAY##_a, b as _##DAY##_b, parse_input as _##DAY##_parse_input' | sed -e "s/##DAY##/${day_number}/g" >> $INIT_PATH
done

echo -e "\ndays = {" >> $INIT_PATH

for day in $(ls solutions/day_* 2> /dev/null)
do
    filename=$(basename -- "$day")
    day_number=$(echo "${filename%.*}" | cut -d '_' -f2)
    day_number_stripped=$(echo $day_number | awk '{print $1 + 0}')
    echo "    ##STRIPPED##: {\"A\": _##DAY##_a, \"B\": _##DAY##_b, \"input\": _##DAY##_parse_input}," | sed -e "s/##DAY##/${day_number}/g" -e "s/##STRIPPED##/${day_number_stripped}/g" >> $INIT_PATH
done

echo "}" >> $INIT_PATH