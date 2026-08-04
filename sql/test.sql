-- ============================================================
-- Script de test PostgreSQL complet
-- Base de données : boutique_test
-- ============================================================

-- 1. Supprimer la base si elle existe déjà (pour pouvoir relancer le script)
DROP DATABASE IF EXISTS boutique_test;

-- 2. Créer la base de données
CREATE DATABASE boutique_test;

-- 3. Se connecter à la nouvelle base (commande psql)
\c boutique_test

-- ============================================================
-- CRÉATION DES TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS clients (
    id_client SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    ville VARCHAR(100),
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    id_categorie SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS produits (
    id_produit SERIAL PRIMARY KEY,
    nom VARCHAR(150) NOT NULL,
    description TEXT,
    prix DECIMAL(10, 2) NOT NULL CHECK (prix >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    id_categorie INTEGER REFERENCES categories(id_categorie),
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS commandes (
    id_commande SERIAL PRIMARY KEY,
    id_client INTEGER NOT NULL REFERENCES clients(id_client),
    date_commande TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut VARCHAR(50) DEFAULT 'en_attente',
    total DECIMAL(10, 2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS details_commande (
    id_detail SERIAL PRIMARY KEY,
    id_commande INTEGER NOT NULL REFERENCES commandes(id_commande),
    id_produit INTEGER NOT NULL REFERENCES produits(id_produit),
    quantite INTEGER NOT NULL CHECK (quantite > 0),
    prix_unitaire DECIMAL(10, 2) NOT NULL
);

-- ============================================================
-- REMPLISSAGE DES TABLES
-- ============================================================

INSERT INTO clients (nom, prenom, email, ville) VALUES
('Dupont', 'Marie', 'marie.dupont@email.com', 'Paris'),
('Martin', 'Jean', 'jean.martin@email.com', 'Lyon'),
('Bernard', 'Sophie', 'sophie.bernard@email.com', 'Marseille'),
('Petit', 'Lucas', 'lucas.petit@email.com', 'Paris'),
('Robert', 'Emma', 'emma.robert@email.com', 'Lyon');

INSERT INTO categories (nom, description) VALUES
('Électronique', 'Appareils électroniques et gadgets'),
('Livres', 'Livres, romans et manuels'),
('Maison', 'Articles de décoration et mobilier'),
('Sport', 'Équipements sportifs et vêtements');

INSERT INTO produits (nom, description, prix, stock, id_categorie) VALUES
('Casque Bluetooth', 'Casque sans fil avec réduction de bruit', 129.99, 45, 1),
('Roman SF', 'Le meilleur roman de science-fiction de l année', 19.50, 120, 2),
('Lampe Design', 'Lampe de bureau LED moderne', 59.00, 30, 3),
('Tapis de Yoga', 'Tapis antidérapant écologique', 35.00, 80, 4),
('Enceinte WiFi', 'Enceinte connectée avec assistant vocal', 89.99, 25, 1),
('Cuisine du Monde', 'Livre de recettes internationales', 24.90, 60, 2),
('Set de Poids', 'Haltères ajustables 2-20kg', 149.00, 15, 4);

INSERT INTO commandes (id_client, statut, total) VALUES
(1, 'livree', 149.49),
(2, 'expediee', 89.99),
(1, 'en_attente', 83.50),
(3, 'livree', 24.90),
(4, 'expediee', 188.99);

INSERT INTO details_commande (id_commande, id_produit, quantite, prix_unitaire) VALUES
(1, 1, 1, 129.99),
(1, 2, 1, 19.50),
(2, 5, 1, 89.99),
(3, 3, 1, 59.00),
(3, 4, 1, 35.00),
(4, 6, 1, 24.90),
(5, 7, 1, 149.00),
(5, 4, 1, 35.00),
(5, 2, 1, 19.50);

-- ============================================================
-- REQUÊTES DE LECTURE
-- ============================================================

-- 4. Liste simple de tous les clients
SELECT '=== LISTE DES CLIENTS ===' AS section;
SELECT * FROM clients;

-- 5. Produits avec leur catégorie (JOIN simple)
SELECT '=== PRODUITS ET CATÉGORIES ===' AS section;
SELECT p.nom AS produit, c.nom AS categorie, p.prix, p.stock
FROM produits p
JOIN categories c ON p.id_categorie = c.id_categorie
ORDER BY p.prix DESC;

-- 6. Commandes d un client avec détails (JOIN multiple)
SELECT '=== COMMANDES DE MARIE DUPONT ===' AS section;
SELECT co.id_commande, co.date_commande, co.statut,
       p.nom AS produit, dc.quantite, dc.prix_unitaire,
       (dc.quantite * dc.prix_unitaire) AS sous_total
FROM commandes co
JOIN details_commande dc ON co.id_commande = dc.id_commande
JOIN produits p ON dc.id_produit = p.id_produit
JOIN clients cl ON co.id_client = cl.id_client
WHERE cl.nom = 'Dupont'
ORDER BY co.date_commande;

-- 7. Chiffre d affaires par catégorie (GROUP BY + agrégation)
SELECT '=== CHIFFRE D AFFAIRES PAR CATÉGORIE ===' AS section;
SELECT c.nom AS categorie,
       COUNT(DISTINCT p.id_produit) AS nb_produits,
       SUM(dc.quantite * dc.prix_unitaire) AS chiffre_affaires
FROM categories c
LEFT JOIN produits p ON c.id_categorie = p.id_categorie
LEFT JOIN details_commande dc ON p.id_produit = dc.id_produit
GROUP BY c.nom
ORDER BY chiffre_affaires DESC NULLS LAST;

-- 8. Top 3 des meilleurs clients (GROUP BY + HAVING)
SELECT '=== TOP CLIENTS ===' AS section;
SELECT cl.nom, cl.prenom, cl.ville,
       COUNT(DISTINCT co.id_commande) AS nb_commandes,
       SUM(co.total) AS montant_total
FROM clients cl
JOIN commandes co ON cl.id_client = co.id_client
GROUP BY cl.id_client, cl.nom, cl.prenom, cl.ville
HAVING COUNT(DISTINCT co.id_commande) >= 1
ORDER BY montant_total DESC
LIMIT 3;

-- 9. Produits en stock faible (moins de 30 unités)
SELECT '=== STOCK FAIBLE ===' AS section;
SELECT nom, stock,
       CASE 
           WHEN stock = 0 THEN 'RUPTURE'
           WHEN stock < 20 THEN 'CRITIQUE'
           ELSE 'FAIBLE'
       END AS alerte
FROM produits
WHERE stock < 30
ORDER BY stock ASC;

-- ============================================================
-- MISE À JOUR ET SUPPRESSION (exemples)
-- ============================================================

-- 10. Mise à jour du statut d une commande
UPDATE commandes SET statut = 'livree' WHERE id_commande = 2;

-- 11. Mise à jour du stock après vente
UPDATE produits SET stock = stock - 1 WHERE id_produit = 1;

-- 12. Vérification post-mise à jour
SELECT '=== STOCK APRÈS MISE À JOUR ===' AS section;
SELECT nom, stock FROM produits WHERE id_produit = 1;

-- ============================================================
-- STATISTIQUES GLOBALES
-- ============================================================

SELECT '=== STATISTIQUES GLOBALES ===' AS section;
SELECT 
    (SELECT COUNT(*) FROM clients) AS total_clients,
    (SELECT COUNT(*) FROM produits) AS total_produits,
    (SELECT COUNT(*) FROM commandes) AS total_commandes,
    (SELECT SUM(total) FROM commandes) AS ca_total,
    (SELECT AVG(prix) FROM produits) AS prix_moyen_produit;

-- ============================================================
-- FIN DU SCRIPT
-- ============================================================
