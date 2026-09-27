import pandas as pd
import numpy as np
import os
from pathlib import Path
import io
from contextlib import redirect_stdout

SCRIPT_DIR = str(Path(__file__).resolve().parent)
OUTPUT_DIR = f"{SCRIPT_DIR}/../outputs"
DATA_FILES_DIR = str(Path(__file__).resolve().parent)+"/../data"
DATA_FILES = [f.name for f in os.scandir(DATA_FILES_DIR) if f.is_file()]

sp="\n"+("-"*50)+"\n"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    output_file = f"{OUTPUT_DIR}/rapport_analyse.txt"
    # Ouverture en mode "w" : écrase le fichier s'il existe
    with open(output_file, "w", encoding="utf-8") as f:
        for file in DATA_FILES:
            analyze_csv_file(DATA_FILES_DIR+"/"+file, f)

def trunc_any(x, nb_trunc:int=50):
    strX = str(x)
    if len(strX)>nb_trunc:
        return strX[:(nb_trunc-3)]+"..."
    return strX

def analyze_csv_file(filePath:str, output_f=None, separator:str=";"):
    df = pd.read_csv(filePath, sep=separator)
    dfDropNa = df.dropna()

    resume = pd.DataFrame({
        "Type": df.dtypes
        , "Nb uniques": df.nunique()
        , "Nb Manquants": df.isnull().sum()
        , "% Manquants": round(df.isnull().mean() * 100, 2)
        , "Première entrée" : dfDropNa.bfill().iloc[0].map(trunc_any)
        , "Dernière entrée" : dfDropNa.ffill().iloc[-1].map(trunc_any)
    })

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print("\n\n"+("_"*100)+"\n"+("*"*100)+f"\n** ANALYSE DE {Path(filePath).name} **\n"+("*"*100))
        print(resume, end=sp)
        print("Total duplicats : ", df.duplicated().sum(), end=sp)

    content = buffer.getvalue()

    # Écriture à la suite dans le fichier (déjà ouvert en "w" par main)
    if output_f is not None:
        output_f.write(content)

    # Affichage console
    print(content)

main()
