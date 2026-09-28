import pandas as pd
import numpy as np
import os
from pathlib import Path
import io
from contextlib import redirect_stdout
import re

SCRIPT_DIR = str(Path(__file__).resolve().parent)
OUTPUT_DIR = f"{SCRIPT_DIR}/../outputs"
OUTPUT_FILE_NAME = f"rapport_analyse.txt"
DATA_FILES_DIR = str(Path(__file__).resolve().parent)+"/../data"
DATA_FILES = [f.name for f in os.scandir(DATA_FILES_DIR) if f.is_file()]
SEUIL_VALEURS_UNIQUES = 30

sp="\n"+("-"*50)+"\n"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    # Ouverture en mode "w" : écrase le fichier s'il existe
    with open(f"{OUTPUT_DIR}/{OUTPUT_FILE_NAME}", "w", encoding="utf-8") as f:
        for file in DATA_FILES:
            analyze_csv_file(DATA_FILES_DIR+"/"+file, f)

def trunc_any(x, nb_trunc:int=50):
    strX = str(x)
    if len(strX)>nb_trunc:
        return strX[:(nb_trunc-3)]+"..."
    return strX

def test_exceptions(df: pd.DataFrame, colonnes_patterns: list[list[str]]):
    """
    Pour chaque couple [nom_colonne, pattern_regex], compte les valeurs
    qui ne correspondent PAS au pattern et les liste.
    """
    data = {}
    for col, pattern in colonnes_patterns:
        if col not in df.columns:
            data[col] = ["[ colonne absente ]"]
            continue

        series = df[col].dropna().astype(str)
        mask = ~series.str.contains(pattern, regex=True)
        exceptions = series[mask].unique().tolist()
        exceptions = sorted(exceptions, key=lambda x: str(x))

        data[col] = [f"{pattern}"] \
                  + [f"[ {len(exceptions)} exceptions ]"] \
                  + [trunc_any(v) for v in exceptions]

    if not data:
        return pd.DataFrame({"Aucune colonne à tester.\n"})

    max_len = max(len(v) for v in data.values())
    for v in data.values():
        v.extend([""] * (max_len - len(v)))

    return pd.DataFrame(data)

def valeurs_ne_matchant_pas(serie: pd.Series, pattern: str) -> pd.Series:
    """
    Retourne les valeurs de `serie` qui ne correspondent PAS au pattern regex.
    Les valeurs non-string (NaN, chiffres...) sont traitées comme non-matchantes
    et exclues via dropna.
    """
    est_match = serie.astype("string").str.fullmatch(pattern, na=False)
    return serie[~est_match].dropna().unique()

def lister_valeurs_uniques(df: pd.DataFrame, seuil: int = SEUIL_VALEURS_UNIQUES):
    """
    Pour chaque colonne ayant moins de `seuil` valeurs uniques,
    retourne un tableau où :
      - l'en-tête = nom de la colonne
      - ligne 0 = nombre de valeurs uniques
      - lignes suivantes = les valeurs uniques triées
    """
    data = {}
    for col in df.columns:
        nb_uniques = df[col].nunique(dropna=True)
        if nb_uniques <= seuil:
            uniques = df[col].dropna().unique().tolist()
            uniques = sorted(uniques, key=lambda x: str(x))
            data[col] = [f"[ {nb_uniques} uniques ]"] + [trunc_any(v) for v in uniques]

    if not data:
        return pd.DataFrame({f"Aucune colonne avec moins de {seuil} valeurs uniques.\n"})

    max_len = max(len(v) for v in data.values())
    for v in data.values():
        v.extend([""] * (max_len - len(v)))

    return pd.DataFrame(data)

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
        # Résumée des colonnes
        print("\n\n"+("_"*100)+"\n"+("*"*100)+f"\n** ANALYSE DE {Path(filePath).name} **\n"+("*"*100))
        print(resume, end=sp)
        print("Total duplicats : ", df.duplicated().sum(), end=sp)

        # Valeurs uniques
        print(f"VALEURS UNIQUES (seuil : {SEUIL_VALEURS_UNIQUES})\n")
        uniques = lister_valeurs_uniques(df, SEUIL_VALEURS_UNIQUES).to_string(index=False)
        print(uniques, end=sp)

        # Recherche de pattern divergents
        col_exceptions = [
            ["ID_Operation", r"OP-[0-9]{7}"]
        ]
        print("TEST DES PATTERNS\n")
        print(test_exceptions(df, col_exceptions).to_string(index=False), end=sp)

    content = buffer.getvalue()

    # Écriture à la suite dans le fichier (déjà ouvert en "w" par main)
    if output_f is not None:
        output_f.write(content)

    # Affichage console
    print(content)

main()
