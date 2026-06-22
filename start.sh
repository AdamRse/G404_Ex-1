#!/bin/bash
source .venv/bin/activate
ls exercices.py main.py | entr -c python main.py
