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
    print(f"(2) Liste des colonnes :\n{df.columns}", end=ps)
    # 3. Types des colonnes
    print(f"(3) Types des colonnes :\n{df.dtypes}", end=ps)
    # 4. print des 5 premières lignes
    print(f"(4) 5 Premières lignes du DataFrame :\n{df.head(5)}", end=ps)
    # 5. Faire un résumé statistique
    print(f"(5) Résumée statistique :\n{df.describe(include="all")}", end=ps)
    # 6. Combien a-t-on de valeurs uniques par colonne ?
    print(f"(6) Nombre de valeurs unique par colonne :\n{df.nunique()}", end="\n___\n\n")
    # 7. Y a-t-il des valeurs manquantes ? Si oui combien au total ?
    print(f"(7) Valeurs manquantes :\n{df.isna().sum()}\nAu total : {df.isna().sum().sum()}", end=ps)
    # 8. Quel jour y a-t-il le plus de clients ?
    print(f"(8) Jour avec le plus de clients :\n{df.value_counts("day").idxmax()}", end=ps) # df['day'].mode()[0] ou df["index"].value_counts().index[0]
    # 9. Trouver la distribution de la semaine en % de chaque journée
    countedDF=df.value_counts("day")
    perDayDF = round(countedDF/countedDF.sum()*100, 2)
    print(f"(9) Distribution par jour :\n{perDayDF}", end=ps)
    # 10. Trouver le nombre de tables par jour (size = nombre de tables)
    print(f"(10) Tables par jour :\n{(df.groupby("day")["size"].sum()/df["size"].sum()*100).round(2)}")
    print("TEST\n",df.groupby("day")["size"].sum())

def exercice3():
    df = pd.read_csv("data/tips.csv")
    print("-- EXERCICE 3 --\n",df, end=ps)
    # 1. Sélectionner la colonne 'tip' comme une Series
    print(f"(1) Série colonne 'tip' :\n{df["tip"]}", end=ps) # Renvoie une liste, tandis que df[["tip"]] renvoie une série
    # 2. Sélectionner les colonnes 'total_bill' et 'day' comme un DataFrame
    print(f"(2) Colonnes 'total_bill' et 'day' dans un DataFrame :\n{df[["total_bill", "day"]]}", end=ps)
    # 3. Afficher les 5 premières lignes avec .loc
    print(f"(3) 5 premières lignes avec .loc :\n{df.loc[:4]}", end=ps)
    # 4. Afficher les lignes 10 à 15 (incluses), avec les colonnes 'tip' et 'sex'
    print(f"(4) Lignes 10 à 15 inclues :\n{df.loc[10:15]}", end=ps)
    # 5. Afficher la 3e ligne avec .iloc
    print(f"(5) Lignes 3 avec iloc :\n{df.iloc[2]}", end=ps)
    # 6. Filtrer les repas avec total_bill > 30
    print(f"(6) Filtrer les repas > 30 :\n{df.loc[df["total_bill"] > 30]}", end=ps)
    # 7. Filtrer les repas du dimanche (Sun) avec un tip > 5
    print(f"(7) Filtrer les repas du dimanche avec un tip > 5 :\n{df.loc[(df["day"] == "Sun") & (df["tip"] > 5)]}", end=ps)
    # 8. Filtrer les repas du soir (Dinner) avec plus de 3 personnes
    print(f"(8) Repas du soir avec >3 personnes :\n{df.loc[(df["time"] == "Dinner") & (df["size"] > 3)]}", end=ps)
    # 9. Quelle est la moyenne du tip pour les repas de plus de 40€ ?
    print(f"(9) Moyenne du tip quand >40€ :\n{df["tip"].loc[(df["total_bill"] > 40)].mean()}", end=ps)
    # 10. Combien de femmes ont laissé un tip supérieur à 5€ ?
    print(f"(10) Combien de femmes ont laissé un tip supérieur à 5€ ? :\n{len(df.loc[(df["tip"] > 5) & (df["sex"] == "Female")])}")

#  MAIN --------------
activate_exercice = [3]
main(activate_exercice, globals())
