# Exercice 5
*Vous avez la table et données suivantes :*
```sql
DROP TABLE IF EXISTS coureurs;
CREATE TABLE coureurs (
id INTEGER PRIMARY KEY,
nom_complet VARCHAR(60),
ville VARCHAR(40),
dossard VARCHAR(8),
categorie VARCHAR(30),
temps VARCHAR(8), -- format HH:MM:SS
distance_km DECIMAL(4,1),
classement INTEGER,
a_fini BOOLEAN
);
INSERT INTO coureurs VALUES
(1, 'Jean Dupont', ' Lyon', 'A101', 'Senior Homme', '01:32:45', 21.1, 1, TRUE),
(2, 'Marie Petit', 'Roanne', 'A102', 'Senior Femme', '01:44:12', 21.1, 3, TRUE),
(3, 'Paul Martin', 'Saint-Etienne','B105','Veteran Homme', '01:38:50', 21.1, 2, TRUE),
(4, 'Julie Bernard', 'Villeurbanne','A104', 'Senior Femme', '01:51:30', 21.1, 5, TRUE),
(5, 'Luc Robert', 'Lyon', 'C201', 'Junior Homme', '01:47:15', 21.1, 4, TRUE),
(6, 'Emma Faure', 'Clermont', 'B310', 'Senior Femme', '02:03:40', 21.1, 8, TRUE),
(7, 'Hugo Girard', 'Paris', 'E450', 'Veteran Homme', '02:22:15', 21.1, 12, FALSE),
(8, 'Léa Morel', 'Lyon', 'B311', 'Senior Femme', '01:59:05', 21.1, 6, TRUE),
(9, 'Adam Lefèvre', ' Marseille', 'F600', 'Senior Homme', '03:10:22', 21.1, 15, FALSE),
(10, 'Chloé Rousseau', 'Lyon', 'D322', 'Veteran Femme', '02:01:48', 21.1, 7, TRUE),
(11, 'Tom Roussel', 'Grenoble', 'E777', 'Senior Homme', '02:30:11', 21.1, 13, TRUE),
(12, 'Sarah Lambert', 'Annecy', 'A108', 'Senior Femme', '01:53:02', 21.1, NULL, TRUE),
(13, 'Louis Perrin', 'Lyon', 'G998', 'Veteran Homme', '02:44:33', 21.1, 14, FALSE),
(14, 'Alice Blanc', 'Lyon', 'B203', 'Senior Femme', '02:03:55', 21.1, 9, TRUE),
(15, 'Gabriel Michel', 'Toulouse', 'H654', 'Senior Homme', '03:22:47', 21.1, 16, FALSE),
(16, 'Zoé Guerin', 'Nantes', 'A145', 'Junior Femme', '02:07:19', 21.1, 10, TRUE),
(17, 'Victor Chevalier', 'Lyon', 'D012', 'Veteran Homme', '02:35:50', 21.1, NULL, FALSE),
(18, 'Manon Test', 'Dijon', 'R120', 'Senior Femme', '02:55:00', 21.1, NULL, FALSE),
(19, 'Alexis Marchand', 'Amiens', 'C301', 'Senior Homme', '02:22:58', 21.1, 11, TRUE),
(20, 'Eva Fournier', 'Lyon', 'B777', 'Veteran Femme', '02:58:30', 21.1, NULL, FALSE),
(21, 'Lucas Renard', 'Toulouse', 'F555', 'Senior Homme', '03:15:22', 21.1, NULL, FALSE),
(22, 'Inès Lambert', 'Lyon', 'A200', 'Junior Femme', '02:12:45', 21.1, NULL, TRUE),
(23, 'Rayan Moreau', 'Lille', 'E888', 'Senior Homme', '02:49:12', 21.1, NULL, TRUE),
(24, 'Camille Noel', 'Lyon', 'B909', 'Senior Femme', '02:41:30', 21.1, NULL, TRUE),
(25, 'Antoine Vasseur', 'Brest', 'G700', 'Veteran Homme', '03:22:00', 21.1, NULL, FALSE),
(26, 'Nina Leclerc', 'Lyon', 'D340', 'Junior Femme', '02:47:15', 21.1, NULL, TRUE),
(27, 'Julien Aubert', 'Nice', 'A111', 'Senior Homme', '03:00:01', 21.1, NULL, FALSE),
(28, 'Sarah Colin', 'Lyon', 'C777', 'Senior Femme', '02:52:33', 21.1, NULL, TRUE),
(29, 'Théo Barbier', 'Reims', 'F222', 'Senior Homme', '03:28:44', 21.1, NULL, FALSE),
(30, 'Lily Gauthier', 'Lyon', 'A309', 'Junior Femme', '02:36:09', 21.1, NULL, TRUE);
```
*Répondez aux questions suivantes :*

