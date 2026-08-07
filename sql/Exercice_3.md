# Exercice 3
*Répondez aux questions suivantes :*



### Question 1 : Créer une base de données nommée “bibliotheque”.
`
CREATE DATABASE bibliotheque
`


### Question 2 : Créer une table “livres” avec les colonnes suivantes :
- `
id : entier, clé primaire
titre : chaîne de 100 caractères, obligatoire
auteur : chaîne de 80 caractères, obligatoire
annee_publication : entier
genre : chaîne de 50 caractères
isbn : chaîne de 20 caractères, valeur unique
disponible : booléen, valeur par défaut TRUE
`
---
`
CREATE TABLE livres (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  titre VARCHAR(100) NOT NULL,
  auteur VARCHAR(80) NOT NULL,
  annee_publication SMALLINT,
  genre VARCHAR(50),
  isbn VARCHAR(20) UNIQUE,
  disponible BOOLEAN DEFAULT TRUE
);
`


### Question 3 : Créer une table membres avec les colonnes suivantes :
- `
id : entier, clé primaire
nom : chaîne de 50, obligatoire
prenom : chaîne de 50, obligatoire
email : chaîne de 100, obligatoire et unique
date_adhesion : DATE, valeur par défaut la date du jour
age : entier, doit être supérieur ou égal à 12
`
---
`
CREATE TABLE membres (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  date_adhesion DATE DEFAULT CURRENT_DATE,
  age SMALLINT CHECK (age >= 12)
);
`

### Question 4 : Créer une table emprunts avec :
- `
id : entier, clé primaire
livre_id : entier, obligatoire
membre_id : entier, obligatoire
date_emprunt : DATE, obligatoire
date_retour : DATE
Ajouter une contrainte de clé étrangère sur livre_id qui référence livres(id) ET une sur
membre_id qui référence membres(id).
Ajouter une contrainte pour que date_retour soit postérieure ou égale à date_emprunt.
`
---
`
CREATE TABLE emprunts (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  livre_id INT NOT NULL,
  membre_id INT NOT NULL,
  date_emprunt DATE NOT NULL,
  date_retour DATE
);
ALTER TABLE emprunts
ADD CONSTRAINT fk_emprunts_livre_id_to_livres_id
FOREIGN KEY (livre_id)
REFERENCES livres(id);

ALTER TABLE emprunts
ADD CONSTRAINT fk_emprunts_membre_id_to_membres_id
FOREIGN KEY (membre_id)
REFERENCES membres(id);

ALTER TABLE emprunts 
ADD CONSTRAINT condition_date_retour 
CHECK (date_retour >= date_emprunt);
`

### Question 5 : Ajouter une contrainte sur le couple (livre_id, date_emprunt) dans la table emprunts pour qu'un même livre ne puisse pas être emprunté deux fois le même jour.
`
ALTER TABLE emprunts
ADD CONSTRAINT condition_date_emprunt
UNIQUE (livre_id, date_emprunt);
`


### Question 6 : Ajouter une contrainte sur la table livres pour que annee_publication soit comprise entre 1450 (invention de l'imprimerie) et l'année en cours (2026).
`
ALTER TABLE livres
ADD CONSTRAINT condition_annee_publication
CHECK (annee_publication BETWEEN 1450 AND date_part('year', CURRENT_DATE));
`


### Question 7 : Ajouter une contrainte sur la table membres pour que l'email contienne le caractère @
`
ALTER TABLE membres
ADD CONSTRAINT condition_email
CHECK (email LIKE '%@%');
`


### Question 8 : Insérer ces 5 livres dans la table livres :
- `
Titre Auteur Année Genre ISBN
Le Petit Prince Antoine de
Saint-Exupéry
1943 Conte 978-207061275
8
1984 George Orwell 1949 Science-Fiction 978-207036822
8
Harry Potter J.K. Rowling 1997 Fantasy 978-207064302
8
L'Étranger Albert Camus 1942 Roman 978-207036002
4
Fondation Isaac Asimov 1951 Science-Fiction 978-229002453
7
`
---
`
INSERT INTO livres (titre, auteur, annee_publication, genre, isbn)
VALUES ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', '978-2070612758'),
  ('1984', 'George Orwell', 1949, 'Science-Fiction', '978-2070368228'),
  ('Harry Potter', 'J.K. Rowling', 1997, 'Fantasy', '978-2070643028'),
  ('L''Étranger', 'Albert Camus', 1942, 'Roman', '978-2070360024'),
  ('Fondation', 'Isaac Asimov', 1951, 'Science-Fiction', '978-2290024537');
`


### Question 9 : Créer une table livres_science_fiction à partir d'une requête qui sélectionne tous les livres du genre Science-Fiction, en ne gardant que les colonnes titre, auteur et annee_publication.
`
CREATE TABLE livres_science_fiction AS
  SELECT titre, auteur, annee_publication FROM livres WHERE genre = 'Science-Fiction';
`


### Question 10 : Créer une table membres_adultes à partir d'une requête qui sélectionne les membres âgés de 18 ans ou plus, avec les colonnes nom, prenom et email.
`
CREATE TABLE membres_adultes AS
  SELECT nom, prenom, email FROM membres WHERE age >= 18;
`


### Question 11 : Ajouter une colonne nationalite de type VARCHAR(50) à la table livres.
`
ALTER TABLE livres ADD COLUMN nationalite VARCHAR(50);
`

### Question 12 : Ajouter une colonne telephone de type VARCHAR(15) à la table membres, avec une contrainte UNIQUE.
`
ALTER TABLE membres ADD COLUMN telephone VARCHAR(15) UNIQUE;
`


### Question 13 : Modifier la colonne genre de la table livres pour la passer à VARCHAR(60).
`
ALTER TABLE livres
ALTER COLUMN genre 
TYPE VARCHAR(60);
`


### Question 14 : Renommer la colonne telephone en portable dans la table membres.
`
ALTER TABLE membres
RENAME COLUMN telephone TO portable;
`


### Question 15 : Supprimer la colonne nationalite de la table livres.
`
ALTER TABLE livres
DROP COLUMN nationalite;
`


### Question 16 : Modifier la colonne id de la table membres pour ajouter une generation automatique des id.
`
ALTER TABLE membres ALTER COLUMN id DROP IDENTITY; --On enlève l'auto increment qu'on ne devait pas mettre

ALTER TABLE membres ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;
`


### Question 17 : Il y a eu une erreur pour l'année de publication des livres. Mettez à jour l'année de publication en ajoutant un an sur chaque année de publication.
`
UPDATE livres
SET annee_publication = annee_publication + 1;
`


### Question 18 : Mettez à jour L'Étranger d'Albert Camus pour montrer qu'il n'est plus disponible.
`
UPDATE livres
SET disponible = FALSE
WHERE titre = 'L''Étranger';
`


### Question 19 : Supprimer les livres qui sont indisponibles.
`
DELETE FROM livres
WHERE NOT disponible;
`


### Question 20 : Supprimer la table livres_science_fiction.
`
DROP TABLE livres_science_fiction;
`


### Question 21 : Supprimer toute la base de données bibliotheque.
`
\c <autre base de données> --On ne peut pas supprimer une base de données sur laquelle on est positionné
DROP DATABASE bibliotheque;
`
