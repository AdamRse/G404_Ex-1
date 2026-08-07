# Mots clefs et requêtes
### Créer une base de données
`
CREATE DATABASE <nom database>
`
### Créer une table :
`
CREATE TABLE <table> (
  <colonne> <type> [conraintes],
  [<colonne> <type> [conraintes]]
  [contraintes]
)
`
- On peut créer une table à partir d'une table existante avec `AS`
`
CREATE TABLE AS <table>
  SELECT <colonnes> FROM <table> --Sélectionner les colonnes et données à importer
`
### Clé primaire
- Pour avoir auto increment et unique et not null :
`<colonne> <type> GENERATED ALWAYS AS IDENTITY PRIMARY KEY`
- ! `AUTO_INCREMENT` n'existe pas en postgre, `SERIAL` est utilisé à la place, mais deprecated
### Clé étrangère
`
CREATE TABLE <table> (
  ...
  <colonne> <type> REFERENCES <table_reference>(<colonne_reference>)
)
`
`
CONSTRAINT <nom contrainte>
    FOREIGN KEY <table_clé_étrangère>(<colonne_clé_étrangère>)
    REFERENCES <table_primaire>(<clé_primaire>)
`
### Modifier une table
`
ALTER TABLE <table>
  <instructions>
`
- Exemples :
`
ALTER TABLE <table> ADD COLUMN <colonne> <type>
ALTER TABLE <table> ALTER COLUMN <colonne> TYPE <nouveau type>
ALTER TABLE <table> ALTER COLUMN <colonne> ADD GENERATED ALWAYS AS IDENTITY
ALTER TABLE <table> ALTER COLUMN <colonne> DROP IDENTITY
ALTER TABLE <table> DROP COLUMN <colonne>
ALTER TABLE <table> ADD CONSTRAINT ...
ALTER TABLE <table> DROP CONSTRAINT ...
ALTER TABLE <table> RENAME TO <nouveau nom table>
ALTER TABLE <table> RENAME COLUMN <colonne> TO <nouveau nom colonne>
`
### Ajouter les données d'une autre table
`
INSERT INTO <table1>(<liste colonnes>)
SELECT * FROM <table2> [WHERE ...]
`
### Supression
- Supprimer une table : `DROP TABLE <table>` :
- Supprimer des données : `DELETE FROM <table> [WHERE <condition>]`
- Reset d'une table (sans toutcher la structure) : `TRUNCATE <table>`
- Supprimer une base de données : `DROP DATABASE <database>`
### Liste de mot clés
- `DEFAULT <valeur par défaut>` : Donne une valeur par défaut
- `NULL` ou `NOT NULL` : Précise s'il est possible de laisser le champ vide (`NULL` par défaut)
- `UNIQUE` : Une seule occurence par colonne
- `CURRENT_DATE` ou `CURRENT_TIMESTAMP` : Date ou datetime
### Fonctions
- `date_part(<selection>, <date>)` : Donne une partie péécise de la date
  - Exemple : `date_part('year', CURRENT_DATE)`
# Notes cours
- Sélectionner la ligne avec le max de col1 :
  - `SELECT * FROM table WHERE col1 = (SELECT MAX(col1) FROM table)`
- `LIMIT 5 OFFSET 2` de postgre = `LIMIT 5, 2` de mysql
- Ordre d'execution SQL : `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`
  - Le `GROUP BY `n'a pas accès aux tables dans `FROM`, seulement à ce que prend le `SELECT`
- `HAVING` est SIMILAIRE a `WHERE` mais executé après le `GROUP BY` ce qui lui donne la possibilité d'utiliser les fonction d'aggrégation (`COUNT`, `AVG`, etc...)
- `AS "<Nouvelle Table>"` : Les `"` Doivent être utilisés dans l'`ORDER BY` aussi. On peut utiliser le `AS` sans `"`, tout en minuscule.
- Affichage des valeurs avec `ORDER BY` : On ne peut `SELECT` une colonne qui a plusieurs valeurs pour un groupe. Il faut utiliser une fonction d'aggrégation (`SUM()`, `AVG()`, `COUNT()`, etc...)
- Les `'` dans les tring ne s'échappent *pas* avec un `\`. Il faut utiliser `''`
  - Par exemple : `'L'orloge'` s'échappe comme : `'L''horloge'`
# Commandes
### Exporter une base de données
- Exporter une base de données entière, structure + données :  
`docker exec -e PGPASSWORD=<mot de passe> -t <nom conteneur> pg_dump -U admin -d <nom base de données> --no-owner --no-privileges > <nom fichier output>.sql`
- Exporter une base de données (structure seule)
`docker exec -e PGPASSWORD=<mot de passe> -t <nom conteneur> pg_dump -U admin -d <nom base de données> --schema-only --no-owner --no-privileges > <nom fichier output>.sql`
- Exporter une base de données (données seules) :
`docker exec -e PGPASSWORD=<mot de passe> -t <nom conteneur> pg_dump -U admin -d <nom base de données> --data-only --no-owner --no-privileges > <nom fichier output>.sql`
- Exporter une table, structure + données :  
`docker exec -e PGPASSWORD=<mot de passe> -t <nom conteneur> pg_dump -U admin -d <nom base de données> -t <nom table> --no-owner --no-privileges > <nom fichier output>.sql`
### A executer dans ce répertoire
Executer une commande SQL
	`docker exec -it postgres-local psql -U admin -d <base de données>`
Executer un script
	`docker exec -i postgres-local psql -U admin -d <base de données> < <script.sql>`
Executer le test
  `docker exec -i postgres-local psql -U admin -d testdb < test.sql`

# Se connecter aux bases de données
Exercice 2
  - `docker exec -it postgres-local psql -U admin -d jeux_de_societe`
  - `docker exec -e PGPASSWORD=monmotdepasse -t postgres-local pg_dump -U admin -d testdb -t jeux_de_societe --no-owner --no-privileges > jeux_de_societe.sql`

# Attention !!
- Strings : Avec PostgreSQL les strings ne fontctionnent qu'avec les `'`. Les `"` sont utilisées dans la requête, pour renommer une colonne avec `AS` par exemple.
  - Si on utlise `AS "Nouvelle colonne"`, alors il faudra lutiliser dans toute la requête : `ORDER BY "Nouvelle colonne"`.
  - Sans les `"`, les colonnes sont mises en miniscules
- `IS` considère que une valeur `NULL` est `FALSE`, c'est la différence avec `=`
