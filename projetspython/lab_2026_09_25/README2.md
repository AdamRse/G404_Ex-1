# Les fichiers du cours

Deux parties indépendantes : [concevoir le projet gaussien](gaussian/README.md),
puis [lire des CSV et utiliser SQLite depuis Python](sql/README.md).

## Préparer Python

Utilisez l’environnement Python du cours. Depuis ce dossier `lab/` :

```bash
python -m pip install -r requirements.txt
```

Si votre commande est `python3`, utilisez-la à la place de `python`.
Dans VS Code, choisissez l'environnement du cours. Vérifiez le Python du terminal avec :

```bash
python -c "import sys; print(sys.executable)"
```

## Choisir l’activité

| Activité | Fichier de départ | Travail |
| --- | --- | --- |
| Projet gaussien | Exigences dans le diaporama et `gaussian/README.md` | Reprendre l'organisation de Rectangle : paquet local, classe, fonctions, lanceur et tests |
| CSV et SQL | `sql/01_create_csv.py` | Exécuter `01` à `03`, compléter les requêtes de `04`, puis lire et exécuter `05` |

Le README de chaque activité donne les fichiers attendus et les contrôles.

Pour les exemples des slides 15–25, ouvrir le
[notebook CSV](csv_examples/04_CSV_types_missing_values_FR.ipynb) et la
[fiche de référence](csv_examples/API_REFERENCE.md). Le notebook utilise cinq
tickets fictifs pour expliquer les règles de lecture reprises dans
[`sql/data_io.py`](sql/data_io.py) avec les clients et leurs commandes.

Les données client du TP SQL sont fictives. L’après-midi est consacré au CV
et au profil LinkedIn.
