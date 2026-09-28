import pandas as pd
import numpy as np
import os
from pathlib import Path
import io
from contextlib import redirect_stdout
import re

SCRIPT_DIR = str(Path(__file__).resolve().parent)
OUTPUT_DIR = f"{SCRIPT_DIR}/../outputs"
OUTPUT_FILE_NAME = "analyse"
DATA_FILES_DIR = str(Path(__file__).resolve().parent)+"/../data"
DATA_FILES = [f.name for f in os.scandir(DATA_FILES_DIR) if f.is_file()]
OUTPUT_FILE = f"{OUTPUT_DIR}/recherche.txt"
SEUIL_VALEURS_UNIQUES = 30

sp="\n"+("-"*50)+"\n"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    # Ouverture en mode "w" : écrase le fichier s'il existe
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for file in DATA_FILES:
            analyze_csv_file(DATA_FILES_DIR+"/"+file, f)
