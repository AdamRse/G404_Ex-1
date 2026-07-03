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



#  MAIN --------------
activate_exercice = [1]
main(activate_exercice, globals())
