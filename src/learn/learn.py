import string

print(" ---------- Tips ----------")
print("Exposant : ", 2**3)  # Exposant
print("Tronquer une division : ",5//2)
print("Ou exclusif : ", True ^ True)  # Ou exclusif (seulement 1 des 2 doit être true)
print("in : ", "a" in ["a", "b", "c"])
uneListe = []
uneListe.append("coucou")
print(uneListe)
unTuple = (2, 4, "helo", "HELLO")  # Lecture seule
print("Tuple ranges : ", unTuple[1], unTuple[1:], unTuple[-1])
print("Range -1 : ", range(-1))


def ma_fonction(a: str = "1"):
    print("fonction ma_fonction, avec le paramètre " + a)


print(string.punctuation)


def diviser_nombres(a, b):
    try:
        resultat = a / b
        print(f"Le résultat de {a} / {b} est {resultat}")
    except ZeroDivisionError:
        # 2. Le premier EXCEPT : S'exécute UNIQUEMENT si on tente de diviser par zéro
        print("Erreur : Il est impossible de diviser par zéro !")

    except TypeError:
        # 3. Le second EXCEPT : S'exécute si on donne des lettres au lieu de chiffres
        print("Erreur : Veuillez utiliser uniquement des nombres.")

    finally:
        # 4. Le bloc FINALLY (optionnel) : S'exécute TOUJOURS à la fin, qu'il y ait eu une erreur ou non
        print("--- Fin de la tentative ---\n")

import itertools
for i, j in itertools.zip_longest(range(5), range(10)):
    print(i, j)
