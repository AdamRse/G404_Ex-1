import math
import re
from tkinter.constants import FALSE

inp = ""
inp2 = ""


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_inp(msg):
    global inp
    inp = input(msg)


def get_inp2(msg):
    global inp2
    inp2 = input(msg)


def printError(msg):
    print(bcolors.FAIL + msg + bcolors.ENDC)


def printSuccess(msg):
    print(bcolors.OKGREEN + msg + bcolors.ENDC)


def printWrong(msg):
    print(bcolors.WARNING + msg + bcolors.ENDC)


# Est une voyelle ?
# -------------------------------

# print("Est-ce qu'le la lettre est une voyelle ?")
voyelles = ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y")


def is_vovel(lettre, display=True):
    if not re.match("^[a-zA-ZéÉèÈàÀêÊ]$", lettre):
        if display:
            printError("Erreur, veuillez entrer une lettre.")
        return False
    if lettre in voyelles:
        if display:
            printSuccess(lettre + " est une voyelle")
        return True
    else:
        if display:
            printWrong(lettre + " n'est pas une voyelle")
        return False


# Une années bissextile
# -------------------------------


def est_bissextile(anneeChar):
    if not re.match("^-?[0-9]+?$", anneeChar):
        printError("ATTENTION AUX DONNÉES ! " + anneeChar + " N'EST PAS UNE ANNÉE !")
        return False

    anneeInt = int(anneeChar)
    if anneeInt % 400 == 0 or (anneeInt % 4 == 0 and anneeInt % 100 != 0):
        printSuccess(anneeChar + " est bissextile")
    else:
        printWrong(anneeChar + " n'est PAS bissextile")


# Est une voyelle
# -------------------------------


def count_vovel(txt):
    if txt == "":
        printError("La phrase envoyée est nulle")
        return False
    if len(txt) > 50:
        printError("La phrase est trop longue")
        return False

    count = 0
    for lettre in txt:
        if is_vovel(lettre, False):
            count += 1

    printSuccess("Il y a " + str(count) + " voyelle" + ("s" if count > 1 else ""))


# Multiplication range
# -------------------------------
def multiplication(number, number2):
    boxSize = 14
    if not re.match("^[0-9]+$", number):
        printError(number + " n'est pas un chiffre >:(")
        return False
    if not re.match("^[0-9]+$", number2):
        printError(number2 + " n'est pas un chiffre >:(")
        return False

    number = int(number)
    number2 = int(number2)

    if number < 0 or number > 10:
        printError(str(number) + " N'est pas entre 1 et 10 >:(")
        return False
    if number2 < 0 or number2 > 10:
        printError(str(number2) + " N'est pas entre 1 et 10 >:(")
        return False

    print("Carré de multiplication " + str(number) + " par " + str(number2))
    for first_multi in range(1, number + 1):
        output = ""
        for second_mult in range(1, number2 + 1):
            line = ""
            result = first_multi * second_mult
            line += str(first_multi) + " x " + str(second_mult) + " = " + str(result)

            for space in range(0, boxSize - len(line)):
                line += " "
            output += line + "|"

        printSuccess(output)


# Comptage de mot
# -------------------------------


def word_count(texte, display=True):
    wordCount = len(word_list(texte))
    if display:
        printSuccess(
            "Le texte contient "
            + str(wordCount)
            + " mot"
            + ("s" if wordCount > 1 else "")
        )
    return wordCount


def word_list(texte, display=True):
    text_split = re.split(r"[,\s;.)(:?+\[\]!{}=#]+", texte)
    wordList = []
    for word in text_split:
        if word != "":
            wordList.append(word)
    if display:
        printSuccess("Liste des mots : ")
        print(wordList)
    return wordList


# Mot le plus long
# -------------------------------


def longest_word(texte: str):
    wordList = word_list(texte, False)
    longestWord = ""
    for word in wordList:
        if len(word) > len(longestWord):
            longestWord = word

    printSuccess(
        "Le mot le plus long est "
        + longestWord
        + " (avec "
        + str(len(longestWord))
        + " lettres)"
    )


def longest_word_sort(texte: str):
    wordList = word_list(texte, False)
    longestWord = max(wordList, key=len)
    printSuccess(
        "Le mot le plus long est "
        + longestWord
        + " (avec "
        + str(len(longestWord))
        + " lettres)"
    )


# Supprimer les doublons
# -------------------------------


def duplicate_del_browse(liste: list, display=True):
    if not liste:
        printError("La liste données est vide.")
        return False
    if display:
        print("Liste à trier : ", liste)
    liste_triee = []

    for i in liste:
        if i not in liste_triee:
            if isinstance(i, list):
                i = duplicate_del_browse(i, False)
            liste_triee.append(i)
        elif display:
            printWrong(str(i) + " est un doublon")

    if display:
        printSuccess(
            "La liste a été triée par boucles, les doublons ont été supprimés !"
        )
        print(liste_triee)
    return liste_triee


def duplicate_del_set(liste: list, display=True):
    if not liste:
        printError("La liste données est vide.")
        return False
    if display:
        print("Liste à trier : ", liste)

    liste_triee = list(set(liste))
    if display:
        printSuccess("La liste a été triée par set, les doublons ont été supprimés !")
        print(liste_triee)
    return liste_triee


def ducplicate_del_dict(liste: list):
    return list(dict.fromkeys(liste))


# Nombre premier
# -------------------------------
def is_prime(number, display=True):

    if not re.match("^[0-9]+$", str(number)):
        printError("Attention, " + str(number) + " n'est pas un nombre.")
        return -1
    number = int(number)

    i = 2
    is_pr = True
    while i < number:
        if number % i == 0:
            is_pr = False
            break
        if i > math.sqrt(number):
            break
        i += 1

    if display:
        if is_pr:
            printSuccess(str(number) + " est un nombre premier !")
        else:
            printWrong(str(number) + " n'est pas un nombre premier")
    return is_pr


# SET EXERCICES
# -------------------------------


def exercice1():
    get_inp("Écrire une lettre : ")

    is_vovel(inp)


def exercice2():
    get_inp("Entrez une année : ")

    est_bissextile(inp)


def exercice3():
    get_inp("Entrez une phrase : ")

    count_vovel(inp)


def exercice4():
    get_inp("Entrez la HAUTEUR du carré (entre 1 et 10) : ")
    get_inp2("Entrez la LARGEUR du carré (entre 1 et 10) : ")

    multiplication(inp, inp2)


def exercice5():
    get_inp("Écrivez un texte : ")

    word_count(inp)


def exercice6():
    get_inp("Écrivez un texte : ")

    longest_word(inp)


def exercice7():
    liste = ["a", "b", "c", "b", "e", "f", "f", "f", "z", "a", "l", ["yo", "yo2", "yo"]]
    duplicate_del_browse(liste)


def exercice8():
    global inp
    get_inp("Donnez un nombre, pour calculer le prochain nombre premier supérieur : ")
    inp = int(inp)
    print("Recherche du premier nombre premier supérieur à " + str(inp))
    while not is_prime(inp, False):
        inp += 1
    printSuccess(str(inp) + " est un premier !")


# RUN
# -------------------------------

# exercice1()
# exercice2()
# exercice3()
# exercice4()
# exercice5()
# exercice6()
# exercice7()
exercice8()
