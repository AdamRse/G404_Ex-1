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
SEUIL_TAILLES_UNIQUES = 8

sp="\n"+("-"*50)+"\n"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def show_unique_length(df: pd.DataFrame, seuil: int = SEUIL_TAILLES_UNIQUES) -> pd.DataFrame:
    """
    Pour chaque colonne de type string ayant au plus `seuil` longueurs
    de chaînes différentes, retourne un tableau où :
      - l'index  = nom de la colonne
      - colonne 'nb tailles'          = nombre de longueurs distinctes
      - colonnes 'taille 1', 'taille 2', ... = la PREMIÈRE valeur
        rencontrée pour chaque longueur, triée par longueur croissante

    Les colonnes avec plus de `seuil` longueurs différentes sont ignorées,
    de même que les colonnes non-string (numériques, booléennes...).
    """
    result = {}
    for col in df.columns:
        serie = df[col].dropna()

        # Ne garder que les colonnes 100% string
        if serie.empty or not serie.map(lambda x: isinstance(x, str)).all():
            continue

        longueurs = serie.str.len()
        nb_tailles = longueurs.nunique()
        if nb_tailles > seuil:
            continue

        # Première valeur de chaque groupe de longueur, triée par longueur
        exemples = (serie.to_frame("valeur")
                         .assign(longueur=longueurs)
                         .groupby("longueur")["valeur"]
                         .first()
                         .sort_index())

        result[col] = [nb_tailles] + [trunc_any(v) for v in exemples.tolist()]

    if not result:
        return pd.DataFrame({f"Aucune colonne string avec moins de {seuil} tailles uniques.\n"})

    nb_max = max(len(v) for v in result.values())
    entetes = ["nb tailles"] + [f"taille {i}" for i in range(1, nb_max)]
    for v in result.values():
        v.extend([""] * (nb_max - len(v)))

    return pd.DataFrame(result, index=entetes).T

def initialiser_recherche_exception_json():
    """
    Crée 'recherche_exception.json' à la racine du projet, pré-rempli avec :
      - les noms des scripts (clés, depuis SCRIPTS)
      - les noms des .csv présents dans ../data (récupérés dynamiquement)
    Si le fichier existe déjà, il n'est PAS écrasé.
    """
    chemin_json=f"{SCRIPT_DIR}/../recherche_exception.json"
    scripts=DATA_FILES
    if chemin_json.exists():
        print(f"[INFO] '{chemin_json}' existe déjà → aucune modification.")
        return

    # Noms des fichiers de données, récupérés dynamiquement (comme dans 01_analyse.py)
    data_files = sorted(f.name for f in DATA_DIR.iterdir() if f.is_file())

    contenu = {
        script: {csv: {} for csv in data_files}
        for script in scripts
    }

    with open(chemin_json, "w", encoding="utf-8") as f:
        json.dump(contenu, f, indent=2, ensure_ascii=False)

    print(f"[OK] '{chemin_json.name}' créé : "
          f"{len(scripts)} script(s), {len(data_files)} fichier(s) de données.")

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

        # Recherche des tailles uniques
        unique_str = show_unique_length(df)
        print(f"TAILLES DES CELLULES (seuil : {SEUIL_TAILLES_UNIQUES}\n")
        print(unique_str, end=sp)



    content = buffer.getvalue()

    # Écriture à la suite dans le fichier (déjà ouvert en "w" par main)
    if output_f is not None:
        output_f.write(content)

    # Affichage console
    print(content)

main()
