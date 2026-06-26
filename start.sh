#!/bin/bash
source .venv/bin/activate
file="main.py"
[[ -n $1 ]] && file=$1
clear
ls exercices.py main.py regex.py | entr -c python $file
