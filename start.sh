#!/bin/bash
source .venv/bin/activate
file="main-numpy.py"
[[ -n $1 ]] && file=$1
clear
ls main-numpy.py numpy_exercices.py | entr sh -c "clear && python $file"
