print(" ---------- Tips ----------")
print("Exposant : ", 2**3)  # Exposant
print("Ou exclusif : ", True ^ True)  # Ou exclusif (seulement 1 des 2 doit être true)
print("in : ", "a" in ["a", "b", "c"])
uneListe = []
uneListe.append("coucou")
print(uneListe)
unTuple = (2, 4, "helo")  # Lecture seule
print(unTuple[1], unTuple[1:], unTuple[-1])


def ma_fonction():
    print("fonction ma_fonction")


try:
    False
except:
    True
