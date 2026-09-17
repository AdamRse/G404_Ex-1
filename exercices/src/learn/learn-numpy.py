import numpy as np

print((np.__version__))

print("--- 1. CRÉATION AUTOMATIQUE D'ARRAYS ---")

# np.arange(début, fin, pas) -> comme la fonction range() de Python, mais crée un array
# Générer les nombres de 0 à 9 (le 10 est exclu)
suite_nombres = np.arange(10)
print("Suite de 0 à 9 :", suite_nombres)

# Générer les nombres de 5 à 20, de 2 en 2
nombres_impairs = np.arange(5, 20, 2)
print("De 5 à 20 de deux en deux :", nombres_impairs)

# np.linspace(début, fin, nombre_d_elements) -> très utile en stat/graphique
# Générer 5 valeurs également réparties entre 0 et 100
paliers = np.linspace(0, 100, 5)
print("5 paliers de 0 à 100 :", paliers)
print("\n")


print("--- 2. OPÉRATIONS MATHÉMATIQUES SIMPLES (VECTORISATION) ---")

# Création d'un array de base
prix_hors_taxe = np.array([10, 20, 50, 100])
print("Prix de départ (HT) :", prix_hors_taxe)

# Multiplier toutes les valeurs par 2 (ton exemple)
prix_doubles = prix_hors_taxe * 2
print("Prix doublés :", prix_doubles)

# Ajouter une valeur fixe (ex: 5€ de frais de port sur chaque produit)
prix_avec_frais = prix_hors_taxe + 5
print("Prix + 5€ de frais :", prix_avec_frais)

# Calculer la TVA (20%) d'un seul coup
prix_ttc = prix_hors_taxe * 1.20
print("Prix finaux (TTC) :", prix_ttc)
print("\n")


print("--- 3. SÉLECTIONNER DES MORCEAUX D'ARRAY (SLICING) ---")

notes = np.array([12, 15, 8, 19, 14, 11])
print("Notes des étudiants :", notes)

# Prendre les 3 premiers éléments
premiers = notes[:3]
print("Les 3 premières notes :", premiers)

# Prendre les éléments du deuxième (index 1) au quatrième (index 3)
milieu = notes[1:4]
print("Notes de l'index 1 à 3 :", milieu)

# Inverser l'ordre de l'array (astuce Python/NumPy classique)
notes_inversees = notes[::-1]
print("Notes à l'envers :", notes_inversees)
print("\n")


print("--- 4. CHANGER LA FORME D'UN ARRAY (RESHAPE) ---")

# On part d'une liste plate de 1 à 6
liste_plate = np.arange(1, 7)
print("Liste plate (1D) :", liste_plate)

# On la transforme en matrice de 2 lignes et 3 colonnes
# Attention : le produit des dimensions (2x3) doit être égal au nombre d'éléments (6)
matrice = liste_plate.reshape(2, 3)
print("Même liste transformée en matrice (2D) :\n", matrice)

# ----------------------------------------------------------------------------------------

# Configuration pour un affichage plus lisible des nombres à virgule
np.set_printoptions(precision=2, suppress=True)

print("--- 1. CRÉATION ET INSPECTION DES DONNÉES ---")

# Chaque ligne = un magasin (Magasin A, B, C)
# Chaque colonne = un trimestre (T1, T2, T3, T4)
donnees_ventes = np.array([
    [120.5, 135.0, 110.2, 150.8],  # Magasin A
    [95.0,  115.3, 105.0, 130.2],  # Magasin B
    [150.0, 160.5, 145.8, 190.0]   # Magasin C
])

# Inspecter la structure du tableau (Crucial en Data Analysis)
print(f"Forme du tableau (lignes, colonnes) : {donnees_ventes.shape}")
print(f"Type de données : {donnees_ventes.dtype}")
print(f"Nombre total d'éléments : {donnees_ventes.size}\n")


print("--- 2. INDEXATION ET SLICING (SÉLECTION DE DONNÉES) ---")

# Obtenir une valeur précise : Ventes du Magasin A (ligne 0) au T3 (colonne 2)
ventes_A_T3 = donnees_ventes[0, 2]
print(f"Ventes du Magasin A au T3 : {ventes_A_T3} k€")

# Sélectionner TOUTES les ventes du Magasin C (ligne 2, toutes les colonnes)
ventes_magasin_C = donnees_ventes[2, :]
print(f"Ventes annuelles du Magasin C : {ventes_magasin_C}")

# Sélectionner les ventes de TOUS les magasins pour le T1 (toutes les lignes, colonne 0)
ventes_T1 = donnees_ventes[:, 0]
print(f"Ventes du réseau au T1 : {ventes_T1}\n")


print("--- 3. FILTRAGE ET MASQUES BOOLEANS ---")

# On veut identifier les trimestres où un magasin a dépassé les 140 k€
Objectif_atteint = donnees_ventes > 140.0
print("Masque booléen (Vrai si > 140) :\n", Objectif_atteint)

# Extraire uniquement ces valeurs supérieures à 140
performances_top = donnees_ventes[donnees_ventes > 140.0]
print(f"Liste des chiffres d'affaires > 140 k€ : {performances_top}\n")


print("--- 4. CALCULS STATISTIQUES ET AGRÉGATIONS (Le cœur du métier) ---")

# Calcul global sur tout le réseau
print(f"Chiffre d'affaires total de l'entreprise : {np.sum(donnees_ventes)} k€")
print(f"Vente moyenne par trimestre/magasin : {np.mean(donnees_ventes):.2f} k€")

# /!\ ASTUCE ESSENTIELLE : Le concept d'axe (axis) /!\
# axis=0 -> Calcul vertical (par colonne / par trimestre)
# axis=1 -> Calcul horizontal (par ligne / par magasin)

moyennes_par_trimestre = np.mean(donnees_ventes, axis=0)
print(f"Performance moyenne du réseau par trimestre (T1 à T4) : {moyennes_par_trimestre}")

ventes_totales_par_magasin = np.sum(donnees_ventes, axis=1)
print(f"CA annuel total par magasin (A, B, C) : {ventes_totales_par_magasin}\n")


print("--- 5. NETTOYAGE ET MANIPULATION DES DONNÉES ---")

# Simulation d'une valeur manquante (NaN : Not a Number), classique en data
donnees_incompletes = np.array([10.5, np.nan, 15.2, 12.0])
print(f"Tableau avec données manquantes : {donnees_incompletes}")

# Les fonctions standards échouent avec des NaN (le résultat sera NaN)
print(f"Moyenne standard (échoue) : {np.mean(donnees_incompletes)}")

# Solution NumPy : Utiliser les fonctions "nan..." qui ignorent le problème
moyenne_propre = np.nanmean(donnees_incompletes)
print(f"Moyenne corrigée (ignore le NaN) : {moyenne_propre:.2f}")

# Remplacer le NaN par 0 pour nettoyer le dataset
donnees_nettoyees = np.isnan(donnees_incompletes)
donnees_incompletes[donnees_nettoyees] = 0.0
print(f"Tableau nettoyé (NaN remplacé par 0) : {donnees_incompletes}")
