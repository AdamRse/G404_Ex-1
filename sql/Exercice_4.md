# Exercice 4

*Vous avez les tables et données suivantes :*
```sql
DROP TABLE IF EXISTS utilisateurs CASCADE;
CREATE TABLE utilisateurs (
id INTEGER PRIMARY KEY,
pseudo VARCHAR(50) NOT NULL UNIQUE,
email VARCHAR(100) NOT NULL UNIQUE,
date_inscription DATE DEFAULT CURRENT_DATE,
parrain_id INTEGER REFERENCES utilisateurs(id)
);
DROP TABLE IF EXISTS jeux CASCADE;
CREATE TABLE jeux (
id INTEGER PRIMARY KEY,
titre VARCHAR(100) NOT NULL,
editeur VARCHAR(50),
annee_sortie INTEGER,
prix DECIMAL(5,2)
);
DROP TABLE IF EXISTS bibliotheques CASCADE;
CREATE TABLE bibliotheques (
id INTEGER PRIMARY KEY,
utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id),
jeu_id INTEGER NOT NULL REFERENCES jeux(id),
date_achat DATE,
heures_jouees DECIMAL(6,1)
);
DROP TABLE IF EXISTS avis CASCADE;
CREATE TABLE avis (
id INTEGER PRIMARY KEY,
utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id),
jeu_id INTEGER NOT NULL REFERENCES jeux(id),
note INTEGER CHECK (note BETWEEN 1 AND 5),
commentaire TEXT,
date_avis DATE
);
INSERT INTO utilisateurs VALUES
(1, 'ShadowSlayer', 'shadow@email.com', '2023-01-15', NULL),
(2, 'PixelQueen', 'pixel@email.com', '2023-03-22', 1),
(3, 'NoobMaster42', 'noob@email.com', '2023-06-10', 1),
(4, 'DragonFury', 'dragon@email.com', '2024-01-05', 2),
(5, 'LootGoblin', 'loot@email.com', '2024-02-14', 2),
(6, 'StealthArcher', 'stealth@email.com', '2024-05-30', 3),
(7, 'MageFireball', 'mage@email.com', '2024-08-18', NULL),
(8, 'TankBuster', 'tank@email.com', '2025-01-10', 7),
(9, 'NoobBuster', 'buster@email.com', '2024-09-19', NULL);
INSERT INTO jeux VALUES
(1, 'Elden Ring', 'Bandai Namco', 2022, 69.99),
(2, 'Baldur''s Gate 3', 'Larian Studios',2023, 59.99),
(3, 'Cyberpunk 2077', 'CD Projekt Red', 2020, 29.99),
(4, 'Hollow Knight', 'Team Cherry', 2017, 14.99),
(5, 'Stardew Valley', 'ConcernedApe', 2016, 14.99),
(6, 'God of War Ragnarok', 'Sony', 2022, 69.99),
(7, 'Portal 2', 'Valve', 2011, 9.99),
(8, 'Among Us', 'Innersloth', 2018, 4.99),
(9, 'Witcher 3', 'CD Projekt Red', 2015, 29.99);
INSERT INTO bibliotheques VALUES
(1, 1, 1, '2023-01-20', 120.5),
(2, 1, 3, '2023-02-10', 45.0),
(3, 1, 7, '2023-03-05', 8.5),
(4, 2, 2, '2023-04-01', 200.0),
(5, 2, 5, '2023-04-15', 350.0),
(6, 2, 6, '2024-01-20', 60.0),
(7, 3, 1, '2023-07-01', 15.0),
(8, 3, 8, '2023-07-15', 500.0),
(9, 4, 2, '2024-01-20', 180.0),
(10, 4, 4, '2024-02-10', 40.0),
(11, 5, 3, '2024-03-01', 75.0),
(12, 5, 5, '2024-03-15', 20.0),
(13, 6, 1, '2024-06-10', 95.0),
(14, 6, 4, '2024-06-20', 55.0),
(15, 6, 7, '2024-07-01', 30.0),
(16, 7, 2, '2024-09-01', 250.0),
(17, 7, 6, '2024-09-15', 10.0),
(18, 8, 1, '2025-01-15', 5.0),
(19, 8, 8, '2025-01-20', 12.0);
INSERT INTO avis VALUES
(1, 1, 1, 5, 'Chef-d''oeuvre absolu !', '2023-02-01'),
(2, 1, 3, 3, 'Bonne ambiance mais buggé au lancement', '2023-03-15'),
(3, 2, 2, 5, 'Jeu de rôle ultime, 200h et pas lassé', '2023-05-01'),
(4, 2, 5, 4, 'Parfait pour se détendre', '2023-06-01'),
(5, 3, 1, 2, 'Trop difficile pour moi...', '2023-08-01'),
(6, 3, 8, 4, 'Excellent pour les soirées entre amis', '2023-09-01'),
(7, 4, 2, 5, 'Meilleur jeu de rôle jamais créé', '2024-03-01'),
(8, 4, 4, 5, 'Un bijou danimation et de gameplay', '2024-03-15'),
(9, 5, 3, 4, 'Beaucoup amélioré depuis le lancement', '2024-04-01'),
(10, 6, 1, 5, 'Difficile mais gratifiant', '2024-07-01'),
(11, 6, 7, 5, 'Un des meilleurs puzzles games', '2024-08-01'),
(12, 7, 2, 4, 'Excellent mais une fin un peu rapide', '2024-10-01'),
(13, 8, 1, 3, 'Je débute, ça va venir...', '2025-02-01');
```
*Répondez aux questions suivantes :*

