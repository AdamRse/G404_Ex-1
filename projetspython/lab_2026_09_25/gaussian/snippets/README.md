# Exemples à copier et à adapter

Ces trois scripts fonctionnent indépendamment. Utilisez leur code pour
construire votre propre projet Python selon les consignes du diaporama.

Depuis le dossier `lab/`, avec le Python du cours :

```bash
python -m pip install -r requirements.txt
python gaussian/snippets/01_draw_values.py
python gaussian/snippets/02_build_dataframe.py
python gaussian/snippets/03_plot_distributions.py
```

L'installation n'est utile que si les bibliothèques manquent.

| Script | Données utilisées | Résultat |
| --- | --- | --- |
| `01_draw_values.py` | Moyenne 0, écart-type 1, 1 000 valeurs, `seed=404` | Un tableau NumPy, avec un seul appel à `rng.normal` |
| `02_build_dataframe.py` | Liste `[1, 2, 3]` | Un dataframe avec une colonne `value` |
| `03_plot_distributions.py` | Une distribution normale, comme dans `01` | Histogramme, boîte à moustaches et courbe cumulée |

Modifiez les paramètres et adaptez ces opérations aux exigences du projet.

Le troisième script utilise le **même échantillon** pour trois graphiques :

- **Histogramme :** forme de la distribution. L'aire totale des barres vaut 1
  car l'axe vertical représente une densité.
- **Boîte à moustaches :** médiane et dispersion ; la boîte contient les 50 %
  centraux des observations.
- **Courbe cumulée :** pour chaque valeur, proportion des observations
  inférieures ou égales à cette valeur.

La courbe cumulée est un exemple supplémentaire, pas une nouvelle exigence du projet.
