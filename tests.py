def fonction_a_tester(test):  # Remplacer la fonction à tester ici
    # Votre fonction
    return True

def tests():
    print("\033[93mTests :\033[0m")
    strings_false=[
        "())","][","}","(]","[}","([)","{\\}","\\()","{\\[]}","(')()'",'["{}]"', # 0 à 10
        '"()[]{}{"}','``([)]',"()`\\`","'()",'"[]',"{}`","\\``()","{}`","'`(`",'"`', # 11 à 20
        "()'()`",'\\"()"',"'`'`"
    ]
    strings_true=[
        "()","[]","{}","","[\\]]","\\}{}","([])\\}","(`([]]]]`)","''()[]","``{}",'"[][["()',"(`)[]]`)", # 0 à 10
        "''`(((((((((((`","\\`()`[[[`",'"\\")("{}'
    ]

    i=0
    for test in strings_false:
        if fonction_a_tester(test): # Remplacer la fonction à tester ici
            print("\033[91mTest (FALSE:"+str(i)+") échoué pour : \033[1m"+test+"\033[0m")
            return False
        i+=1
    i=0
    for test in strings_true:
        if not fonction_a_tester(test): # Remplacer la fonction à tester ici
            print("\033[91mTest (TRUE:"+str(i)+") échoué pour : \033[1m"+test+"\033[0m")
            return False
        i+=1
    print("\033[96m\n____________________________________\n--- Tous les tests sont passés ! ---\n____________________________________")

# %%

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

# string_check_no_switch("()")

# %%

def calcul_mediane(liste:list):
    liste.sort()
    size=len(liste)
    median=False
    if size %2 == 0:
        first=liste[(size//2)-1]
        second=liste[(size//2)]
        median=(first+second)/2
    else:
        median=liste[(size//2)-1]
    print(median)
calcul_mediane([1,9,2,88,8,7,40,21,22,101])