## Question 1 : Afficher tous les noms de jeux, les commentaires et les notes laissés. Les jeux sans avis doivent apparaître aussi.



## Question 2 : Afficher le pseudo de chaque utilisateur qui possède au moins un jeu.



## Question 3 : Trouver les jeux qui n'ont reçu aucun avis.



## Question 4 : Trouver les utilisateurs qui n'ont aucun jeu dans leur bibliothèque.



## Question 5 : Afficher les nombres moyens d'heures jouées pour chaque jeu.



## Question 6 : Afficher le pseudo de chaque utilisateur et le titre des jeux qu'il possède dans sa bibliothèque.



## Question 7 : Afficher les pseudos, titres de jeux et notes pour tous les avis laissés.



## Question 8 : Afficher les pseudos, titres et heures jouées, triés par heures jouées décroissantes, limité aux 5 premiers.



## Question 9 : Pour chaque utilisateur, afficher son pseudo et le nombre de jeux qu'il possède, trié du plus grand au plus petit.



## Question 10 : Afficher les pseudos, titres de jeux et notes pour les avis dont la note est supérieure ou égale à 4, trié par note décroissante.



## Question 11 : Afficher tous les utilisateurs et le titre des jeux qu'ils possèdent. Les utilisateurs sans jeu doivent apparaître aussi.



## Question 12 : Pour chaque utilisateur, afficher son pseudo et la moyenne de ses notes données. Les utilisateurs qui n'ont donné aucun avis doivent apparaître avec NULL.



## Question 13 : Afficher tous les jeux et les pseudos des utilisateurs qui les possèdent. L'objectif est que tous les jeux apparaissent, même ceux qui ne sont dans aucune bibliothèque.



## Question 14 : Afficher tous les utilisateurs et tous les jeux, avec les heures jouées quand un utilisateur possède un jeu.



## Question 15 : Trouver les utilisateurs sans jeu et les jeux sans propriétaire.



## Question 16 : Pour chaque jeu, afficher son titre et la note moyenne reçue. Tous les jeux doivent apparaître, même ceux sans note.



## Question 17 : Afficher le pseudo de chaque utilisateur et le pseudo de son parrain (celui qui l'a invité).



## Question 18 : Trouver les utilisateurs qui ont parrainé au moins 2 personnes, avec le nombre de filleuls.



## Question 19 : Trouve les utilisateurs qui n'ont pas été parrainés et qui n'ont parrainé personne.



## Question 20 : Générer toutes les combinaisons possibles entre les utilisateurs et les jeux. Afficher seulement les 10 premières lignes.



## Question 21 : Afficher le commentaire, le pseudo, le titre du jeu, la note donnée et les heures jouées pour chacun des avis.



## Question 22 : Afficher tous les utilisateurs, les jeux qu'ils possèdent (avec heures jouées), et les notes qu'ils ont donné. Inclure les utilisateurs sans jeu, les jeux sans avis, et les avis sans possession.



## Question 23 : Afficher les jeux du plus rentable au moins rentable en heures jouées moyennes par euro payé. Afficher le nom du jeu et le ratio demandé.



## Question 24 : Afficher, pour l'utilisateur ShadowSlayer, toute la chaîne de générations de ses filleuls et leurs propres filleuls.
