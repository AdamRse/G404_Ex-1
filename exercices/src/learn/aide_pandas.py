import pandas as pd
import numpy as np

ps = "\n" + ("-" * 50) + "\n\n"


print("--- DÉBUT DE L'EXERCICE 2 ---", end=ps)
# Données de base
donnees = {
    "prenom": ["Lucas", "Emma", "Hugo", "Léa", "Tom", "Chloé"],
    "nom": ["Dupont", "Martin", "Bernard", "Petit", "Robert", "Richard"],
    "ville": ["Roanne", "Lyon", "Roanne", "Saint-Étienne", "Lyon", "Roanne"],
    "maths": [12.5, 19.5, 8.0, 14.0, 18.5, 9.0],
    "python": [15.0, 14.0, 10.0, np.nan, 16.0, 11.0] # Note manquante pour Léa
}

# 1. Création du DataFrame
df = pd.DataFrame(donnees)
print(f"DataFrame initial :\n{df}", end=ps)

# 2. Fusionner les colonnes 'prenom' et 'nom' en une nouvelle colonne 'nom_complet'
# Méthode 1 : Concaténation simple (opérateur +)
df['nom_complet'] = df['prenom'] + " " + df['nom']

# Méthode 2 : Utilisation des méthodes de string de Pandas (str.cat)
# df['nom_complet'] = df['prenom'].str.cat(df['nom'], sep=" ")

# Nettoyage : on supprime les anciennes colonnes et on réorganise
df = df.drop(columns=['prenom', 'nom'])
df = df[['nom_complet', 'ville', 'maths', 'python']] # Réorganisation des colonnes
print(f"Après fusion du prénom et nom :\n{df}", end=ps)

# 3. Gérer les valeurs manquantes (NaN)
# Remplaçons la note manquante de Python par un 0
df['python'] = df['python'].fillna(0)
print(f"Après gestion des valeurs manquantes :\n{df}", end=ps)

# 4. Augmenter la note de maths de 2 points, limitée à 20 maximum
# C'est ici qu'on voit la puissance de la vectorisation (sans boucle !)

# Méthode 1 : Utilisation de la méthode native .clip() de Pandas (La plus "Pandas")
df['maths'] = (df['maths'] + 2).clip(upper=20)

# Méthode 2 : Utilisation de numpy.minimum
# df['maths'] = np.minimum(df['maths'] + 2, 20)

# Méthode 3 : Utilisation de numpy.where (Si Condition Vraie -> Fais A, Sinon -> Fais B)
# df['maths'] = np.where(df['maths'] + 2 > 20, 20, df['maths'] + 2)
print(f"Notes de maths augmentées de 2 points (max 20) :\n{df}", end=ps)

# 5. Modifier certaines lignes : Bonus de +1 point en Python pour les étudiants de Roanne
# On utilise .loc[lignes, colonnes] qui est LA bonne pratique pour modifier des données
masque_roanne = df['ville'] == "Roanne"

# On applique le +1 uniquement sur les lignes correspondantes et on s'assure de ne pas dépasser 20
df.loc[masque_roanne, 'python'] = (df.loc[masque_roanne, 'python'] + 1).clip(upper=20)
print(f"Bonus d'un point en Python pour les étudiants de Roanne :\n{df}", end=ps)

# 6. Calculer la moyenne de chaque étudiant sur les deux matières
# L'argument axis=1 indique qu'on fait la moyenne sur les colonnes (horizontalement)
df['moyenne_generale'] = df[['maths', 'python']].mean(axis=1)
print(f"Calcul des moyennes :\n{df}", end=ps)

# 7. Filtrer et trier : Ne garder que les étudiants ayant la moyenne, triés du meilleur au moins bon
# Méthode 1 : Masque booléen et sort_values
df_admis = df[df['moyenne_generale'] >= 10].sort_values(by='moyenne_generale', ascending=False)

# Méthode 2 : Utilisation de la méthode query() (Très lisible pour les requêtes complexes)
# df_admis = df.query("moyenne_generale >= 10").sort_values(by='moyenne_generale', ascending=False)

print(f"Étudiants admis (Moyenne >= 10) :\n{df_admis}", end=ps)

# ----------------------------------------------------

print("--- DÉBUT DE L'EXERCICE 3 ---", end=ps)

# --- 1. ARRIVÉE DE DONNÉES EXTERNES 1 : Une liste brute sans index ---
# On reçoit une simple liste de mentions/appréciations envoyée par un professeur.
# Problème : C'est une liste Python pure. Il faut la transformer et l'aligner.
appreciations = ["Passable", "Excellent", "Insuffisant", "Bien", "Très Bien", "Insuffisant"]

