#!/bin/bash
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

cd "${SCRIPT_DIR}" || exit 1
source .venv/bin/activate
file="main-pandas.py"
[[ -n $1 ]] && file=$1
clear
find . -path "./.venv" -prune -o -name "*.py" -print | entr sh -c "clear && python $file"
