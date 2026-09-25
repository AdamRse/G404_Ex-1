# Concevoir un projet Python : mélange de deux gaussiennes

Le [diaporama](../../slides/2026-09-25_python_architecture_et_sql.pptx),
partie I, donne les exigences. Reprenez l'organisation du projet Rectangle :
un paquet local, un lanceur et des tests. Vous choisissez les noms et écrivez
votre code. Les [trois scripts d'aide](snippets/README.md)
illustrent des opérations à reprendre et à adapter.

## Les six exigences

1. **Simuler deux groupes.** A : moyenne 100, écart-type 18, proportion 60 %.
   B : moyenne 106, écart-type 24, proportion 40 %. Produire 2 000 observations
   avec la graine aléatoire (`seed`) 404. Ces paramètres sont modifiables
   dans le script de lancement.
2. **Produire un dataframe.** Une observation par ligne, une colonne numérique
   `value` et une colonne `component` indiquant A ou B. Le cas initial contient
   1 200 A et 800 B. Chaque observation vient d'un groupe ; les tirages ne
   s'additionnent pas.
3. **Utiliser une classe.** Chaque objet garde ses paramètres et son dernier
   dataframe. Ses méthodes produisent et renvoient ce dataframe, puis préparent
   et renvoient les figures. Des fonctions séparées tirent les valeurs et les
   assemblent dans le dataframe ; le module de la classe les importe et ses
   méthodes les utilisent.
4. **Reprendre l'organisation de Rectangle.** Un paquet local est un dossier
   contenant `__init__.py`. Ce fichier définit une constante pour la graine par
   défaut, utilisée par la classe et le lanceur. Placez la classe et les fonctions
   dans deux modules distincts de ce paquet. À l'intérieur du paquet, utilisez
   des imports relatifs, qui désignent les modules du même paquet.
   Un script de lancement importe la classe, choisit les paramètres, crée les
   objets, lance le calcul et affiche les résultats. Les fichiers du dossier
   `tests/` importent cette même classe. Importer le paquet et ses modules ne
   lance aucune simulation ni aucun affichage. Les noms des fichiers, fonctions
   et classes sont libres.
5. **Produire trois graphiques du premier objet depuis le même dataframe.** Deux histogrammes
   superposés pour comparer A et B, un histogramme du mélange sans distinguer
   les groupes, puis des boîtes à moustaches pour A, B et leur mélange
   (A∪B : toutes les observations), afin de comparer médianes et dispersion.
   Les histogrammes représentent des densités ; les axes et les groupes sont nommés.
6. **Reproduire un résultat et garder deux objets indépendants.** Les mêmes
   paramètres et la même graine redonnent les mêmes valeurs dans votre environnement.
   Le second objet utilise 30 % de A et un écart-type de 30 pour B, les autres
   paramètres restant identiques : 600 A et 1 400 B. Le premier objet conserve
   ses propres paramètres et données. Des tests vérifient les valeurs et
   effectifs, la reproductibilité, l'indépendance des objets et la réutilisation
   du dataframe par les figures.

## Ce que vous présentez

Un dossier de projet avec vos fichiers Python, la liste des bibliothèques à installer
et un court README donnant les commandes de lancement et de test ainsi que le
rôle des fichiers. Le projet démarre depuis le terminal. Montrez les effectifs
des deux objets, les trois figures du premier et les tests réussis ; expliquez
le parcours des données et les imports.

Pour préparer Python, suivez [les instructions du kit](../README.md).
