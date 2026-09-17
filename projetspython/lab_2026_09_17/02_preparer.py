"""Étape 02 : appliquer et tracer vos décisions de qualité."""

import pandas as pd

from chemins_projet import (
    CSV_BRUT,
    CSV_JOURNAL_QUALITE,
    CSV_NETTOYE,
    creer_dossiers_sortie,
)


def preparer_tickets(donnees_brutes):
    """Renvoyer deux tableaux : tickets_nettoyes, journal_qualite.

    CSV nettoyé : ticket_id, channel, resolution_minutes.
    Journal : ligne_source, ticket_id, regle, decision, justification.

    À FAIRE :
    1. Travailler sur une copie et repérer les lignes du CSV source.
    2. Examiner les identifiants répétés avant de décider quoi conserver.
    3. Justifier les corrections de modalités de channel.
    4. Convertir resolution_minutes en nombres et vérifier leur validité.
    5. Documenter chaque correction, exclusion et valeur signalée conservée.
    6. Renvoyer les deux tableaux, en conservant les valeurs rares plausibles.

    Aide : sections 2 à 5 de ../PYTHON_SNIPPETS.md.
    """
    raise NotImplementedError("À FAIRE : écrire vos règles de préparation.")


def main():
    donnees_brutes = pd.read_csv(CSV_BRUT, dtype="string", keep_default_na=False)
    tickets_nettoyes, journal_qualite = preparer_tickets(donnees_brutes)

    creer_dossiers_sortie()
    tickets_nettoyes.to_csv(CSV_NETTOYE, index=False)
    journal_qualite.to_csv(CSV_JOURNAL_QUALITE, index=False)

    print(f"Lignes brutes : {len(donnees_brutes)}")
    print(f"Lignes analysables : {len(tickets_nettoyes)}")
    print(f"Données nettoyées : {CSV_NETTOYE}")
    print(f"Journal : {CSV_JOURNAL_QUALITE}")
    print("Contrôle : justifier chaque ligne retirée à l'aide du journal.")


if __name__ == "__main__":
    main()
