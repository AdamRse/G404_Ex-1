# Notes cours
- Sélectionner la ligne avec le max de col1 :
  - `SELECT * FROM table WHERE col1 = (SELECT MAX(col1) FROM table)`
- `LIMIT 5 OFFSET 2` de postgre = `LIMIT 5, 2` de mysql

# Commandes
### A executer dans ce répertoire
Executer une commande SQL
	docker exec -it postgres-local psql -U admin -d <base de données>
Executer un script
	docker exec -i postgres-local psql -U admin -d <base de données> < <script.sql>
Executer le test
  docker exec -i postgres-local psql -U admin -d testdb < test.sql
