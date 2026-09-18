# Environnement d'exécution du pipeline (aucun code projet copié : le dossier
# courant est monté en volume par docker-compose.yml au moment de l'exécution).

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dépendances figées pour la reproductibilité (voir requirements.txt).
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["python", "main.py"]
