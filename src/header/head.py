import sys

sys.set_int_max_str_digits(0)
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

def printError(*args, **kwargs):
    print(bcolors.FAIL, end="")
    print(*args, **kwargs)
    print(bcolors.ENDC, end="")

def printSuccess(*args, **kwargs):
    print(bcolors.OKGREEN+bcolors.BOLD, end="")
    print(*args, **kwargs)
    print(bcolors.ENDC, end="")

def printWrong(*args, **kwargs):
    print(bcolors.WARNING, end="")
    print(*args, **kwargs)
    print(bcolors.ENDC, end="")

def del_accents(texte):
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    output=""
    for lettre in texte:
        try:
            id=accent.index(lettre)
            output+=sans_accent[id]
        except ValueError:
            output+=lettre
    return output

def main(activate_exercice, context):
    for nb in activate_exercice:
        nom_fonction = f"exercice{nb}"

        # On cherche dans le contexte passé en paramètre
        if nom_fonction in context:
            context[nom_fonction]()
        else:
            print(f"⚠️ L'exercice {nb} n'existe pas.")
