from src.header.head import *
from src.exercices import *


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
    inp = input("Entrez un caractère : ")
    while len(inp)>1:
        printError("Il faut un seul caractère !")
        inp = input("Entrez un caractère : ")
    infinite_triangle(inp)

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
        inp=input("Envoyez parenthèses et crochets : ")
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
        do_regex("a","a*a")

def exercice16():
    l1=[18,2,10]
    l2=[20,8, 1, 7, 8]
    sort_merge(l1, l2)

def exercice17():
    lettres=["a", "b", "c", "a", "c", "c"]
    sort_frequence(lettres)

def exercice18():
    inp = input("Écrivez une phrase : ")
    char_zip(inp)

def exercice19():
    list=[2,3,1,4,8,0]
    bubbleSort(list)

def exercice20():
    inp = input("Entrez un nombre entier : ")
    inverse_un_entier(int(inp))

def exercice21():
    inp = input("Entrez un numbre romain : ")
    nombre_romains_vers_decimal(str(inp))

def exercice22():
    inp = input("Entrez un chiffre décimal : ")
    decimal_vers_nombre_romain(int(inp))

def exercice23(tests=False):
    if tests:
        test_list1 = [4171, 3698, 3525, 3150, 3948, 4032, 3569, 3784, 3510, 3212, 3861, 3696, 3652, 3116, 4230, 3276, 3321, 3696, 3936]
        test_list2 = [247774972, 247481270, 246937264, 246039300, 246955500, 245886776, 246861669, 247411426, 248106755, 248297709,
                    244425709, 246755586, 246169628, 246567590, 248227550, 246172056, 246118294, 247550989, 245374022, 247424914,
                    246765022, 246366021, 246273920]

        print("Lancement du calcul.")
        for i in range(1, 20):
            random.seed(i)
            test = [random.randint(0, 100) for _ in range(50)]
            result = biggest_container_optimized(test, False)
            if result == test_list1[i-1]:
                printSuccess("Test "+str(i)+" passé.")
            else:
                printError("Test 1 : Mauvais résultat pour l'itération "+str(i)
                    + "\nTrouvé : "
                    + str(result)+"m²"
                    + "\nAttendu :" + str(test_list1[i-1]))
                sys.exit("Arrêt du programme")

        print("Calculs longs :")
        for i in range(20, 43):
            start_time = time.time()
            random.seed(i)
            test = [random.randint(0, 10000) for _ in range(25000)]
            result = biggest_container_optimized(test, False)
            if result == test_list2[i-20]:
                time_calcul = datetime.timedelta(seconds=(time.time() - start_time))
                printSuccess("Test "+str(i)+" passé en "+str(time_calcul))
            else:
                printError("Test 1 : Mauvais résultat pour l'itération "+str(i)
                    + "\nTrouvé : "
                    + str(result)+"m²"
                    + "\nAttendu :" + str(test_list2[i-20]))
                sys.exit("Arrêt du programme")
        print("Fini !")
    else:
        tableau=[2,1,7,9,4,2,5]
        print(tableau)
        print("Normal : "+str(biggest_container(tableau, False)))
        print("Opti : "+str(biggest_container_optimized(tableau, False)))

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
exercice13(True)
# exercice14()
# exercice15(True)
# exercice16()
# exercice17()
# exercice18()
# exercice19()
# exercice20()
# exercice21()
# exercice22()
# exercice23(True)
