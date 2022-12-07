#!/bin/bash

echo "Day ${1} Parse Input" 
python3.11 -m timeit -s "day = ${1}" -s "from solutions import days" "days[day]['input'](f'inputs/{day:02d}/real.txt')"

echo "Day ${1} Part A"
python3.11 -m timeit -s "day = ${1}" -s "from solutions import days" -s "parsed_input = days[day]['input'](f'inputs/{day:02d}/real.txt')" "days[day]['A'](parsed_input)"

echo "Day ${1} Part B"
python3.11 -m timeit -s "day = ${1}" -s "from solutions import days" -s "parsed_input = days[day]['input'](f'inputs/{day:02d}/real.txt')" "days[day]['B'](parsed_input)"
