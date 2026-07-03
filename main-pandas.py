import pandas as pd
import numpy as np
from src.header.head import main, printSuccess, printError, printWrong, bcolors # NOQA

ps="\n"+("-"*50)+"\n\n"
# Cours : https://github.com/G404-Data-Analyst/Formation_Data_Analyst/blob/main/numpy_et_pandas_cours.ipynb

def exercice1():
    etudiants = {
        "prenom": ["Lucas", "Emma", "Hugo", "Léa", "Tom"],
        "age":    [23, 28, 19, 32, 26],
        "ville":   ["Roanne", "Saint-Étienne", "Roanne", "Lyon", "Saint-Étienne"],
        "niveau d'études": ["Licence", "Master", "Licence", "Master", "Master"]
    }
    etudiantsDF=pd.DataFrame(etudiants)
    # 1. Depuis le dictionnaire créez un DataFrame
    print(f"Création d'un dataframe :\n{etudiantsDF}", end=ps)
    # 2. Créez un array de 10 lignes x 3 colonnes de notes aléatoires entre 0 et 20 (utilisez seed=123)
    rng = np.random.default_rng(123)
    notes = rng.integers(0, 21, (10, 3))
    print(f"Créations d'un tableau de notes 3x10 :\n{notes}", end=ps)
    # Nommez les colonnes "matiere1", "matiere2", "matiere3", mettez-les dans un nouveau DataFrame
    noteDF=pd.DataFrame(
        notes,
        columns=["matiere1", "matiere2", "matiere3"]
    )
    print(f"Dataframe avec colonnes :\n{noteDF}", end=ps)
    # 3. Afficher la forme des deux DataFrames
    print(f"Forme des du dataframe notes :\n{noteDF.shape}\nForme du dataframe étudiants :\n{etudiantsDF.shape}", end=ps)
    # 4. Trouver trois facons de joindre ces deux DataFrames, et sauvegarder le resultat dans un nouveau DataFrame
    nouveauDF=etudiantsDF.join(noteDF)
    nouveauDF=etudiantsDF.merge(noteDF, left_index=True, right_index=True)
    nouveauDF=pd.concat([etudiantsDF, noteDF], axis=1, join="inner")
    print(f"Dataframe fusionné :\n{nouveauDF}", end=ps)
    # 5. Créer un 4e DataFrame en ne gardant que les colonnes prenom et matiere1
    notesPM=nouveauDF.drop(columns=["age", "matiere2", "matiere3", "niveau d'études", "ville"])
    notesPM=pd.DataFrame(nouveauDF, columns=["prenom", "matiere1"])
    notesPM=nouveauDF[["prenom", "matiere1"]]
    print(f"On ne garde que prénoms et matière1 :\n{notesPM}", end=ps)

def exercice2():
    # Charger les données
    df = pd.read_csv("data/tips.csv")
    print("---Exercice 2 ---\n", df, end=ps)
    # 1. Dimensions du dataframe
    print(f"(1) Dimension du dataFrame :\n{df.shape}", end=ps)
    # 2. Liste des colonnes
    print(f"(2) Liste des colonnes :\n{df.columns.values}", end=ps)
    # 3. Types des colonnes
    print(f"(3) Types des colonnes :\n{df.dtypes}", end=ps)
    # 4. print des 5 premières lignes
    print(f"(4) 5 Premières lignes du DataFrame :\n{df.head(5)}", end=ps)
    # 5. Faire un résumé statistique
    print(f"(5) Résumée statistique :\n{df.describe(include="all")}", end=ps)
    # 6. Combien a-t-on de valeurs uniques par colonne ?
    print(f"(6) Nombre de valeurs unique par colonne :\n{df.nunique()}", end="\n___\n\n")
    # 7. Y a-t-il des valeurs manquantes ? Si oui combien au total ?
    print(f"(7) Valeurs manquantes :\n{df.isna().sum()}", end=ps)
    # 8. Quel jour y a-t-il le plus de clients ?
    print(f"(8) Jour avec le plus de clients :\n{df.value_counts("day").idxmax()}", end=ps)

#  MAIN --------------
activate_exercice = [2]
main(activate_exercice, globals())
