import numpy as np
from numpy_exercices import *

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


activate_exercice = [2]
main(activate_exercice)
