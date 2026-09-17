# Énoncé
Vous avez la table suivante :
```sql
CREATE TABLE jeux_video (
    id INTEGER PRIMARY KEY,
    titre VARCHAR(100),
    genre VARCHAR(30),
    plateforme VARCHAR(30),
    annee_sortie INTEGER,
    editeur VARCHAR(50),
    note_metacritic INTEGER,
    prix DECIMAL(5,2),
    ventes_millions DECIMAL(5,2),
    multijoueur BOOLEAN
);
```  

*Répondez aux questions suivantes :*

# Questions
### Question 1 : Afficher toute la table.
`SELECT *`  
`FROM jeux_video`  

### Question 2 : Afficher tous les titres et genres des jeux vidéo.
`SELECT titre, genre`  
`FROM jeux_video`  

### Question 3 : Afficher tous les genres différents présents dans le catalogue.
`SELECT DISTINCT genre`  
`FROM jeux_video`  

### Question 4 : Afficher toutes les plateformes différentes présentes dans le catalogue.
`SELECT DISTINCT plateforme`  
`FROM jeux_video`  

### Question 5 : Afficher tous les éditeurs différents, triés par ordre alphabétique.
`SELECT DISTINCT editeur`  
`ORDER BY editeur ASC`  

### Question 6 : Afficher les titres, notes et annee de sortie des jeux sortis après 2020.
`SELECT titre, note_metacritic, annee_sortie`  
`FROM jeux_video`  
`WHERE annee_sortie > 2020`  

### Question 7 : Afficher les titres, genres et prix des jeux des éditeurs Nintendo qui coûtent moins de 50€.
`SELECT titre, genre, prix`  
`FROM jeux_video`  
`WHERE editeur = 'Nintendo'`  
`AND prix < 50`  

### Question 8 : Afficher les titres, genres et notes des jeux qui sont des RPG ou qui ont une note d'au moins 95.
`SELECT titre, genre, note_metacritic`  
`FROM jeux_video`  
`WHERE genre = 'RPG'`  
`OR note_metacritic >= 95`  

### Question 9 : Afficher les titres et prix des jeux qui ne sont pas multijoueurs sans compter les NULL.
`SELECT titre, prix`  
`FROM jeux_video`  
`WHERE multijoueur = FALSE`  
`AND multijoueur IS NOT NULL`  

### Question 10 : Afficher les titres et prix des jeux qui ne sont pas multijoueurs, NULL compris.
`SELECT titre, prix`  
`FROM jeux_video`  
`WHERE multijoueur = FALSE`  
`OR multijoueur IS NULL`  

### Question 11 : Afficher les titres et années des jeux des éditeurs Nintendo ou Sony sortis avant
2020.
`SELECT titre, annee_sortie`  
`FROM jeux_video`  
`WHERE (editeur = 'Nintendo' OR editeur = 'Sony')`  
`AND annee_sortie < 2020`  

### Question 12 : Afficher les titres et notes des jeux dont la note Metacritic est comprise entre 85 et 95 inclus.
`SELECT titre, notes`  
`FROM jeux_video`  
`WHERE note_metacritic`  
`BETWEEN 85`  
`AND 95`  

### Question 13 : Afficher les titres et prix des jeux dont le prix est compris entre 19.99€ et 49.99€ inclus.
`SELECT titre, prix`  
`FROM jeux_video`  
`WHERE prix`  
`BETWEEN 19.99`  
`AND 49.99`  

### Question 14 : Afficher les titres des jeux qui commencent par la lettre "C".
`SELECT titre`  
`FROM jeux_video`  
`WHERE titre LIKE 'C%'`  

### Question 15 : Afficher les titres des jeux qui contiennent "The" dans leur titre.
`SELECT titre`  
`FROM jeux_video`  
`WHERE titre LIKE '%The%'`  

### Question 16 : Afficher les titres et prix des jeux dont le prix est manquant (NULL).
`SELECT titre, prix`  
`FROM jeux_video`  
`WHERE prix IS NULL`  

### Question 17 : Afficher les titres et prix des jeux dont le prix n'est pas manquant (NULL).
`SELECT titre, prix`  
`FROM jeux_video`  
`WHERE prix IS NOT NULL`  

### Question 18 : Afficher les titres, genres et notes des jeux qui sont des jeux d'Action, RPG ou Aventure.
`SELECT titre, genre, note_metacritic`  
`FROM jeux_video`  
`WHERE genre IN ('Action', 'RPG', 'Aventure')`  

### Question 19 : Afficher les titres et éditeurs des jeux des éditeurs Nintendo, Sony ou EA.
`SELECT titre, editeur`  
`FROM jeux_video`  
`WHERE editeur IN ('Nintendo', 'Sony', 'EA')`  

### Question 20 : Compter le nombre total de jeux dans le catalogue.
`SELECT count(*) as 'Nombre de jeux'`  
`FROM jeux_video`  

### Question 21 : Compter le nombre de jeux multijoueurs.
`SELECT count(*) as 'Nombre de jeux'`  
`FROM jeux_video`  
`WHERE multijoueur = TRUE`  

### Question 22 : Trouver la note maximale parmi tous les jeux.
`SELECT MAX(note) as 'Note maximale'`  
`FROM jeux_video`  

### Question 23 : Trouver le prix minimum et le prix maximum des jeux.
`SELECT MAX(prix) as 'Prix maximum', MIN(prix) as 'Prix minimum'`  
`FROM jeux_video`  

### Question 24 : Calculer la moyenne des notes Metacritic de tous les jeux.
`SELECT AVG(prix) as 'Moyenne Metacritic'`  
`FROM jeux_video`  

### Question 25 : Calculer la somme totale des ventes (en millions) de tous les jeux.
`SELECT SUM(ventes_millions) as 'Somme totale des ventes en million'`  
`FROM jeux_video`  

### Question 26 : Pour chaque genre, afficher le nombre de jeux et la note moyenne.
`SELECT COUNT(*) as 'Nombre de jeux, AVG(note) as 'Note moyenne'`  
`FROM jeux_video`  
`GROUP BY genre`  

### Question 27 : Pour chaque éditeur, afficher le nombre de jeux, la note maximale et le nombre total de jeux vendus.
`SELECT COUNT(*) as 'Nombre de jeux', MAX(note_metacritic) as 'Note maximale', SUM(ventes_millions) as 'Millions de jeux vendus'`  
`FROM jeux_video`  
`GROUP BY editeur`  

### Question 28 : Pour chaque année de sortie, afficher le nombre de jeux et le prix moyen pour les jeux qui coûtent plus de 39.99€.
`SELECT COUNT(*) as 'Nombre de jeux, AVG(prix) as 'Prix moten'`  
`FROM jeux_video`  
`WHERE prix >= 40`  
`GROUP BY annee_sortie`  

### Question 29 : Afficher les jeux qui sont soit multijoueur soit qui ont vendu plus de 30 millions d'exemplaires, mais pas les deux.
`SELECT titre`  
`FROM jeux_video`  
`WHERE ( multijoueur = TRUE AND NOT ventes_millions > 30)`  
`OR (NOT multijoueur = TRUE AND ventes_millions > 30)`
ou
`SELECT titre`  
`FROM jeux_video`  
`WHERE (multijoueur = TRUE) <> (ventes_millions > 30)`
