from logging import lastResort

from head import *
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
from collections import Counter

sys.set_int_max_str_digits(0)



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
    pass

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

# Trier par fréquence d'apparition
# -------------------------------
def sort_frequence(lettres):
    #cnt = Counter(lettres)
    cnt={}
    for lettre in lettres:
        if lettre not in cnt.keys():
            cnt[lettre]=1
        else:
            cnt.update({lettre: (cnt[lettre]+1)})

    cnt={k: v for k, v in sorted(cnt.items(), key=lambda item: item[1])}
    print(cnt)
    return cnt

# Compression des caractères
# -------------------------------
def char_zip(text:str):
    last_char=False
    compressed_txt=""
    print("texte reçu : ", text)
    count=1
    for c, nc in itertools.zip_longest(text, text[1:]):
        if c == nc:
            count+=1
        else:
            compressed_txt+=c+str(count) if count > 1 else c
            count=1
    print(compressed_txt)

# Bubble sort
# -------------------------------
def bubbleSort(list:list, display=True):
    if display:
        printWrong("Liste données : "+str(list)+' ('+str(len(list))+')')
    decalage=0
    for id_n1, n1 in enumerate(list):
        minimum=[id_n1,n1]
        for id_n2, n2 in enumerate(list[id_n1:]):
            if minimum[1] > n2:
                minimum=[decalage+id_n2,n2]
        list.pop(minimum[0])
        list.insert(id_n1,minimum[1])
        decalage+=1
    printSuccess("Liste triée !\n"+str(list)+' ('+str(len(list))+')')

# Inverser un entier
# -------------------------------
def inverse_un_entier(nombre:int):
    if type(nombre) is not int: return False

    nombre_string = str(nombre)
    reverse_nombre = nombre_string[::-1]
    if reverse_nombre[-1] == '-':
        reverse_nombre = '-'+reverse_nombre[:-1]

    return int(reverse_nombre)

# Traduction chiffres romains
# -------------------------------
def nombre_romains_vers_decimal(nombre_r:str, display=True) -> int:
    nombre_r = nombre_r.upper()
    dict_unitaire={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    # calcul des patterns d'addition
    def get_patterns(chiffre:str) -> list:
        patterns=[]
        line=""
        for n, n2 in itertools.zip_longest(chiffre, chiffre[1:]):
            if not n2:
                patterns.append(line+n)
                break
            if dict_unitaire[n] >= dict_unitaire[n2]:
                patterns.append(line+n)
                line=""
            else:
                line+=n
        return patterns

    # fiare la somme des chiffres
    def val_pattern(liste_pattern: list) -> int:
        somme = 0
        for lettre in liste_pattern:
            tmp_somme = 0
            if len(lettre) > 1: ## Pour les lettre plus petit I et V
                tmp_nombre = dict_unitaire[lettre[0]]
                for char in lettre:
                    if tmp_nombre < dict_unitaire[char]:
                        tmp_somme =  dict_unitaire[char] - tmp_nombre
                    else:
                        tmp_somme =  dict_unitaire[char] + tmp_nombre
                somme += tmp_somme
            else:
                somme += dict_unitaire[lettre]
        return somme


    liste_pattern = get_patterns(nombre_r)
    result = val_pattern(liste_pattern)
    if display:
        printSuccess(nombre_r+" > "+str(result))
    return result

def decimal_vers_nombre_romain(nombre_r:int, display=True) -> str|bool:
    dict_unitaire={1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"DM", 1000:"M"}
    dict_read=dict(dict_unitaire)
    find=99
    num_rom=""
    if nombre_r > 3999:
        return False
    while find > 0:
        biggest_divisor=max(dict_read)
        biggest_rom=find // biggest_divisor
        rest_rom=find % biggest_divisor
        while biggest_rom > 0:
            num_rom+=dict_read[biggest_divisor]
            biggest_rom-=1
        del dict_read[biggest_divisor]
        find=rest_rom
    if display:
        print(num_rom)
    return num_rom
