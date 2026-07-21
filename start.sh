#!/bin/bash
SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"

IDE_PROCESS_NAME="zed-editor"

cd "${SCRIPT_DIR}" || exit 1
if ! pgrep -x "${IDE_PROCESS_NAME}"; then
    zed .
fi
source .venv/bin/activate
file="main_matplotlib.py"
[[ -n $1 ]] && file=$1
clear
find . -path "./.venv" -prune -o -name "*.py" -print | entr sh -c "clear && python $file"
