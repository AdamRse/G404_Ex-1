DROP TABLE IF EXISTS participations, evaluations, inscriptions, ateliers, entreprises, formateurs, formations, apprenants CASCADE;

CREATE TABLE apprenants (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 prenom VARCHAR(50) NOT NULL,
 nom VARCHAR(50) NOT NULL,
 email VARCHAR(100) UNIQUE,
 ville VARCHAR(50),
 date_naissance DATE,
 date_adhesion DATE NOT NULL,
 telephone VARCHAR(20)
);

CREATE TABLE formations (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 titre VARCHAR(80) NOT NULL,
 niveau VARCHAR(10) NOT NULL,
 duree_semaines INT NOT NULL,
 prix NUMERIC(8,2) NOT NULL
);

CREATE TABLE inscriptions (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 apprenant_id INT NOT NULL REFERENCES apprenants(id),
 formation_id INT NOT NULL REFERENCES formations(id),
 date_inscription DATE NOT NULL,
 montant_paye NUMERIC(8,2),
 statut VARCHAR(20) NOT NULL DEFAULT 'en cours'
);

CREATE TABLE ateliers (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 titre VARCHAR(80) NOT NULL,
 date_atelier TIMESTAMP NOT NULL,
 duree_heures INT NOT NULL,
 ville VARCHAR(50) NOT NULL
);

CREATE TABLE participations (
 atelier_id INT NOT NULL REFERENCES ateliers(id),
 apprenant_id INT NOT NULL REFERENCES apprenants(id),
 present BOOLEAN NOT NULL DEFAULT false,
 PRIMARY KEY (atelier_id, apprenant_id)
);

CREATE TABLE evaluations (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 apprenant_id INT NOT NULL REFERENCES apprenants(id),
 formation_id INT NOT NULL REFERENCES formations(id),
 note INT NOT NULL CHECK (note BETWEEN 0 AND 100),
 date_evaluation DATE NOT NULL
);

CREATE TABLE entreprises (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 nom VARCHAR(80) NOT NULL,
 ville VARCHAR(50) NOT NULL,
 secteur VARCHAR(40)
);

CREATE TABLE formateurs (
 id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 prenom VARCHAR(50) NOT NULL,
 nom VARCHAR(50) NOT NULL,
 ville VARCHAR(50),
 specialite VARCHAR(50)
);


INSERT INTO apprenants (prenom, nom, email, ville, date_naissance, date_adhesion, telephone) VALUES
('Camille','Grand', 'camille.grand@mail.fr', 'Roanne', '1998-04-12', '2023-09-01', '0612345678'),
('Hugo', 'Bernard', 'hugo.bernard@mail.fr', 'Saint-Étienne', '2001-11-23', '2022-09-15', NULL),
('Awa', 'Traoré', 'awa.traore@mail.fr', 'Villeurbanne', '1997-04-07', '2023-09-04', '0623456789'),
('Emma', 'Nguyen', 'emma.nguyen@mail.fr', 'Lyon', '2000-02-17', '2024-02-13', '0634567890'),
('Léa', 'Petit', 'lea.petit@mail.fr', 'Vichy', '2002-09-30', '2025-09-02', '0645678901'),
('Noah', 'Dubois', 'noah.dubois@mail.fr', 'Saint-Étienne', '2004-04-08', '2026-01-06', NULL),
('Gabriel','Martin', 'gabriel.martin@mail.fr', 'Roanne', '2003-03-15', '2025-01-03', '0656789012'),
('Mané', 'Lefebvre', 'mane.lefebvre@mail.fr', 'Villeurbanne', '1998-03-14', '2022-06-01', '0667890123'),
('Sara', 'Benali', 'sara.benali@mail.fr', 'Lyon', '2002-12-01', '2025-09-10', '0678901234'),
('Thomas', 'Roux', 'thomas.roux@mail.fr', 'Roanne', '1999-05-25', '2023-10-01', '0689012345');


