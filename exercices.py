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

# get_inp("Écrire une lettre : ")


def is_vovel(lettre):
    if not re.match("^[a-zA-ZéÉèÈàÀêÊ]$", lettre):
        printError("Erreur, veuillez entrer une lettre.")
        return False
    if lettre in voyelles:
        printSuccess(lettre + " est une voyelle")
    else:
        printWrong(lettre + " n'est pas une voyelle")


# is_vovel(inp)

# Une années bissextile
# -------------------------------


# get_inp("Écrire une année : ")


def est_bissextile(anneeChar):
    if not re.match("^-?[0-9]+?$", anneeChar):
        printError("ATTENTION AUX DONNÉES ! " + anneeChar + " N'EST PAS UNE ANNÉE !")
        return False

    anneeInt = int(anneeChar)
    if anneeInt % 400 == 0 or (anneeInt % 4 == 0 and anneeInt % 100 != 0):
        printSuccess(anneeChar + " est bissextile")
    else:
        printWrong(anneeChar + " n'est PAS bissextile")


# est_bissextile(inp)


# Une années bissextile
# -------------------------------
