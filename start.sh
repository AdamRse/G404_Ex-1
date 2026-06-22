#!/bin/bash
source .venv/bin/activate
ls exercices.py | entr -c python exercices.py
