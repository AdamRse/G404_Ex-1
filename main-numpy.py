import numpy as np
from numpy.ma.extras import column_stack
from src.header.head import printSuccess, printError, printWrong, bcolors # NOQA

# Cours : https://github.com/G404-Data-Analyst/Formation_Data_Analyst/blob/main/numpy_et_pandas_cours.ipynb

def main(activate_exercice):
    for nb in activate_exercice:
        nom_fonction = f"exercice{nb}"
        if nom_fonction in globals():
            globals()[nom_fonction]()
        else:
            print(f"⚠️ L'exercice {nb} n'existe pas.")


def exercice1():
    nombres = np.arange(5, 30, 5)
    print(f"Array de 5 : {nombres}")
    print(f"Forme : {nombres.shape}, Dimensions : {nombres.ndim}, Type : {nombres.dtype}")
    print(f"Array de 0 à 20 exclu {np.arange(0, 20)}")
    print(f"Vecteur de 10 zéros : {np.zeros(10)}")
    print(f"Matrix 3x4 avec des 1 :\n{np.ones((3,4))}\nou\n{np.ones(12).reshape(3, 4)}")
    print(f"Vecteur de 7 points équidistants de 0 à 1 :\n{np.linspace(0, 1, 7)}")
    print(f"Tableau 5x5 avec nombres aléatoires entre 1 et 100 :\n{np.random.default_rng().integers(1, 101, (5, 5))}")

# Indexation et Slicing
def exercice2():
    rng = np.random.default_rng(42)
    notes = rng.integers(0, 21, 30)  # 30 notes entre 0 et 20
    print("Notes :", notes)
    # ------------------
    print(f"Note de l'étudiant n°5 : {notes[4]}")
    print(f"Note des 5 premiers étudiants : {notes[:5]}")
    print(f"Note des 10 derniers étudiants : {notes[-10:]}")
    print(f"Note ayant la moyenne : {notes[notes >= 10]}")
    print(f"Note ayant 15 ou + : {notes[notes >= 15]}")
    print(f"Note entre 8 et 12 : {notes[(notes >= 8) & (notes <= 12)]}")
    print(f"Nombre d'étudiants en échec (<10) : {notes[notes < 10].size}")

# Opérations et ufuncs
def exercice3():
    rng = np.random.default_rng(42)
    notes = rng.normal(12, 3, 20).round(1)  # 20 notes, moyenne 12, écart 3
    orininal=notes
    print("Notes de la promo :", notes, "\n----")
    # ------------------
    print(f"Moyenne : {notes.sum() / notes.size}\n----") # ou np.mean()

    notes=np.clip(np.add(notes, 0.5), 0, 20)
    print(f"0.5 bonus à chacun : {notes}\n----") # ou  notes=np.clip(notes + 0.5, 0, 20)

    notes=np.clip(notes * 1.1, 0, 20)
    print(f"Majoration : {notes}\n----")

    printSuccess(f"Écart bonus : {np.clip(notes - orininal, 0, 20)}")

# Stats et agrégations
def exercice4():
    rng = np.random.default_rng(42)
    notes = rng.integers(0, 21, (8, 5))
    matieres = ["Mathematiques", "Francais", "Physique", "Histoire-Geog.", "EPS"]

    print("=== RELEVÉ DE NOTES ===")
    print("Étudiant |", " ".join(f"{m:8s}" for m in matieres))
    for i in range(8):
        print(f"  {i+1:3d}    |", " ".join(f"{n:9d}" for n in notes[i]))
    print("---")
    print(f"Moyenne générale : {np.mean(notes)}", "\n---")
    print(f"Écart type : {np.std(notes)}", "\n---")
    print(f"Note minimale : {np.min(notes)} et maximale : {np.max(notes)}", "\n---")
    print("Moyennes par matières :")
    for id, m in enumerate(np.mean(notes, axis=0)):
        print(f"{matieres[id]:>25} : {m:>6}")
    print("---")
    print(f"L'élève {np.argmax(np.mean(notes, axis=1))+1} a la meilleure moyenne", "\n---")
    print("Meilleure matière : ", matieres[np.argmax(np.mean(notes, axis=0))], "\n---")
    print(f"Étudiants avec la moyennes : {np.sum(np.mean(notes, axis=1) >= 10)}", "\n---")
    print(f"3 meilleures notes : {np.sort(notes.ravel())[-3:]}", "\n---") # Ou np.sort(notes, axis=None)