INSERT INTO formations (titre, niveau, duree_semaines, prix) VALUES
('Développeur web', 'Bac+2', 45, 8850.00),
('Concepteur d''application', 'Bac+2', 52, 12500.00),
('Intégrateur IA', 'Bac+2', 52, 9900.00),
('CRM Manager', 'Bac+2', 40, 7900.00),
('Cybersécurité', 'Bac+2', 45, 10800.00),
('Data Engineer', 'Bac+2', 50, 9900.00),
('Concepteur UI', 'Bac+2', 42, 8400.00),
('Concepteur 3D', 'Bac+2', 48, 8700.00);


INSERT INTO inscriptions (apprenant_id, formation_id, date_inscription, montant_paye, statut) VALUES
(1, 6, '2023-10-01', 4950.00, 'en cours'),
(2, 2, '2022-09-15', 12500.00, 'terminee'),
(2, 1, '2025-09-10', NULL, 'en cours'),
(3, 6, '2023-09-06', 9900.00, 'terminee'),
(3, 3, '2025-10-01', 4000.00, 'en cours'),
(4, 5, '2024-09-15', 10800.00, 'terminee'),
(5, 4, '2024-06-02', NULL, 'en cours'),
(6, 1, '2025-09-20', 3000.00, 'en cours'),
(7, 6, '2026-01-06', 9900.00, 'en cours'),
(8, 7, '2022-06-01', 8400.00, 'terminee'),
(9, 4, '2025-10-06', 3000.00, 'en cours'),
(10, 3, '2024-10-01', 5000.00, 'abandon'),
(10, 5, '2025-01-30', 5000.00, 'en cours'),
(10, 2, '2022-09-15', 12500.00, 'terminee'),
(10, 2, '2022-09-15', 12500.00, 'terminee');


INSERT INTO ateliers (titre, date_atelier, duree_heures, ville) VALUES
('Atelier SQL découverte', '2026-03-12 18:00:00', 2, 'Roanne'),
('Atelier Python initiation', '2026-05-20 18:00:00', 2, 'Saint-Étienne'),
('Table ronde IA & métiers', '2026-06-15 10:00:00', 3, 'Villeurbanne'),
('Atelier CV numérique', '2026-08-18 14:00:00', 2, 'Lyon'),
('Hackathon data 24h', '2026-04-25 09:00:00', 24, 'Villeurbanne'),
('Atelier IA générative', '2026-07-15 18:30:00', 2, 'Lyon'),
('Job dating numérique', '2026-09-15 10:00:00', 4, 'Saint-Étienne');


INSERT INTO participations (atelier_id, apprenant_id, present) VALUES
(1, 1, true),
(1, 3, true),
(1, 6, true),
(1, 10, true),
(2, 1, true),
(2, 3, true),
(2, 7, true),
(3, 4, true),
(3, 8, true),
(4, 5, true),
(4, 9, true),
(5, 3, true),
(5, 7, true);


INSERT INTO evaluations (apprenant_id, formation_id, note, date_evaluation) VALUES
(1, 6, 88, '2025-03-01'),
(2, 2, 85, '2024-01-15'),
(3, 6, 92, '2024-02-10'),
(4, 5, 88, '2025-03-20'),
(5, 4, 64, '2025-01-10'),
(6, 1, 55, '2026-01-15'),
(7, 6, 82, '2026-02-12'),
(8, 7, 91, '2022-05-01'),
(9, 4, 63, '2025-12-15'),
(10, 3, 70, '2025-01-15'),
(10, 5, 74, '2023-06-15'),
(3, 2, 93, '2023-06-05');


INSERT INTO entreprises (nom, ville, secteur) VALUES
('Lexi', 'Roanne', 'ESN'),
('DataCorner', 'Lyon', 'Data'),
('CyberNova', 'Villeurbanne', 'Cybersécurité'),
('IndustLab 42','Roanne', 'Industrie 4.0'),
('DataWave', 'Lyon', 'Marketing digital');


INSERT INTO formateurs (prenom, nom, ville, specialite) VALUES
('Marie', 'Claire', 'Roanne', 'Data / SQL'),
('David', 'Lopez', 'Lyon', 'Python'),
('Ana', 'Silva', 'Saint-Étienne', 'IA'),
('Ilies', 'Ndiaye', 'Villeurbanne', 'Cybersécurité');