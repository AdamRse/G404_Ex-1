import re

inp = ""


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


def exercice1():
    get_inp("Écrire une lettre : ")

    is_vovel(inp)


def exercice2():
    get_inp("Entrez une année : ")

    est_bissextile(inp)


def exercice3():
    get_inp("Entrez une phrase : ")

    count_vovel(inp)


# RUN
# -------------------------------

exercice1()
exercice2()
exercice3()
