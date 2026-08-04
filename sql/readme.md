Executer une commande SQL
	docker exec -it postgres-local psql -U admin -d <base de données>
Executer un script
	docker exec -i postgres-local psql -U admin -d <base de données> < <script.sql>
