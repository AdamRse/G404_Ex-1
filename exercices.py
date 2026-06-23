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
    def getNextPattern(id, patternString):
        if len(patternString)-1>id:
            return patternString[id+1]
        else:
            return False
    def patternsDelimiterAfterStar(id, patternString): # A partir du pattern suivant
        # On cherche le caractère sur (sans étoile derrière, puis ensuite on teste ceux avec les étoiles)
        next_p=getNextPattern(id, patternString)
        after_next_p=getNextPattern(id+1, patternString)
        delimiters=[]
        while next_p:
            if next_p=="*":
                id+=1
            elif after_next_p=="*":
                delimiters.append(next_p)
                id+=2
            else:
                print("DELIMITER : Trouvé un pattern sans étoile ")
                delimiters.insert(0, next_p)
                break
            next_p=getNextPattern(id, patternString)
        print("DELIMITER : ", delimiters)
        return delimiters

    index_reader=0
    is_match=True
    skip_next=False
    print("---------------------\nA tester : ",string, pattern)
    for id, p in enumerate(pattern):
        if skip_next:
            skip_next=False
            continue
        print("String : "+string[index_reader],"(",index_reader,")\nPattern : "+p)

        match p:
            case "*":
                previous_p=pattern[id-1]
                if previous_p == string[index_reader]:
                    print("cas *, on va calculer le nombre de ",previous_p," dans la string")
                    while previous_p == string[index_reader]:
                        print(previous_p,"=",string[index_reader]," index_reader : ",index_reader)
                        index_reader+=1
                        if len(string) <= index_reader:
                            print("On sort de la string, index reader = ",index_reader, "et la taille de la string est : ",len(string))
                            return True
                        print("On passe l'index reader à ",index_reader,string[index_reader])
                    print("On sort du wile avec la string : ",index_reader,string[index_reader])

                elif previous_p == ".":
                    printWrong("cas .* détecté !")
                    next_p=getNextPattern(id, pattern)
                    if not next_p:
                        print("aucun pattern après à tester, on peut renvoyer True")
                        return True

                    print("Il y a un pattern next_p:",next_p," qui détermine la fin du comptage")

                    demimitersAfterStar=patternsDelimiterAfterStar(id, pattern)
                    print("Calcul du démimiteur à tester : ",demimitersAfterStar)
                    while not next_p == string[index_reader] and next_p not in demimitersAfterStar:
                        print("index reader :",index_reader)
                        print(string[index_reader]," n'est pas ",next_p,"on incrémente et continue.")
                        index_reader+=1
                        next_p=getNextPattern(id, pattern)
                        if len(string) >= index_reader:
                            return False


            case ".":
                next_p=getNextPattern(id, pattern)
                if not next_p:
                    print("Il n'y a pas de patern ensuite, le . fonctionne pour tout, on sort de la boucle")
                    break
                if next_p == "*":
                    print(".*, on le calculrera dans la boucle suivante, next, sans incrémenter index_reader")
                else:
                    index_reader+=1
            case _:
                if not p==string[index_reader]:
                    print("On compare",p," n'est pas ",string[index_reader])
                    next_p=getNextPattern(id, pattern)
                    if not next_p:
                        print("Le pattern ",p,"ne correspond pas à la string, et n'est pas annulé par une étoile, on peux renvoyer false")
                        return False
                    if not next_p == "*":
                        print("Le pattern ",p,"ne correspond pas à la string, pas d'étoile derrière. FALSE")
                        return False
                    else:
                        print("On a testé le prochain élément")
                        skip_next=True
                    print(p," est annulé par",next_p)
                index_reader+=1
        print()

        if index_reader>=len(string):
            print("Sortie de boucle : Détection index_reader >= len(string)",index_reader,len(string))
            break
    ######
    if not index_reader == len(string):
        print("index reader nest pas la longueur de la sting",index_reader,len(string))
        return False
    print(is_match)
    return is_match

## V2

def listePatterns(pattern):
    def getNextPattern(id, patternString):
        if len(patternString)-1>id:
            return patternString[id+1]
        else:
            return False
    listPatterns=[]
    for id, p in enumerate(pattern):
        next_p=getNextPattern(id, pattern)
        if next_p == "*":
            listPatterns.append(p+next_p)
        elif not p == "*":
            listPatterns.append(p)
    return listPatterns

def get_next_single_pattern(p_list, id):
    for p in p_list[id:]:
        if len(p)==1:
            return p
    return False

def test_tree(dictTree, pattern_starless, string, index_reader):
    pass

def test_all_scenarios_until_simple_pattern(p_list, id, string, index_reader): # On doit tester tous les scénarios jusqu'au prochain simple pattern
    max_id=len(p_list)-1
    delimiter_p=False
    star_letters_only=[]
    for p in p_list[id:]:
        if len(p)==2:
            star_letters_only.append(p[0])
        elif len(p)==1:
            delimiter_p=p
            break

    nb_occurence_delimiter_in_str=0
    if delimiter_p:
        for s_id, s in enumerate(string[index_reader:]):
            if s == delimiter_p:
                nb_occurence_delimiter_in_str+=1

    sub_reader=index_reader
    if nb_occurence_delimiter_in_str==0: # Aucun démiliteur dans la string, il ne reste que des n* dans la string
        for s in string[index_reader:]:
            if s not in star_letters_only:
                return False
        return len(string)-1
    elif nb_occurence_delimiter_in_str==1:# La string possède une unique occurence du délimiteur, on peur extraire le pattern à tester
        for s in string[index_reader:]:
            if s == delimiter_p:
                return sub_reader+1
            if s not in star_letters_only:
                sub_reader+=1
                return False
        return sub_reader
    else:# Plusieurs délimiteur, il faut tester pour caque occurence

        pass


    # sub_reader=index_reader
    # for s_id, s in enumerate(string[index_reader:]):
    #     for p_id, p in enumerate(p_list):
    #         max_occurence=0
    #         while p == s:
    #             max_occurence+=1

    #     sub_reader+=1

    return index_reader

def analyseSimplePattern(p, s):
    return p==s or p == "."

def test_only_stars_remaining(p_list, id):
    for p in p_list:
        if len(p)==1:
            return False
    return True

def do_regex2(string, pattern):
    p_list=listePatterns(pattern)
    max_index_reader=len(string)-1
    index_reader=0
    skip_double_pattern=False
    for id, p in enumerate(p_list):
        if skip_double_pattern:
            if len(p)==1:
                skip_double_pattern=False
            else:
                continue
        if index_reader >= max_index_reader:
            return test_only_stars_remaining(p_list, id)


        if len(p) == 1:
            if analyseSimplePattern(p, string[index_reader]):
                index_reader+=1
            else:
                return False
        else: # On doit tester tous les scénarios jusqu'au prochain simple pattern
            new_index=test_all_scenarios_until_simple_pattern(p_list, id, string, index_reader)
            if new_index:
                index_reader=new_index
                skip_double_pattern=True
            else:
                return False


    print(p_list)
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
