#!/bin/bash
source .venv/bin/activate
file="main-numpy.py"
[[ -n $1 ]] && file=$1
clear
find . -path "./.venv" -prune -o -name "*.py" -print | entr sh -c "clear && python $file"
