from IPython.display import display
from tabulate import tabulate
import pandas as pd
import numpy as np
from src.snippets.pandas_snippets import convert_column_int, convert_column_float, get_list_from_multiple_value, get_list_from_column
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

def exercice3():
    df = pd.read_csv("data/tips.csv")
    print("-- EXERCICE 3 --\n",df, end=ps)
    # 1. Sélectionner la colonne 'tip' comme une Series
    print(f"(1) Série colonne 'tip' :\n{df["tip"]}", end=ps) # Renvoie une liste, tandis que df[["tip"]] renvoie une série
    # 2. Sélectionner les colonnes 'total_bill' et 'day' comme un DataFrame
    print(f"(2) Colonnes 'total_bill' et 'day' dans un DataFrame :\n{df[["total_bill", "day"]]}", end=ps) # Ou df.loc[:,["total_bill", "day"]]
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

def exercice4():
    data = {
        "eleve": ["Léa", "Hugo", "Sarah", "Maxime", "Inès", "Paul"],
        "python":    ["18", 14, np.nan, 11, 16, 9],
        "sql":       [15, np.nan, 17, 8, np.nan, 12],
        "stats":     [12, 16.0, 14, 10, 15, np.nan],
        "present":   [True, True, True, True, True, False]
    }
    df = pd.DataFrame(data)
    # 1. Faites en sorte que la matière "python" soit de type entier ou flotant
    df["python"] = pd.to_numeric(df["python"])
    print(f"Conversion de la matière python en entier :\n{df["python"]}", end=ps)
    # 2. Diagnostiquer les valeurs manquantes
    print(f"Valeurs manquantes :\n{df.isna()}\nNombre de valeurs manquantes :\n{df.isna().sum()}\ntotal des valeurs manquantes : {df.isna().sum().sum()}", end=ps)
    # 3. Remplir les notes manquantes avec la moyenne de leur matière
    df=df.fillna({
        "python": df["python"].mean(),
        "sql": df["sql"].mean(),
        "stats": df["stats"].mean(),
    })
    print(f"Correction des valeurs manquantes avec la moyenne :\n{df}", end=ps)
    # 4. Créer une colonne "moyenne" (moyenne des 3 matières)
    df["moyenne"] = df[["python", "sql", "stats"]].mean(axis=1)
    print(f"Ajout d'une colonne moyennes :\n{df}", end=ps)
    # 5. Créer une colonne "statut" : "Validé" si moyenne >= 10, "Rattrapage" si entre 8 et 10, "Échec" sinon
    df["statut"] = np.select([df["moyenne"] >= 10, df["moyenne"] >= 8], ["Validé", "Rattrapage"], default="Échec")
    print(f"Correction des valeurs manquantes avec la moyenne :\n{df}", end=ps)
    # 6. Supprimer la colonne "present"
    df=df.drop("present", axis=1)
    print(f"Supression de la colonne 'present' :\n{df}", end=ps)
    # 7. Compter combien d'eleves sont "Validé"
    print(f"Il y a {(df["statut"] == "Validé").sum()} élèves reçu", end=ps)
    # 8. Quelle est la moyenne générale de la promo ?
    print(f"La promo a une moyenne de : {(df["moyenne"].mean()).round(1)}", end=ps)

def exercice5():
    # Création du dataset
    rng = np.random.default_rng(101)
    sites = ["Roanne"] * 10 + ["St-Étienne"] * 10 + ["Lyon"] * 10
    niveaux = rng.choice(["Débutant", "Intermédiaire", "Avancé"], 30, p=[0.5, 0.3, 0.2])
    note = rng.normal(14, 4, 30).round(1).clip(0, 20)
    heures_etude = rng.integers(5, 30, 30)
    abandon = rng.choice([0, 1], 30, p=[0.8, 0.2])
    df = pd.DataFrame({
        "site": sites,
        "niveau": niveaux,
        "note": note,
        "heures_etude": heures_etude,
        "abandon": abandon
    })

    df.head(5)
    print(df, end=ps)
    # 1. Note moyenne par site
    print(f"Calcul de la note moyenne :\n{df.groupby("site")["note"].mean()}", end=ps)
    # 2. Statistiques par site ("mean", "std", "min", "max", "count")
    print(f"Statistiques par site :\n{df.groupby("site")["note"].agg(["mean", "std", "min", "max", "count"])}", end=ps)
    # 3. Note moyenne par site ET par niveau
    print(f"Moyenne par site et niveau :\n{df.groupby(["site", "niveau"])["note"].mean()}", end=ps)
    # 4. Nombre d'apprenants par site
    print(f"Nombre d'apprenants par site :\n{df.groupby("site").size()}", end=ps)
    # 5. Taux d'abandon par site
    print(f"Taux d'abandon par site :\n{df.groupby("site")["abandon"].mean()*100}", end=ps)
    # 6. Heures d'étude moyennes par niveau
    print(f"Heures d'études moyenne par niveaux :\n{df.groupby("niveau")["heures_etude"].mean()}", end=ps)
    # 7. Classement des sites avec la meilleure note moyenne
    print(f"Meilleurs moyennes par sites :\n{df.groupby("site")["note"].mean().sort_values(ascending=False)}", end=ps)