## Question 1 : Afficher le nom complet de chaque coureur en majuscule et en minuscule.
```sql
SELECT 
    UPPER(nom_complet) AS nom_majuscule,
    LOWER(nom_complet) AS nom_minuscule
FROM coureurs;
```


## Question 2 : Afficher une colonne qui concatène la ville et le dossard (ex: 'Lyon - A101') pour chaque coureur.
```sql
SELECT 
    CONCAT(ville, ' - ', dossard) AS ville_dossard
FROM coureurs;
```


## Question 3 : Afficher le nom complet et une nouvelle colonne initiale_prenom qui contient le premier caractère du nom.
```sql
SELECT 
    nom_complet,
    LEFT(SPLIT_PART(nom_complet, ' ', 1), 1) AS initiale_prenom
FROM coureurs;
```


## Question 4 : Afficher les coureurs dont le nom complet commence par 'M'. Trouver deux solutions.
```sql
-- avec like
SELECT * FROM coureurs WHERE nom_complet LIKE 'M%';
-- avec left
SELECT * FROM coureurs WHERE LEFT(nom_complet, 1) = 'M';
```


## Question 5 : Afficher le nom complet de chaque coureur avec sa longueur en nombre de caractères.
```sql
SELECT 
    nom_complet,
    LENGTH(nom_complet) AS "Nb de caractères"
FROM coureurs;
```


## Question 6 : Afficher le prénom et le nom de famille de chaque coureur dans des colonnes séparées.
```sql
SELECT 
    SPLIT_PART(nom_complet, ' ', 1) AS prenom,
    SPLIT_PART(nom_complet, ' ', 2) AS "Nom de famille"
FROM coureurs;
```


## Question 7 : Certains noms de villes ont pu être saisis avec des espaces en trop. Afficher les noms de villes sans ses espaces en trop.
```sql
SELECT TRIM(ville) AS ville_nettoyee
FROM coureurs;
```


## Question 8 : Afficher la lettre au début de chaque numéro de dossard dans une colonne, et le numéro de dossard sans cette lettre dans une autre colonne.
```sql
SELECT 
    LEFT(dossard, 1) AS "Lettre dossard",
    SUBSTRING(dossard, 2) AS "Numéro de dossard"
FROM coureurs;
```


## Question 9 : Afficher pour chaque coureur le nom_complet avec la catégorie en majuscules, concaténée de manière lisible (ex : 'nom_complet : CATEGORIE').
```sql
SELECT 
    CONCAT(nom_complet, ' : ', UPPER(categorie)) AS "nom et catégorie"
FROM coureurs;
```


## Question 10 : Remplacer dans ville toutes les occurrences de 'y' par 'Y'.
```sql
SELECT REPLACE(ville, 'y', 'Y') AS "ville corrigée"
FROM coureurs;
```


## Question 11 : Afficher le nom complet sans les espaces (on garde le texte collé).
```sql
SELECT REPLACE(nom_complet, ' ', '') AS "nom"
FROM coureurs;
```


## Question 12 : Afficher les coureurs de la ville de Lyon. Attention, certains noms de villes ont peut-être des espaces en trop.
```sql
SELECT *
FROM coureurs
WHERE TRIM(ville) = 'Lyon';
```


## Question 13 : Créer une colonne status qui affiche 'A terminé' ou 'Abandon' en fonction de si le coureur a fini la course ou pas.
```sql
SELECT 
    nom_complet,
    CASE 
        WHEN a_fini THEN 'A terminé'
        ELSE 'Abandon'
    END AS status
FROM coureurs;
```


