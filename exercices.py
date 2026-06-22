import datetime
import math
from operator import index
from pydoc import text
import re
import sys
import time
import random
import os
import itertools

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


def printError(msg):
    print(bcolors.FAIL + msg + bcolors.ENDC)


def printSuccess(msg):
    print(bcolors.OKGREEN + msg + bcolors.ENDC)


def printWrong(msg):
    print(bcolors.WARNING + msg + bcolors.ENDC)

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


def longest_word(texte: str | int):
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
        printSuccess("La liste a été triée par boucles, les doublons ont été supprimés !")
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


# Suite de fibonacci
# -------------------------------
def fibonacci_range(limit):
    if not re.match("^[0-9]+$", str(limit)):
        printError("Attention, " + str(limit) + " n'est pas un nombre.")

    limit = int(limit)
    suite_fi = [0, 1]

    if limit == 1:
        suite_fi.pop()

    for _ in range(limit - 2):
        current_fibo = int(suite_fi[-1]) + int(suite_fi[-2])
        suite_fi.append(current_fibo)

    printSuccess("Calcul terminé !")
    print(suite_fi)


def fibonacci_show(limit):
    if not re.match("^[0-9]+$", str(limit)):
        printError("Attention, " + str(limit) + " n'est pas un nombre.")

    limit = int(limit)
    last_fi = [0, 1]
    if limit < 10:
        sleepTime = 0.8
    elif limit < 100:
        sleepTime = 0.4
    elif limit < 1000:
        sleepTime = 0.1
    elif limit < 10000:
        sleepTime = 0.05
    else:
        sleepTime = 0.0001
    if limit > 0:
        # print("0", end=" ")
        sys.stdout.write("\rF1 : 0")
        sys.stdout.flush()
        time.sleep(sleepTime)
    if limit > 1:
        sys.stdout.write("\rF2 : 1")
        sys.stdout.flush()
        time.sleep(sleepTime)
    if limit > 2:
        for i in range(limit - 2):
            num_fibo = int(last_fi[-1]) + int(last_fi[-2])
            # print(num_fibo, end=" ")
            sys.stdout.write("\rF" + str(i + 3) + " : " + str(num_fibo))
            sys.stdout.flush()
            last_fi.append(num_fibo)
            last_fi.pop(0)
            time.sleep(sleepTime)
    printSuccess("\nCalcul terminé !")


# Triangle d'étoiles
# -------------------------------
def draw_triangle(taille, margin=1):
    if not re.match("^[0-9]+$", str(taille)):
        printError("La taille doit être un nombre entre 1 et 80. " + str(taille) + " n'est pas un nombre.")
    if not re.match("^[0-9]+$", str(margin)):
        printError("La marge doit être un nombre entre 1 et 100. " + str(margin) + " n'est pas un nombre.")
    taille = int(taille)
    margin = int(margin)
    if taille > 80 or taille <= 0:
        printError("La taille doit être un nombre entre 1 et 80. taille donnée : " + str(taille))
        return False
    if margin > 300 or margin < 0:
        printError("La marge doit être un nombre entre 0 et 300. marge donnée : " + str(margin))
        return False

    stars = 1
    for i in range(1,taille):
        stars = (i * 2) - 1
        blank_spaces = round((taille * 2) - 1 / 2) - math.trunc(stars / 2) + margin
        # print("ROUND " + str(i))
        # print("blank : " + str(blank_spaces))
        # print("stars : " + str(stars))
        while blank_spaces > 0:
            print(" ", end="")
            blank_spaces -= 1

        while stars > 0:
            print("*", end="")
            stars -= 1
        print(" ")