def exercice6():
    test=None
    df = pd.read_csv("data/Pokemon_dataset.csv", delimiter=";")
    df=df.T.set_axis(df.iloc[:,0], axis=1).drop("Unnamed: 0", axis=0)
    df[df.columns[6].split(" / ")]=df[df.columns[6]].str.split(" / ", n=1, expand=True)
    df=df.drop(df.columns[6], axis=1)
    number_columns=['#', 'Total', 'HP', 'Speed', 'Generation', 'Attack',"Sp. Atk", "Sp. Def", 'Defense % of Attack']
    convert_column_float(df, number_columns)
    df = df.sort_values("#", ascending=True)
    df[df[['Speed', 'Attack',"Sp. Atk", "Sp. Def", 'HP']] > 255]=np.nan
    df[df[number_columns] < 1]=np.nan
    df=df.dropna(axis=0, how="all")

    # nettoyage de # ID
    convert_column_int(df, ["#"])

    # nettoyage des HP

    # correction de l'Attack
    stats_no_attack = ['HP', 'Speed', 'Sp. Atk', 'Sp. Def']
    missing_atk=((df['Total'] - df[stats_no_attack].sum(axis=1)) / (1+df['Defense % of Attack']/100)).round()
    df['Attack']=df['Attack'].fillna(missing_atk)

    # nettoyage Name
    df["Name"] = df["Name"].str.lower()
    df["Name"] = df["Name"].str.replace(".+mega ", "mega " ,regex=True)
    df["Name"] = df["Name"].str.title()

    # création colonne défense
    df['Defense'] = ((df['Attack'] * df['Defense % of Attack']) / 100).round()
    #df=df.drop("Defense % of Attack", axis=1)
    convert_column_float(df, ["Defense"])

    # nettoyage Generation
    df["Generation"]=df["Generation"].replace(0, np.nan)
    df["Generation"]=df["Generation"].bfill()
    convert_column_int(df, ["Generation"])

    # nettoyage Types
    df["Types"] = df["Types"].str.replace(r",\s*$", "" ,regex=True)
    types=get_list_from_multiple_value(df["Types"])

    # nettoyage stats
    stats_col = ['HP', 'Speed', 'Attack', 'Sp. Atk', 'Sp. Def', 'Defense']
    is_calculable = df[stats_col].isna().sum(axis=1) < 2
    diff = df['Total'] - df[stats_col].sum(axis=1)
    for col in stats_col:
        condition = is_calculable & df[col].isna()
        df.loc[condition, col] = diff[condition]

    # fix les sommes
    is_calculable = df[stats_col].isna().sum(axis=1) == 0
    df.loc[is_calculable, "Total"]=df[stats_col].sum(axis=1)

    # fix les double NaN dans les stats
    missing_double= df[stats_col].isna().sum(axis=1)
    for col in stats_col:
        df.loc[missing_double >= 2, col] = round(diff[missing_double >= 2]/missing_double)

    df=df[["#", "Name", "Types", "Generation", "Legendary", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]]

    with pd.option_context('display.max_rows', None):  # more options can be specified also
        pass
        #print("TEST :\n", test, end=ps)
    print(tabulate(df, headers=df.columns, tablefmt="double_grid"))

    printWrong("CHECK DES TYPES DE POKEMON :\n", types)

