import pandas as pd
import numpy as np
import os
from pathlib import Path
import io
from contextlib import redirect_stdout

SCRIPT_DIR = str(Path(__file__).resolve().parent)
OUTPUT_DIR = f"{SCRIPT_DIR}/../outputs"
sp="\n\n"+("-"*50)+"\n\n"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv("/home/adam/dev/projets/exercice1-python/projetspython/TP_Klaus/data/01_ACTIVITE.csv", sep=";")
resume = pd.DataFrame({
    "Type": df.dtypes
    , "Nb uniques": df.nunique()
    , "Nb Manquants": df.isnull().sum()
    , "% Manquants": round(df.isnull().mean() * 100, 2)
})
print(df, end=sp)
print(resume, end=sp)
print("Total duplicates : ", df.duplicated().sum(), end=sp)

buffer = io.StringIO()
with redirect_stdout(buffer):
    print(df, end=sp)
    print(resume, end=sp)
    print("Total duplicates : ", df.duplicated().sum(), end=sp)

# Écriture dans le fichier
with open(f"{OUTPUT_DIR}/rapport_activite.txt", "w", encoding="utf-8") as f:
    f.write(buffer.getvalue())

# Optionnel : afficher quand même à l'écran
print(buffer.getvalue())
