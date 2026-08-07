# Notes cours
- Sélectionner la ligne avec le max de col1 :
  - `SELECT * FROM table WHERE col1 = (SELECT MAX(col1) FROM table)`
- `LIMIT 5 OFFSET 2` de postgre = `LIMIT 5, 2` de mysql
- Ordre d'execution SQL : `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`
  - Le `GROUP BY `n'a pas accès aux tables dans `FROM`, seulement à ce que prend le `SELECT`
- `HAVING` est SIMILAIRE a `WHERE` mais executé après le `GROUP BY` ce qui lui donne la possibilité d'utiliser les fonction d'aggrégation (`COUNT`, `AVG`, etc...)
- `AS "<Nouvelle Table>"` : Les `"` Doivent être utilisés dans l'`ORDER BY` aussi. On peut utiliser le `AS` sans `"`, tout en minuscule.
- Affichage des valeurs avec `ORDER BY` : On ne peut `SELECT` une colonne qui a plusieurs valeurs pour un groupe. Il faut utiliser une fonction d'aggrégation (`SUM()`, `AVG()`, `COUNT()`, etc...)

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
