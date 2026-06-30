import numpy as np
from numpy_exercices import * # NOQA
from head import printSuccess, printError, printWrong, bcolors # NOQA

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

    reshaped=np.column_stack((eval1,eval2,eval3,eval4))
    print(f"Matrice 25x4 : {reshaped}")
    print(f"Dimension de la matrice : {reshaped.shape}")
    print(f"Moyenne générale : {reshaped.mean()}\nÉcart type : {reshaped.std()}\nNote minimale : {reshaped.min()}\nNote maximale : {reshaped.max()}")
    print(f"Moyenne par évaluations : {reshaped.mean(axis=0)}\nMédianes : {np.median(reshaped, axis=0)}\nMinimales : {np.min(reshaped, axis=0)}\nMaximale : {np.max(reshaped, axis=0)}")
    print(f"Moyenne par élèves : {reshaped.mean(axis=1)}")
    print(f"Nombre d'élèves ayant la moyenne : {np.sum(reshaped.mean(axis=1) >= 10)}")
    print(f"Indice des 3 meilleurs élèves : {np.argsort(reshaped.mean(axis=1), axis=None)[-3:]}")
    print((reshaped >= 15))
    print(f"Élève >=15 à la 3ème évaluation : {np.where(reshaped[:,2] >= 15)[0]+1}")
    # 8. Quels apprenants ont eu >= 15 à l'évaluation 3 ?
    # 9. Créer un masque pour les apprenants ayant TOUTES les notes >= 8
    # 10. Bonus de 2 points sur les notes inférieures a 8 uniquement
    # 11. Bonus de 5 points sur l'évaluation 1 (plafonné à 20)
    # 12. Appliquer la normalisation Min-Max sur les notes de l'évaluation 1
    # 13. Standardiser les notes de l'évaluation 2
    # 14. Afficher un array de la meilleure note dans chaque matiere entre les 10 meilleurs eleves de la classe
    #
    # axis 0=vertical
    # axis 1=horizontal

#  MAIN --------------
activate_exercice = [5]
main(activate_exercice)
