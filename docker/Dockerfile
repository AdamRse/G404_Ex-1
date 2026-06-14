# On utilise l'image officielle Python basée sur Alpine Linux (très légère)
FROM python:3.14-alpine

# On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# On copie le reste des fichiers du projet dans le conteneur
COPY . .

# Commande exécutée par défaut au démarrage du conteneur
CMD ["python", "main.py"]