## Question 14 : Afficher une colonne tranche_temps selon le temps. Si le temps commence par 01: -> 'Moins de 2h', s'il commence par 02: -> 'Entre 2h et 3h', sinon -> 'Plus de 3h'.
```sql
SELECT 
    nom_complet,
    temps,
    CASE 
        WHEN LEFT(temps, 3) = '01:' THEN 'Moins de 2h'
        WHEN LEFT(temps, 3) = '02:' THEN 'Entre 2h et 3h'
        ELSE 'Plus de 3h'
    END AS tranche_temps
FROM coureurs;
```


## Question 15 : Afficher une colonne ville_maj qui met la ville en majuscules uniquement si elle contient exactement 4 caractères, sinon garder la valeur d'origine.
```sql
SELECT 
    ville,
    CASE 
        WHEN LENGTH(ville) = 4 THEN UPPER(ville)
        ELSE ville
    END AS ville_maj
FROM coureurs;
```


## Question 16 : Créer une colonne 'niveau'. Si le coureur a terminé et a un classement <= 5 alors afficher 'Elite', sinon afficher 'Terminé' ou 'Non fini'.
```sql
SELECT 
    nom_complet,
    classement,
    a_fini,
    CASE 
        WHEN a_fini AND classement <= 5 THEN 'Elite'
        WHEN a_fini THEN 'Terminé'
        ELSE 'Non terminé'
    END AS niveau
FROM coureurs;
```


## Question 17 : Afficher le nom_complet et le classement, mais remplace les NULL de classement par le texte 'Non classé'.
```sql
SELECT 
    nom_complet,
    CASE 
        WHEN classement IS NULL THEN 'Non classé'
        ELSE classement::TEXT
    END AS classement
FROM coureurs;
-- Méthode trouvée COALESCE
SELECT 
    nom_complet,
    COALESCE(classement::TEXT, 'Non classé') AS classement
FROM coureurs;
```


## Question 18 : Afficher les initiales (1er caractère du prénom + 1er caractère du nom) pour chaque coureur.
```sql
SELECT 
    nom_complet,
    CONCAT(
        LEFT(SPLIT_PART(nom_complet, ' ', 1), 1),
        LEFT(SPLIT_PART(nom_complet, ' ', 2), 1)
    ) AS initiales
FROM coureurs;
```


## Question 19 : Créer un acronyme du nom de chaque ville en ne prenant que les trois premières lettres et les mettant en majuscule, et donner le nombre de coureurs pour chaque ville. Ne montrer que les villes qui ont au moins deux coureurs, et les mettre dans l'ordre décroissant de nombre de coureurs.
```sql
SELECT 
    UPPER(LEFT(ville, 3)) AS "Acronyme de la ville",
    COUNT(*) AS nb_coureurs
FROM coureurs
GROUP BY ville
HAVING COUNT(*) >= 2
ORDER BY nb_coureurs DESC;
```


## Question 20 : Créer trois colonnes booléennes qui disent si un coureur est Junior, Senior ou Veteran. Faire la requête de deux manières différentes.
```sql
SELECT 
    nom_complet,
    CASE WHEN categorie LIKE 'Junior%'
        THEN TRUE
        ELSE FALSE
    END AS junior,
    CASE WHEN categorie LIKE 'Senior%'
        THEN TRUE
        ELSE FALSE
    END AS senior,
    CASE WHEN categorie LIKE 'Veteran%'
        THEN TRUE
        ELSE FALSE
    END AS veteran
FROM coureurs;
-- Ou
SELECT 
    nom_complet,
    (categorie LIKE 'Junior%') AS junior,
    (categorie LIKE 'Senior%') AS senior,
    (categorie LIKE 'Veteran%') AS veteran
FROM coureurs;
```


## Question 21 : Donner le total d'inscrits pour chaque catégorie d'âge (Junior, Senior ou Veteran).
```sql
SELECT 
    CASE 
        WHEN categorie LIKE 'Junior%'  THEN 'Junior'
        WHEN categorie LIKE 'Senior%'  THEN 'Senior'
        WHEN categorie LIKE 'Veteran%' THEN 'Veteran'
    END AS "catégorie d'âge",
    COUNT(*) AS "total d'inscrits"
FROM coureurs
GROUP BY "catégorie d'âge";
```
