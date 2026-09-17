
### Requete 1 :
`
SELECT 
    nom, 
    prix
FROM jeux_de_societe
WHERE prix < 30
ORDER BY prix ASC;
`
- Afficher, du moins cher au plus cher, le nom et le prix des jeux qui coûtent moins de 30€

### Requete 2 :
`
SELECT
    type_jeu,
    COUNT(*) AS total
FROM jeux_de_societe
GROUP BY type_jeu
HAVING COUNT(*) >= 3;
`
- Pour chaque type de jeu, afficher le type de jeu et le nombre de jeux (dans une colonne total), pour chaque type de jeu ayant 3 jeux ou plus.

### Requete 3 : 
`
SELECT
    editeur,
    AVG(prix) AS prix_moyen
FROM jeux_de_societe
WHERE annee_sortie >= 2015
GROUP BY editeur
ORDER BY prix_moyen DESC
LIMIT 5;
`
- Pour chaque éditeur, afficher le prix moyen et l'éditeur, les 5 jeux le plus chers du plus cher au moins cher. Seulement les jeux sortis après 2015
### Requete 4 : 
`
SELECT
    type_jeu,
    AVG(duree_minutes) AS duree_moyenne,
    COUNT(*) AS nombre
FROM jeux_de_societe
WHERE est_cooperatif
GROUP BY type_jeu
HAVING AVG(duree_minutes) > 60
ORDER BY duree_moyenne DESC;
`
- Pour chaque type de jeu, afficher le type de jeu, la durée moyenne, et le nombre de jeux, qui sont coopératifs. Afficher du plus long au moins long, et n'afficher que les type de jeux dont la durée moyenne est de plus d'une heure.

### Requete 5 : 
`
SELECT 
    nom,
    note_moyenne
FROM jeux_de_societe
WHERE note_moyenne >= 8
ORDER BY note_moyenne DESC;
`
- Afficher le nom et la note moyenne des jeux, quand la note est supérieur à 7. Le résultat est affiché de la note moyenne la plus élévée à la moins élevée.

### Requete 6 : 
`
SELECT
    editeur,
    COUNT(*) AS nombre_jeux
FROM jeux_de_societe
GROUP BY editeur
ORDER BY nombre_jeux DESC;
`
- Afficher l'éditeur et le nombre de jeux pour chaque éditeur, du plus grand nombre de jeux au plus petit.

### Requete 7 : 
`
SELECT
    type_jeu,
    AVG(note_moyenne) AS moyenne_note
FROM jeux_de_societe
GROUP BY type_jeu
ORDER BY moyenne_note DESC
LIMIT 3;
`
- Afficher le top 3 des type de jeu avec la meilleur moyenne, et la moyenne associée.

### Requete 8 : 
`
SELECT
    nom,
    duree_minutes,
    nb_joueurs_max
FROM jeux_de_societe
WHERE duree_minutes > 120
AND nb_joueurs_max >= 5;
`
- Afficher le nom, la durée et le nombre de joueurs max des jeux dont la durée de de plus de 2 heures, et qui peux se jouer à plus de 4 joueurs.

### Requete 9 : 
`
SELECT
    annee_sortie,
    COUNT(*) AS nombre_sorties
FROM jeux_de_societe
GROUP BY annee_sortie
ORDER BY annee_sortie;
`
- Afficher l'année de sortie et le nombre de sortie des jeux par année de sortie et dans l'ordre des années de sorties.

### Requete 10 : 
`
SELECT
    editeur,
    AVG(prix) AS prix_moyen
FROM jeux_de_societe
GROUP BY editeur
HAVING AVG(prix) < 25;
`
- Afficher l'éditeur et le prix moyen de chaque éditeur qui ont une moyenne de prix de plus de 25 €.

### Requete 11 : 
`
SELECT
    nom,
    prix,
    note_moyenne
FROM jeux_de_societe
WHERE prix < 40
AND note_moyenne >= 8.5
ORDER BY note_moyenne DESC, prix ASC;
`
Afficher le nom, prix, et note moyennedes jeux de plus de 40€ en ayant une moyenne de 8.5 ou plus. Mettre le résultat dans l'ordre décroissant des moyennes et dans l'ordre croissant de prix.

### Requete 12 : 
`
SELECT
    nom,
    type_jeu
FROM jeux_de_societe
WHERE est_cooperatif = TRUE
AND nb_joueurs_max >= 6;
`
- Afficher le nom et le type de jeu qui sont coopératifs et qui peuvent se jouer a plus de 5.

### Requete 13 :  
`
SELECT
    type_jeu,
    COUNT(*) AS nombre,
    AVG(prix) AS prix_moyen
FROM jeux_de_societe
GROUP BY type_jeu
HAVING COUNT(*) >= 5
ORDER BY prix_moyen DESC;
`
- Pour chaque type de jeu qui contiennent plus de 4 jeux, afficher le type, le nombre, et le prix moyen des jeux, par ordre descroissant du prix moyen.

### Requete 14 :
`
SELECT
    editeur,
    MAX(note_moyenne) AS meilleure_note
FROM jeux_de_societe
GROUP BY editeur
ORDER BY meilleure_note DESC;
`
- Pour chaque éditeur, afficher l'éditeur et la meilleur note, dans l'ordre décroissant de la meilleur note.
