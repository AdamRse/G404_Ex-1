"""Étape 03 : décrire la durée de résolution dans chaque canal."""

import pandas as pd

from chemins_projet import CSV_NETTOYE, CSV_RESUME, creer_dossiers_sortie


def decrire_par_groupe(tickets_nettoyes):
    """Renvoyer une ligne par canal.

    Colonnes : channel, nombre, moyenne, mediane, ecart_type,
    q1, q3, minimum, maximum.

    À FAIRE : sélectionner un canal, calculer ses statistiques, puis répéter
    pour les autres canaux. Utiliser l'écart-type d'échantillon : std(ddof=1).
    Aide : sections 6 et 7 de ../PYTHON_SNIPPETS.md.
    """
    raise NotImplementedError("À FAIRE : décrire chaque canal séparément.")


def main():
    tickets_nettoyes = pd.read_csv(CSV_NETTOYE)
    resume = decrire_par_groupe(tickets_nettoyes)

    creer_dossiers_sortie()
    resume.to_csv(CSV_RESUME, index=False)
    print(resume.to_string(index=False))
    print(f"Sortie : {CSV_RESUME}")
    print("Contrôle : la somme des effectifs égale le nombre de lignes nettoyées.")


if __name__ == "__main__":
    main()