def exercice5():
    rng = np.random.default_rng(75)
    eval1 = rng.normal(11, 4, 25).round(1).clip(0, 20)
    eval2 = rng.normal(12, 3, 25).round(1).clip(0, 20)
    eval3 = rng.normal(13, 5, 25).round(1).clip(0, 20)
    eval4 = rng.normal(10, 4, 25).round(1).clip(0, 20)

    print(eval1)
    print(eval2)
    print(eval3)
    print(eval4)

    separateur="\n"+('-'*50)+"\n\n"

    notes=np.column_stack((eval1,eval2,eval3,eval4))
    print(f"Matrice 25x4 :\n{notes}", end=separateur)
    print(f"Dimension de la matrice : {notes.shape}", end=separateur)
    print(f"Moyenne générale : {notes.mean()}\nÉcart type : {notes.std()}\nNote minimale : {notes.min()}\nNote maximale : {notes.max()}", end=separateur)
    print(f"Moyenne par évaluations : {notes.mean(axis=0)}\nMédianes : {np.median(notes, axis=0)}\nMinimales : {np.min(notes, axis=0)}\nMaximale : {np.max(notes, axis=0)}", end=separateur)
    print(f"Moyenne par élèves : {notes.mean(axis=1)}", end=separateur)
    print(f"Nombre d'élèves ayant la moyenne : {np.sum(notes.mean(axis=1) >= 10)}", end=separateur)
    print(f"Indice des 3 meilleurs élèves : {np.argsort(notes.mean(axis=1))[-3:]} avec sort(), ou {np.argpartition(notes.mean(axis=1),-3)[-3:]} avec partition()", end=separateur) # Plus rapide avec argpartition() : La position sélectionnée (-3) contient le même chiffre et son argument qu'avec sort. A gauche tous les chiffre sont <=, et droite ils sont >=. L'ordre à gauche et à droite est indéfini
    print(f"Élève >=15 à la 3ème évaluation : {np.where(notes[:,2] >= 15)[0]+1}", end=separateur) # Where est une exeption en renvoie l'indice
    print(f"Élèves n'ayant pas de notes < 8 : {np.where(np.all(notes >= 8, axis=1))[0]}", end=separateur)

    notes=np.where(notes < 8, notes+2, notes) # Ou : notes[notes < 8] += 2
    print(f"+2 points pour les notes < 8 :\n{notes}", end=separateur)

    notes[:,0]=notes[:,0]+5
    notes=notes.clip(0,20)
    print(f"+5 points sur l'évaluation 1 :\n{notes}", end=separateur)

    notesFinales=notes.copy()
    notes[:,0]=(notes[:,0] - notes[:,0].min()) / (notes[:,0].max() - notes[:,0].min())
    print(f"Normalisation de l'éval 1 :\n{notes}", end=separateur) # Xnorm = ( X - Xmin) / (Xmax - Xmin)

    moyenne2=np.mean(notes[:,1])
    ecartType2=np.std(notes[:,1])
    print(f"Moyenne colonne 2 : {moyenne2}\nécard type colonne 2 : {ecartType2}")
    notes[:,1]=((notes[:,1] - moyenne2) / ecartType2)
    print(f"Standadisation de l'éval 2 :\n{notes}", end=separateur) # Xstd = (X - moyenne) / écart type

    argtop10=np.argpartition(notesFinales.mean(axis=1), -10)[-10:]
    print(f"Arguments du top 10 :\n{argtop10}")
    notesTop10=notesFinales[argtop10,:]
    print(f"Notes du top 10 :\n{notesTop10}")
    bestNoteTop10=notesTop10.max(axis=1)
    print(f"Meilleures notes du top 10 :\n{bestNoteTop10}")

    # axis 0=vertical
    # axis 1=horizontal

def exercice6():
    rng = np.random.default_rng(42)

    # Données de base : 7 jours de la semaine, 3 produits (A, B, C)
    produits = ["Produit A", "Produit B", "Produit C"]
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    # 1. Matrice des quantités vendues (7 jours x 3 produits) entre 0 et 15 unités
    ventes = rng.integers(0, 16, (7, 3))
    print("=== QUANTITÉS VENDUES ===")
    print(ventes)
    print("-" * 50)

    # 2. Vecteur des prix unitaires pour chaque produit (A: 10€, B: 25€, C: 50€)
    prix = np.array([10, 25, 50])

    # ---- À TOI DE COMPLÉTER LES OPÉRATIONS SUIVANTES ----

    # A. Calculer le chiffre d'affaires (CA) quotidien de chaque jour (7 jours)
    # INDICE : Multiplier les ventes par les prix (Produit matriciel ou somme pondérée)
    ca_quotidien = ventes @ prix  # Ou np.dot(ventes, prix)
    print(f"Chiffre d'affaires par jour :\n{dict(zip(jours, ca_quotidien))}")
    print("-" * 50)

    # B. Calculer le Chiffre d'Affaires cumulé tout au long de la semaine (Évolution)
    # FONCTION À UTILISER : np.cumsum()
    ca_cumule = np.cumsum(ca_quotidien)
    print(f"Évolution du CA cumulé : {ca_cumule}")
    print("-" * 50)

    # C. Trouver le jour où le Chiffre d'Affaires a été le plus élevé
    meilleur_jour_idx = np.argmax(ca_quotidien)
    print(f"Le meilleur jour de la semaine est le {jours[meilleur_jour_idx]} avec {ca_quotidien[meilleur_jour_idx]}€")
    print("-" * 50)

    # D. Identifier s'il y a eu des jours de "rupture" pour AU MOINS un produit (0 vente)
    # FONCTIONS À UTILISER : np.any() sur l'axe horizontal
    jours_rupture_masque = np.any(ventes == 0, axis=1)
    indices_jours_rupture = np.where(jours_rupture_masque)[0]
    jours_rupture = [jours[i] for i in indices_jours_rupture]
    print(f"Jours avec au moins une rupture de stock (0 vente) : {jours_rupture}")
    print("-" * 50)

    # E. Restructuration et Ajout de données (Concaténation)
    # Imaginons les ventes d'un 8ème jour (Nouvelle journée de ventes pour les 3 produits)
    ventes_jour8 = np.array([12, 5, 9])
    # FONCTION À UTILISER : np.vstack() pour ajouter une ligne à la matrice existante
    ventes_totale = np.vstack((ventes, ventes_jour8))
    print(f"Nouvelle forme de la matrice après ajout du Jour 8 : {ventes_totale.shape}")

    print("TEST",[x for x in range(10)])

#  MAIN --------------
activate_exercice = [6]
main(activate_exercice)
