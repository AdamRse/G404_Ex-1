# Exercice 2
Vous avez la table suivante :
```sql
CREATE TABLE jeux_de_societe (
    id INTEGER PRIMARY KEY,
    nom VARCHAR(80),
    editeur VARCHAR(50),
    type_jeu VARCHAR(30),
    nb_joueurs_min INTEGER,
    nb_joueurs_max INTEGER,
    duree_minutes INTEGER,
    note_moyenne DECIMAL(3,1),
    prix DECIMAL(5,2),
    annee_sortie INTEGER,
    est_cooperatif BOOLEAN
);
```
*Répondez aux questions suivantes :*

### Question 1 : Afficher le nom et le type de tous les jeux en les renommant en Jeu et Categorie respectivement.
SELECT nom AS jeu, type_jeu AS Catégorie
FROM jeux_de_societe;

### Question 2 : Afficher les 5 premiers jeux.
SELECT *
FROM jeux_de_societe
LIMIT 5;

### Question 3 : Afficher les différents types de jeux, triés par ordre alphabétique.
SELECT type_jeu
FROM jeux_de_societe
ORDER BY type_jeu ASC;

### Question 4 : Afficher les noms et notes des jeux triés de la meilleure note à la moins bonne.
SELECT nom, note_moyenne
FROM jeux_de_societe
ORDER BY note_moyenne DESC;

### Question 5 : Afficher les noms et prix des 3 jeux les moins chers.
SELECT nom, prix
FROM jeux_de_societe
ORDER BY prix ASC
LIMIT 3;

### Question 6 : Afficher les noms et durées des 5 jeux les plus longs triés par durée décroissante.
SELECT nom, duree_minute
FROM jeux_de_societe
ORDER BY duree_minute DESC
LIMIT 5;

### Question 7 : Afficher le nom et la note des jeux coopératifs.
SELECT nom, note_moyenne
FROM jeux_de_societe
WHERE est_cooperatif;


### Question 8 : Compter le nombre total de jeux dans le catalogue et l'afficher dans une colonne nommée "Nombre de jeux".
SELECT COUNT(*) AS Nombre de jeux
FROM (SELECT DISTINCT nom FROM jeux_de_societe);


### Question 9 : Calculer le nombre de jeux coopératifs et le nombre de jeux non coopératifs (renommer la colonne en "Nombre").
SELECT est_cooperatif, COUNT(*) AS 'Nombre'
FROM jeux_de_societe GROUP BY est_cooperatif;


### Question 10 : Renommer type_jeu en "Type de jeu" puis pour chaque type de jeu, afficher le nombre de jeux (renommé en "Total") et la note moyenne (renommé en "Note Moyenne"), trié par note moyenne décroissante.
SELECT type_jeu AS 'Type de jeu', COUNT(*) AS Total, AVG(note_moyenne) AS 'Note Moyenne'
FROM jeux_de_societe;


### Question 11 : Parmi les types de jeux, afficher ceux qui ont au moins 3 jeux dans le catalogue.
SELECT type_jeu
FROM jeux_de_societe
GROUP BY type_jeu
HAVING COUNT(*) >= 3;

### Question 12 : Parmi les éditeurs, afficher ceux dont la note moyenne est supérieure ou égale à 7.5.
SELECT editeur
FROM jeux_de_societe
WHERE note_moyenne >= 7.5;
> ? Pas besoin de group by + having avg() >= 7.5

### Question 13 : Parmi les éditeurs, afficher ceux dont le prix moyen dépasse 40€ (stocké dans une colonne "Prix Moyen"), trié par ordre décroissant.
SELECT editeur, prix
FROM jeux_de_societe
GROUP BY editeur
HAVING AVG(prix) > 40
ORDER BY prix DESC;


### Question 14 : Parmi les types, afficher ceux dont la note moyenne (renommé en "Moyenne") est supérieure à 7 et qui ont au moins 2 jeux (renommé en "Nombre"), trié par note moyenne décroissante.
SELECT COUNT(*) AS "Nombre", note_moyenne AS "Moyenne"
FROM jeux_de_societe
WHERE note_moyenne > 7
GROUP BY note_moyenne
HAVING COUNT(*) >= 2;