# Méthode 1 : Insertion directe comme nouvelle colonne (Pandas aligne automatiquement via l'index de position)
df['appreciation'] = appreciations

# Méthode 2 : Si on voulait être plus rigoureux et en faire une Série avec le même index
# df['appreciation'] = pd.Series(appreciations, index=df.index)


# --- 2. ARRIVÉE DE DONNÉES EXTERNES 2 : Un dictionnaire d'identifiants uniques ---
# Dans une base de données, on utilise des ID. On nous fournit ce dictionnaire de correspondance.
# Attention : Il manque l'ID de "Tom Robert" et il y a un étudiant en trop ("Sarah Connor").
chiffrement_id = {
    "Lucas Dupont": "ID-001",
    "Emma Martin": "ID-002",
    "Hugo Bernard": "ID-003",
    "Léa Petit": "ID-004",
    "Chloé Richard": "ID-006",
    "Sarah Connor": "ID-999"
}

# Pour fusionner proprement avec les principes de jointure (join/merge), transformons ce dictionnaire en DataFrame
df_id = pd.DataFrame(list(chiffrement_id.items()), columns=['nom_complet', 'etudiant_id'])

# Fusion par jointure : On veut TOUS les étudiants de notre DF principal, même si leur ID est manquant (Left Join)
# Méthode 1 : .merge() avec positionnement à gauche (La plus fréquente et flexible)
df = pd.merge(df, df_id, on='nom_complet', how='left')

# Méthode 2 : En utilisant .join() (Nécessite de mettre la clé de jointure en index pour au moins un des deux DF)
# df = df.join(df_id.set_index('nom_complet'), on='nom_complet', how='left')

print(f"Après intégration des appréciations et des ID (Left Join) :\n{df}", end=ps)


# --- 3. ARRIVÉE DE DONNÉES EXTERNES 3 : Une mise à jour de notes (Fichier correctif) ---
# Le professeur de Python s'est trompé. Il fournit un DataFrame de correction.
# Il contient l'ID de l'étudiant et la nouvelle note.
correctif_data = {
    "etudiant_id": ["ID-003", "ID-004", "ID-001"],
    "python_correct": [12.0, 14.5, 15.0]
}
df_correctif = pd.DataFrame(correctif_data)

# Objectif : Mettre à jour la colonne 'python' du DF principal en ciblant les bonnes lignes grâce à l'ID.
# Étape A : On fait une jointure pour ramener la colonne corrective
df = pd.merge(df, df_correctif, on='etudiant_id', how='left')

# Étape B : On met à jour la colonne 'python' uniquement là où il y a une correction (où python_correct n'est pas NaN)
# Méthode 1 : Utilisation de .combine_first() (Remplace les valeurs du premier DF par le second si le premier est NaN, ou inversement selon la logique. Ici on fait l'inverse : on écrase)
# On va plutôt utiliser .loc avec un masque pour cibler précisément la zone à modifier
masque_correction = df['python_correct'].notna()
df.loc[masque_correction, 'python'] = df.loc[masque_correction, 'python_correct']

# Étape C : Nettoyage de la colonne temporaire
df = df.drop(columns=['python_correct'])

print(f"Après application du correctif de notes en Python :\n{df}", end=ps)


# --- 4. RÉORGANISATION DU DATAFRAME ET RECALCUL ---
# Suite aux modifications, la moyenne générale n'est plus bonne, et l'ordre des colonnes est chaotique.

# A. Recalcul de la moyenne de manière vectorisée
df['moyenne_generale'] = df[['maths', 'python']].mean(axis=1)

# B. Remplacement du NaN de l'ID de Tom (ID manquant lors du left join) par "INCONNU"
df['etudiant_id'] = df['etudiant_id'].fillna('ID-UNKNOWN')

# C. Réorganisation complète : Mettre l'ID en premier, puis le Nom, et enfin le reste.
ordre_colonnes = ['etudiant_id', 'nom_complet', 'ville', 'maths', 'python', 'moyenne_generale', 'appreciation']
df = df[ordre_colonnes]

# D. Définir l'ID comme le nouvel Index du DataFrame (Pratique courante en Data Analyse)
df = df.set_index('etudiant_id')

print(f"DataFrame final réorganisé, indexé et corrigé :\n{df}", end=ps)