def draw_triangle_no_while(taille, margin=1):
    if not re.match("^[0-9]+$", str(taille)):
        printError("La taille doit être un nombre entre 1 et 80. " + str(taille) + " n'est pas un nombre.")
    if not re.match("^[0-9]+$", str(margin)):
        printError("La marge doit être un nombre entre 1 et 100. " + str(margin) + " n'est pas un nombre.")
    taille = int(taille)
    margin = int(margin)
    if taille > 80 or taille <= 0:
        printError("La taille doit être un nombre entre 1 et 80. taille donnée : " + str(taille))
        return False
    if margin > 300 or margin < 0:
        printError("La marge doit être un nombre entre 0 et 300. marge donnée : " + str(margin))
        return False

    tree=bcolors.OKGREEN
    for i in range(1,taille+1):
        tree+=("*"*(i*2-1)).center(taille*2+margin)+"\n"

    print(tree+bcolors.ENDC)

def infinite_triangle(max_width=math.trunc(os.get_terminal_size().columns/2), min_width=1):
    i=min_width
    increase=True
    colorStart=""
    colorStop=bcolors.ENDC
    colors=[bcolors.FAIL,bcolors.OKBLUE,bcolors.OKCYAN,bcolors.OKGREEN,bcolors.WARNING]
    while True:
        # max_width=math.trunc(os.get_terminal_size().columns/2) # En cas de redimentionement du terminal
        print(colorStart + ("@"*(i*2-1)).center(max_width*2) + colorStop)

        if i<=min_width:
            increase=True
            colorStart = random.choice(colors)
            rand_num=random.randint(0,10)
            if rand_num<3:
                colorStart+=bcolors.BOLD
            elif rand_num<5:
                colorStart+=bcolors.UNDERLINE
        elif i>=max_width:
            increase=False
        if increase:
            i+=1
        else:
            i-=1
        time.sleep(0.01)



# Palindrome
# -------------------------------
def is_palindrome(word, display=True):
    if len(word) < 2:
        return False
    word=str(word)
    wordList=list(word.lower())
    if wordList==wordList[::-1]:
        if display:
            printSuccess(word + " est un palindrome !")
        return True
    else:
        if display:
            printWrong(word + " n'est pas un palindrome.")
        return False

def is_palindrome_text(text):
    wordList = word_list(text, False)
    if not wordList:
        printError("Impossible de trouver un mot dans le texte donné.")
        return -1

    palindromeList=[]
    for word in wordList:
        if is_palindrome(word, False):
            palindromeList.append(word)

    nb_palindromes=len(palindromeList)
    if nb_palindromes == 0:
        printWrong("Il n'y a aucun palindrome dans la phrase.")
        return False
    else:
        printSuccess("Il y a " + str(nb_palindromes) + (" palindromes" if nb_palindromes > 1 else " palindrome") + " dans le texte !")
        printSuccess(("palindromes trouvés :" if nb_palindromes > 1 else "palindrome trouvé :"))
        print(palindromeList)

# Chiffrement César
# -------------------------------
def cesar_crypt(texte, decalage:int=3):
    texte=del_accents(texte)
    alphabetList=list("abcdefghijklmnopqrstuvwxyz")
    sizeAlphabetList=len(alphabetList)
    output=""
    for lettre in texte:
        isUpper=lettre.isupper()
        lettre=lettre.lower()
        try:
            index=alphabetList.index(lettre)
        except ValueError:
            output+=lettre
            continue
        newIndex=(index+decalage)%sizeAlphabetList
        output+=alphabetList[newIndex].upper() if isUpper else alphabetList[newIndex]
    print("Hachage : ", output)
    return output

# String détection
# -------------------------------
def string_check(string):
    stack=[]
    conforme=True
    for letter in string:
        match letter:
            case "("|"["|"{":
                stack.append(letter)
            case ")":
                if len(stack) == 0:
                    conforme=False
                    break
                if stack[-1]=="(":
                    stack.pop()
                else:
                    conforme=False
            case "]":
                if len(stack) == 0:
                    conforme=False
                    break
                if stack[-1]=="[":
                    stack.pop()
                else:
                    conforme=False
            case "}":
                if len(stack) == 0:
                    conforme=False
                    break
                if stack[-1]=="{":
                    stack.pop()
                else:
                    conforme=False

    if not len(stack) == 0:
        conforme=False

    if conforme:
        printSuccess("Le texte est conforme !")
    else:
        printWrong("Le texte n'est pas conforme.")
    return conforme