# Exercice Bonus
def exercice7():
    df = pd.read_csv("data/IMDB_dataset.csv", encoding="ISO-8859-1", on_bad_lines='skip', delimiter=";")
    print(df, end=ps)
    printWrong(f"Valeurs manquantes par colonnes :\n{df.isna().sum()}")
    printWrong(f"Valeurs manquantes totales :\n{df.isna().sum().sum()}")
    printSuccess("Nettoyage du CSV", end=ps)

    # colonne unamed 8
    print(f"Analyse de la colonne Unamed: 8, nombre de données manquantes : {df["Unnamed: 8"].isna().sum()}/{df["Unnamed: 8"].shape[0]}")
    df=df.drop(columns="Unnamed: 8")
    printWrong("Supression de la colonne 'Unnamed: 8'", end=ps)

    # supression lignes vides
    df=df.dropna(how="all", axis=0)
    printWrong("Supression des lignes vide", end=ps)

    # Correction des index
    df=df.rename(columns={
        "IMBD title ID":"IMDB title ID",
        "Original titlÊ":"Original Title",
        "Genrë¨":"Genre",
        " Votes ":"Votes"
    })
    printWrong("Correction des index", end=ps)

    # correxion des ID :
    df['IMDB title ID'] = df['IMDB title ID'].str.replace('tt', "")
    printWrong("correction des IDs IMDB", end=ps)
    # nettoyage des titres
    df['Original Title'] = df['Original Title'].str.replace('Ã©', 'é')
    df['Original Title'] = df['Original Title'].str.replace('Ã¹', 'ù')
    df['Original Title'] = df['Original Title'].str.replace('Â·', '-')

    # nettoyage des Genres
    genres=get_list_from_multiple_value(df["Genre"])
    print("LISTE DES GENRES DE FILM :\n", genres)
    print("Pas de correction sur les genres de film", end=ps)


    # nettoyage des durées
    df['Duration'] = df['Duration'].str.replace(r'[^\d.]', '', regex=True)
    df["Duration"] = pd.to_numeric(df["Duration"], errors='coerce', downcast="unsigned")



    # netoyage des pays
    df['Country'] = df['Country'].str.replace('USA', 'US')
    df['Country'] = df['Country'].str.replace('West Germany', 'Germany')
    df['Country'] = df['Country'].str.replace('Italy1', 'Italy')
    df['Country'] = df['Country'].str.replace('Zesland', 'Zealand')
    df['Country'] = df['Country'].str.replace('Zeland', 'Zealand')
    df['Country'] = df['Country'].str.replace('.', '')

    # nettoyage des rating
    printWrong(f"Valeurs de Rating : {get_list_from_column(df["Content Rating"])}")
    df['Content Rating'] = df['Content Rating'].str.replace('Not Rated', "G")
    df['Content Rating'] = df['Content Rating'].str.replace('Approved', "G")
    df['Content Rating'] = df['Content Rating'].str.replace('Unrated', "R")
    printWrong(f"Valeurs de Rating après correction : {get_list_from_column(df["Content Rating"])}", end=ps)

    # nettoyage des incomes
    printWrong(f"correction des IDs IMDB. Valeurs manquantes : {df["Income"].isna().sum()}")
    df['Income'] = df['Income'].str.replace('o', '0')
    df['Income'] = df['Income'].str.replace('$', '')
    df['Income'] = df['Income'].str.replace(',', '')
    df["Income"] = pd.to_numeric(df["Income"])
    printWrong(f"Valeurs manquantes après correction : {df["Income"].isna().sum()}", end=ps)

    # nettoyage des votes
    df['Votes'] = df['Votes'].str.replace(',', '')
    df['Votes'] = df['Votes'].str.replace('.', '')
    df['Votes'] = pd.to_numeric(df['Votes'])


    # nettoyage des scores
    df['Score'] = df['Score'].str.replace(',', '.')
    df['Score'] = df['Score'].str.replace('..', '.')
    df['Score'] = df['Score'].str.replace(r'[^\d.]', '', regex=True)
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')


    # conversion des dates uniformes
    df['Release year'] = pd.to_datetime(df['Release year'], format='mixed', errors='coerce').dt.date


    printSuccess("::::::::::: Données traitées :::::::::::")
    with pd.option_context('display.max_rows', None):  # more options can be specified also
        print(df)


#  MAIN --------------
activate_exercice = [6]
main(activate_exercice, globals())