#-------------------------------------------
print("-"*100, end=ps)
print("--- DÉBUT DE L'EXERCICE 4 (cc) ---", end=ps)
#-------------------------------------------
# Exercice 2 : élèves et notes
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 150)

eleves = {
    "nom": ["Girard", "Lambert", "Bonnet", "François", "Martinez", "Legrand", "Garnier", "Faure"],
    "prenom": ["Camille", "Sarah", "Nathan", "Chloé", "Enzo", "Manon", "Louis", "Inès"],
    "age": [17, 16, 18, 17, 16, 17, 18, 16],
    "ville": ["Roanne", "Saint-Étienne", "Lyon", "Roanne", "Saint-Étienne", "Lyon", "Roanne", "Saint-Étienne"],
    "classe": ["Première", "Terminale", "Première", "Terminale", "Première", "Première", "Terminale", "Terminale"]
}
elevesDF = pd.DataFrame(eleves)
# 1. Depuis le dictionnaire, créez un DataFrame
print(f"Création du dataframe élèves :\n{elevesDF}", end=ps)

# 2. Créez un array de 8 lignes x 3 colonnes de notes aléatoires entre 0 et 20 (seed=7)
#    Nommez les colonnes "maths", "francais", "sport", mettez-les dans un nouveau DataFrame
rng = np.random.default_rng(7)
notes = rng.integers(0, 21, (8, 3))
notesDF = pd.DataFrame(notes, columns=["maths", "francais", "sport"])
print(f"Tableau de notes :\n{notesDF}", end=ps)

# 3. Fusionnez les deux DataFrames (comme à l'exercice 1) et gardez le résultat dans elevesDF
elevesDF = elevesDF.join(notesDF)
print(f"Dataframe complet élèves + notes :\n{elevesDF}", end=ps)

# 4. Le contrôle de maths était trop dur : ajoutez 2 points de bonus à toute la colonne "maths",
#    en bornant le résultat entre 0 et 20
elevesDF["maths"] = (elevesDF["maths"] + 2).clip(lower=0, upper=20)
print(f"Bonus de 2 points en maths (borné entre 0 et 20) :\n{elevesDF}", end=ps)

# 5. Créez une colonne "nom complet" en fusionnant "prenom" et "nom" (deux façons)
elevesDF["nom complet"] = elevesDF["prenom"] + " " + elevesDF["nom"]
elevesDF["nom complet"] = elevesDF["prenom"].str.cat(elevesDF["nom"], sep=" ")
print(f"Ajout de la colonne nom complet :\n{elevesDF}", end=ps)

# 6. Les élèves de "Première" étaient en sortie scolaire pendant le cours de sport :
#    ajoutez-leur 3 points bonus en sport (borné à 20), sans toucher à "Terminale"
masque = elevesDF["classe"] == "Première"
elevesDF.loc[masque, "sport"] = (elevesDF.loc[masque, "sport"] + 3).clip(upper=20)
print(f"Bonus sport réservé aux élèves de Première :\n{elevesDF}", end=ps)

# 7. Erreur de saisie : remplacez toutes les villes "Saint-Étienne" par "St-Étienne"
elevesDF["ville"] = elevesDF["ville"].replace("Saint-Étienne", "St-Étienne")
print(f"Correction de la colonne ville :\n{elevesDF}", end=ps)

# 8. Calculez la moyenne générale de chaque élève sur les 3 matières (colonne "moyenne")
elevesDF["moyenne"] = elevesDF[["maths", "francais", "sport"]].mean(axis=1).round(2)
print(f"Ajout de la moyenne générale :\n{elevesDF}", end=ps)

# 9. Ajoutez une colonne "resultat" : "Admis" si moyenne >= 10, sinon "Ajourné"
elevesDF["resultat"] = np.where(elevesDF["moyenne"] >= 10, "Admis", "Ajourné")
print(f"Ajout du résultat (admis / ajourné) :\n{elevesDF}", end=ps)

# 10. Affichez uniquement les élèves "Ajourné", triés par moyenne décroissante
ajournesDF = elevesDF[elevesDF["resultat"] == "Ajourné"].sort_values(by="moyenne", ascending=False)
print(f"Élèves ajournés, triés par moyenne :\n{ajournesDF}", end=ps)

# 11. Calculez la moyenne de la classe pour chaque classe (groupby)
moyenneParClasse = elevesDF.groupby("classe")["moyenne"].mean().round(2)
print(f"Moyenne par classe :\n{moyenneParClasse}", end=ps)


#-------------------------------------------
print("-"*100, end=ps)
#-------------------------------------------
