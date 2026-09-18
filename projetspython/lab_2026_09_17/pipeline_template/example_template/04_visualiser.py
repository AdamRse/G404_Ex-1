"""Étape 04 : rendre les distributions visibles et comparables."""

import pandas as pd

from chemins_projet import (
    CSV_NETTOYE,
    HTML_BOITE,
    HTML_DISTRIBUTIONS,
    creer_dossiers_sortie,
)


def ecrire_graphiques(tickets_nettoyes):
    """Écrire deux graphiques HTML utilisables hors connexion.

    À FAIRE :
    - montrer trois histogrammes séparés de resolution_minutes, un par channel ;
    - utiliser les mêmes axes et classes de 10 minutes (bords 5, 15, 25…) ;
    - ajouter un trait par observation sous chaque histogramme (rug) ;
    - comparer centre, dispersion et observations inhabituelles ;
    - rendre les canaux et l'unité visibles, choisir des axes comparables ;
    - écrire HTML_DISTRIBUTIONS et HTML_BOITE avec include_plotlyjs=True.

    Aide : section 8 de ../PYTHON_SNIPPETS.md.
    Plotly Express et make_subplots fonctionnent avec Plotly 6 et 7.
    Facultatif après les histogrammes : une vue séparée avec densité estimée (KDE).
    Utiliser histnorm="probability density" pour comparer histogramme et KDE.
    ff.create_distplot, utilisé au cours précédent, ne fonctionne plus en 7.
    """
    raise NotImplementedError("À FAIRE : construire et enregistrer les figures.")


def main():
    tickets_nettoyes = pd.read_csv(CSV_NETTOYE)
    creer_dossiers_sortie()
    ecrire_graphiques(tickets_nettoyes)

    print(f"Vue des formes : {HTML_DISTRIBUTIONS}")
    print(f"Vue centre/dispersion : {HTML_BOITE}")
    print("Contrôle : ouvrir les deux fichiers et expliquer chaque graphique.")


if __name__ == "__main__":
    main()
