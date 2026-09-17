"""Étape 05 : mesurer une fréquence observée au-delà d'un seuil."""

import pandas as pd

from chemins_projet import (
    CSV_FREQUENCES,
    CSV_NETTOYE,
    SEUIL_QUEUE_MINUTES,
    creer_dossiers_sortie,
)

COLONNES_FREQUENCES = ["channel", "seuil_minutes", "nombre_queue",
                       "effectif_groupe", "frequence_queue"]


def calculer_frequences_queue(tickets_nettoyes):
    """Une ligne par canal : proportion de tickets à 180 minutes ou plus.

    frequence_queue = nombre_queue / effectif_groupe, dans CE canal
    (jamais l'effectif du fichier entier).
    """
    lignes = []
    for canal in sorted(tickets_nettoyes["channel"].unique()):
        durees = tickets_nettoyes.loc[tickets_nettoyes["channel"] == canal,
                                      "resolution_minutes"]
        effectif_groupe = int(durees.count())
        nombre_queue = int((durees >= SEUIL_QUEUE_MINUTES).sum())
        lignes.append({
            "channel": canal,
            "seuil_minutes": SEUIL_QUEUE_MINUTES,
            "nombre_queue": nombre_queue,
            "effectif_groupe": effectif_groupe,
            "frequence_queue": nombre_queue / effectif_groupe,
        })
    return pd.DataFrame(lignes, columns=COLONNES_FREQUENCES)


def main():
    tickets_nettoyes = pd.read_csv(CSV_NETTOYE)
    frequences = calculer_frequences_queue(tickets_nettoyes)

    creer_dossiers_sortie()
    frequences.to_csv(CSV_FREQUENCES, index=False)

    # Contrôles demandés par le README.
    assert (frequences["nombre_queue"] <= frequences["effectif_groupe"]).all()
    assert frequences["frequence_queue"].between(0, 1).all()
    assert int(frequences["effectif_groupe"].sum()) == len(tickets_nettoyes)

    print(f"Seuil : {SEUIL_QUEUE_MINUTES} minutes")
    print(frequences.round(4).to_string(index=False))
    print(f"Sortie : {CSV_FREQUENCES}")
    print("Contrôle : vérifier le numérateur et le dénominateur de chaque ligne.")


if __name__ == "__main__":
    main()
