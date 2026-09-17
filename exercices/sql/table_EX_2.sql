-- ============================================================
-- Script de création et peuplement de la table jeux_de_societe
-- Pour PostgreSQL
-- ============================================================

-- Suppression de la table si elle existe déjà (pour réexécution propre)


DROP TABLE IF EXISTS jeux_de_societe;

-- Création de la table
CREATE TABLE jeux_de_societe (
    id INTEGER PRIMARY KEY,
    nom VARCHAR(80) NOT NULL,
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

-- ============================================================
-- Insertion des données
-- ============================================================

INSERT INTO jeux_de_societe (id, nom, editeur, type_jeu, nb_joueurs_min, nb_joueurs_max, duree_minutes, note_moyenne, prix, annee_sortie, est_cooperatif) VALUES
(1, 'Les Aventuriers du Rail', 'Days of Wonder', 'Stratégie', 2, 5, 45, 7.5, 44.90, 2004, FALSE),
(2, 'Catan', 'Kosmos', 'Stratégie', 3, 4, 90, 7.3, 39.90, 1995, FALSE),
(3, 'Carcassonne', 'Hans im Glück', 'Stratégie', 2, 5, 45, 7.4, 29.90, 2000, FALSE),
(4, 'Pandemic', 'Z-Man Games', 'Coopératif', 2, 4, 45, 7.6, 39.90, 2008, TRUE),
(5, '7 Wonders', 'Repos Production', 'Stratégie', 2, 7, 30, 7.7, 44.90, 2010, FALSE),
(6, 'Dixit', 'Libellud', 'Ambiance', 3, 6, 30, 7.2, 29.90, 2008, FALSE),
(7, 'Ticket to Ride: Europe', 'Days of Wonder', 'Stratégie', 2, 5, 60, 7.6, 44.90, 2005, FALSE),
(8, 'Azul', 'Plan B Games', 'Abstrait', 2, 4, 45, 7.8, 34.90, 2017, FALSE),
(9, 'Codenames', 'Czech Games Edition', 'Ambiance', 2, 8, 15, 7.6, 19.90, 2015, FALSE),
(10, 'Gloomhaven', 'Cephalofair Games', 'Aventure', 1, 4, 120, 8.7, 139.90, 2017, TRUE),
(11, 'Terraforming Mars', 'FryxGames', 'Stratégie', 1, 5, 120, 8.4, 64.90, 2016, FALSE),
(12, 'Wingspan', 'Stonemaier Games', 'Stratégie', 1, 5, 70, 8.1, 54.90, 2019, FALSE),
(13, 'Splendor', 'Space Cowboys', 'Stratégie', 2, 4, 30, 7.4, 32.90, 2014, FALSE),
(14, 'King of Tokyo', 'IELLO', 'Ambiance', 2, 6, 30, 7.0, 34.90, 2011, FALSE),
(15, 'Munchkin', 'Steve Jackson Games', 'Aventure', 3, 6, 90, 6.5, 24.90, 2001, FALSE),
(16, 'Unlock!', 'Space Cowboys', 'Coopératif', 1, 6, 60, 7.3, 29.90, 2017, TRUE),
(17, 'Dominion', 'Rio Grande Games', 'Deck-building', 2, 4, 30, 7.6, 39.90, 2008, FALSE),
(18, 'Scythe', 'Stonemaier Games', 'Stratégie', 1, 5, 115, 8.2, 79.90, 2016, FALSE),
(19, 'The Crew', 'Kosmos', 'Coopératif', 2, 5, 20, 7.8, 14.90, 2019, TRUE),
(20, 'Everdell', 'Starling Games', 'Stratégie', 1, 4, 80, 8.0, 59.90, 2018, FALSE),
(21, 'Love Letter', 'Z-Man Games', 'Bluff', 2, 4, 20, 7.1, 11.90, 2012, FALSE),
(22, 'Root', 'Leder Games', 'Stratégie', 2, 4, 90, 8.1, 54.90, 2018, FALSE),
(23, 'Brass: Birmingham', 'Roxley Games', 'Stratégie', 2, 4, 120, 8.6, 64.90, 2018, FALSE),
(24, 'Spirit Island', 'Greater Than Games', 'Coopératif', 1, 4, 120, 8.3, 69.90, 2017, TRUE),
(25, 'Sushi Go!', 'Gamewright', 'Famille', 2, 5, 15, 7.2, 12.90, 2013, FALSE),
(26, '7 Wonders Duel', 'Repos Production', 'Stratégie', 2, 2, 30, 8.1, 24.90, 2015, FALSE),
(27, 'Hanabi', 'R&R Games', 'Coopératif', 2, 5, 25, 7.3, 10.90, 2010, TRUE),
(28, 'Takenoko', 'Matagot', 'Famille', 2, 4, 45, 7.3, 34.90, 2011, FALSE),
(29, 'Patchwork', 'Lookout Games', 'Abstrait', 2, 2, 30, 7.7, 24.90, 2014, FALSE),
(30, 'Arkham Horror', 'Fantasy Flight Games', 'Coopératif', 1, 6, 180, 7.4, 59.90, 2005, TRUE);

-- ============================================================
-- Vérification : afficher les données insérées
-- ============================================================
SELECT * FROM jeux_de_societe ORDER BY id;