def string_check_no_switch(string):
    pile=[]
    open_close=["(",")","[","]","{","}"]
    strings_detection=['"',"'","`"]
    string_detected=False
    conforme=True
    for id, letter in enumerate(string):
        if id > 0 and string[id-1]=="\\":
            continue

        if letter in strings_detection:
            if string_detected:
                if string_detected==letter:
                    string_detected=False
            else:
                string_detected=letter
            continue
        if string_detected:
            continue

        if letter in open_close[::2]:
            pile.append(letter)
        if letter in open_close[1::2]:
            if len(pile) == 0:
                conforme=False
                break
            index_close=open_close.index(letter)
            if open_close[index_close-1]==pile[-1]:
                pile.pop()
            else:
                conforme=False
                break

    if len(pile) or string_detected:
        print("\033[91mTexte non confome.\033[0m")
        return False
    print("\033[92mTexte bien formaté !\033[0m" if conforme else "\033[91mTexte non confome.\033[0m")
    return conforme

# reverse middle
# -------------------------------
def reverse_middle(liste_reverse_middle):
    first=liste_reverse_middle[(len(liste_reverse_middle)//2):]
    second=liste_reverse_middle[:(len(liste_reverse_middle)//2)]
    first.extend(second)
    print(first)

# Expression régulière
# -------------------------------
def do_regex(string, pattern):
    index_reader=0
    is_match=True
    print("A tester : ",string, pattern)
    for id, p in enumerate(pattern):
        print("String : "+string[index_reader],"\nPattern : "+p)

        match p:
            case "*":
                previous_p=pattern[id-1]
                if previous_p == string[index_reader]:
                    while previous_p == string[index_reader]:
                        index_reader+=1
                        if len(string) >= index_reader:
                            return True

                elif previous_p == ".":
                    print("cas .* détecté !")
                    if len(pattern)-1>id:
                        next_p=pattern[id+1]
                    else:
                        print("aucun pattern après à tester, on peut renvoyer True")
                        return True
                    print("Il y a un pattern next_p:",next_p," qui détermine la fin du comptage")
                    while not next_p == string[index_reader]:
                        print("index reader :",index_reader)
                        print(string[index_reader]," n'est pas ",next_p,"on incrémente et continue.")
                        index_reader+=1
                        if len(string) >= index_reader:
                            return False

            case ".":
                index_reader+=1
            case _:
                if not p==string[index_reader]:
                    next_pattern=pattern[id+1]
                    if not next_pattern == "*":
                        is_match=False
                        break
                index_reader+=1
        print()

        if index_reader>=len(string):
            break
    ######
    if not index_reader == len(string):
        is_match=False
    print(is_match)
    return is_match

# Fusionner et trier 2 listes
# -------------------------------
def sort_merge(l1, l2):
    def get_min(lmin:list):
        minimum=False
        for n in lmin:
            if not minimum:
                minimum=n
            else:
                if minimum > n:
                    minimum=n
        return minimum
    l1.extend(l2)
    sorted=[]
    for _ in range(len(l1)):
        minL1=get_min(l1)
        sorted.append(minL1)
        l1.remove(minL1)
    printSuccess("Fusion terminée !")
    print(sorted)




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
    start_time = time.time()
    inp = int(inp)
    start_inp = inp
    print("Recherche du nombre premier >= " + bcolors.BOLD + str(inp) + bcolors.ENDC)
    while not is_prime(inp, False):
        inp += 1
    printSuccess(bcolors.BOLD + str(inp) + " est un premier !")
    nb_calculs = inp - start_inp + 1
    time_calcul = datetime.timedelta(seconds=(time.time() - start_time))

    print(
        "-- Résultat trouvé en "
        + bcolors.BOLD
        + str(time_calcul)
        + bcolors.ENDC
        + ", pour "
        + bcolors.BOLD
        + str(nb_calculs)
        + bcolors.ENDC
        + (" calculs" if nb_calculs > 1 else " calcul")
        + " --"
    )

def exercice9():
    get_inp("Combien de nombre de Fibonaccin dois-je calculer ? : ")
    fibonacci_show(inp)

def exercice10():
    # get_inp("Taille du triangle : ")
    # taille = inp
    # get_inp("Marge à gauche (optionel) : ")
    # marge = inp
    # if not marge:
    #     marge = 0
    #draw_triangle(taille, int(marge))
    #draw_triangle_no_while(taille, int(marge))
    infinite_triangle()

def exercice11():
    #get_inp("Donnez un mot : ")
    #is_palindrome(inp)
    get_inp("Écrivez une phrase : ")
    is_palindrome_text(inp)

def exercice12():
    get_inp("Écrivez une phrase : ")
    cesar_crypt(inp)

def exercice13(tests=False):
    if tests:
        printWrong("Tests :")
        strings_false=[
            "())","][","}","(]","[}","([)","{\\}","\\()","{\\[]}","(')()'",'["{}]"', # 0 à 10
            '"()[]{}{"}','``([)]',"()`\\`","'()",'"[]',"{}`","\\``()","{}`","'`(`",'"`', # 11 à 20
            "()'()`",'\\"()"',"'`'`", "`````"
        ]
        strings_true=[
            "()","[]","{}","","[\\]]","\\}{}","([])\\}","(`([]]]]`)","''()[]","``{}",'"[][["()',"(`)[]]`)",
            "''`(((((((((((`","\\`()`[[[`",'"\\")("{}', "''''''"
        ]

        i=0
        for test in strings_false:
            if string_check_no_switch(test):
                printError("Test (FALSE:"+str(i)+") échoué pour : \033[1m"+test)
                return False
            i+=1
        i=0
        for test in strings_true:
            if not string_check_no_switch(test):
                printError("Test (TRUE:"+str(i)+") échoué pour : \033[1m"+test)
                return False
            i+=1
        printSuccess("\n____________________________________\n--- Tous les tests sont passés ! ---\n____________________________________")
    else:
        get_inp("Envoyez parenthèses et crochets : ")
        string_check_no_switch(inp)

def exercice14():
    #get_inp("Envoyez parenthèses et crochets : ")
    liste_reverse_middle=["a", "b", "c", "d"]
    reverse_middle(liste_reverse_middle)

def exercice15(tests=False):
    if tests:
        test_cases = {
            "s" : ["aa", "aa", "ab", "aab", "ab", "aaa", "a", "mississippi", "bbbba", "ab", "bb", "bbab", "abbabaaaaaaacaa", "bcbabcaacacbcabac"],
            "p" : ["a", "a*", ".*", "c*a*b", ".*c", "a*a", "ab*", "mis*is*p*.", ".*a*a", ".*..c*", ".bab", "b*a*", "a*.*b.a.*c*b*a*c*", "a*c*a*b*.*aa*c*a*a*"],
            "expected_answer" : [False, True, True, True, False, True, True, False, True, True, False, False, True, True]
            }
        errors=False
        for i in range(len(test_cases["s"])):
            result=do_regex(test_cases["s"][i], test_cases["p"][i])
            if result == test_cases["expected_answer"][i]:
                printSuccess("Pattern "+test_cases["p"][i]+" (string : '"+test_cases["s"][i]+"') correct !")
            else:
                errors="Erreur sur le pattern "+test_cases["p"][i]+" (string : '"+test_cases["s"][i]+"'), renvoie "+str(result)+" au lieu de "+str(test_cases["expected_answer"][i])
                break
        if errors:
            printError(errors)
        else:
            printSuccess("Les tests sont bien passés !")
    else:
        do_regex("abc","a*b*c*d*")

def exercice16():
    l1=[18,2,10]
    l2=[20,8, 1, 7, 8]
    sort_merge(l1, l2)
# RUN
# -------------------------------

# exercice1()
# exercice2()
# exercice3()
# exercice4()
# exercice5()
# exercice6()
# exercice7()
# exercice8()
# exercice9()
# exercice10()
# exercice11()
# exercice12()
# exercice13(True)
# exercice14()
exercice15(True)
# exercice16()