### Question 15 : Afficher les 3 types de jeux avec la plus haute note moyenne (renommé en "Moyenne"), mais uniquement ceux qui ont au moins 2 jeux (renommé en "Nombre").
SELECT type_jeu, AVG(note_moyenne) AS moyenne
FROM jeux_de_societe
GROUP BY type_jeu
HAVING COUNT(*) >= 2
ORDER BY moyenne DESC
LIMIT 3;


### Question 16 : Parmi les jeux sortis après 2015, afficher les types qui ont une note moyenne supérieure à 7.5.
SELECT DISTINCT type_jeu
FROM jeux_de_societe
WHERE annee_sortie > 2015
AND note_moyenne > 7.5;
> Note moyenne de note moyenne ?
SELECT type_jeu
FROM jeux_de_societe
WHERE annee_sortie > 2015
GROUP BY type_jeu
HAVING AVG(note_moyenne) > 7.5;

### Question 17 : Parmi les jeux qui coûtent moins de 40€, afficher les éditeurs qui ont entre 2 et 4 jeux dans le catalogue.
SELECT editeur
FROM jeux_de_societe
WHERE prix < 40
GROUP BY editeur
HAVING COUNT(nom) BETWEEN 2 AND 4;

### Question 18 : Parmi les jeux non coopératifs, afficher les types qui ont une note moyenne supérieure ou égale à 7.0, triés par note moyenne décroissante.
SELECT type_jeu, AVG(note_moyenne) AS note
FROM jeux_de_societe
WHERE est_cooperatif
GROUP BY type_jeu
HAVING AVG(note_moyenne) >= 7
ORDER BY note DESC;

### Question 19 : Parmi les jeux coopératifs ou ceux qui durent moins de 60 minutes, afficher les types de jeux qui ont une note moyenne entre 7.0 et 8.5 et qui ont au moins 2 jeux. Trier sur la moyenne et afficher les types de jeu qui ne sont pas dans le top 3.
SELECT type_jeu, AVG(note_moyenne) AS note
FROM jeux_de_societe
WHERE est_cooperatif OR duree_minutes < 60
GROUP BY type_jeu
HAVING AVG(note_moyenne) BETWEEN 7 AND 8.5
ORDER BY note
OFFSET 3;

### Question 20 : Parmi les jeux dont le prix est entre 10€ et 50€ et qui sont de type 'Stratégie' ou 'Ambiance', afficher les éditeurs qui ont soit au moins 2 jeux soit une note moyenne supérieure à 7.0. Afficher les 3 résultats avec la plus grande note moyenne après le premier.
SELECT editeur, AVG(note_moyenne) AS note
FROM jeux_de_societe
WHERE prix BETWEEN 10 AND 50
AND (type_jeu = 'Stratégie' OR type_jeu = 'Ambiance')
GROUP BY editeur
HAVING COUNT(*) >= 2 OR AVG(note_moyenne) > 7
ORDER BY note
LIMIT 3
OFFSET 1;

### Question 21 : Parmi les jeux sortis entre 2015 et 2020 et qui sont coopératifs ou coûtent plus de 30€, afficher les types qui ont au moins 2 jeux et une durée moyenne entre 30 et 90 minutes. Afficher les 2 premiers seulement, triés d'abord par nombre de jeux décroissant, puis par durée moyenne décroissante.
SELECT type_jeu, COUNT(*) AS nb_de_jeu, AVG(duree_minutes) AS duree_moyenne
FROM jeux_de_societe
WHERE annee_sortie BETWEEN 2015 AND 2020
AND (est_cooperatif OR prix > 30)
GROUP BY type_jeu
HAVING COUNT(*) >= 2 AND AVG(duree_minutes) BETWEEN 30 AND 90
ORDER BY nb_de_jeu DESC, duree_moyenne DESC
LIMIT 2;
