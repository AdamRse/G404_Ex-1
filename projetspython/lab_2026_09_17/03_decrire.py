"""Étape 03 : décrire la durée de résolution dans chaque canal."""

import pandas as pd

from chemins_projet import CSV_NETTOYE, CSV_RESUME, creer_dossiers_sortie

COLONNES_RESUME = ["channel", "nombre", "moyenne", "mediane", "ecart_type",
                   "q1", "q3", "minimum", "maximum"]


def decrire_un_canal(nom_canal, durees):
    """Calculer les indicateurs d'un seul canal, étape explicite."""
    return {
        "channel": nom_canal,
        "nombre": int(durees.count()),
        "moyenne": durees.mean(),
        "mediane": durees.median(),
        "ecart_type": durees.std(ddof=1),  # écart-type d'échantillon
        "q1": durees.quantile(0.25),
        "q3": durees.quantile(0.75),
        "minimum": durees.min(),
        "maximum": durees.max(),
    }


def decrire_par_groupe(tickets_nettoyes):
    """Renvoyer une ligne par canal, dans l'ordre alphabétique des canaux."""
    lignes = []
    for nom_canal in sorted(tickets_nettoyes["channel"].unique()):
        durees = tickets_nettoyes.loc[tickets_nettoyes["channel"] == nom_canal,
                                      "resolution_minutes"]
        lignes.append(decrire_un_canal(nom_canal, durees))
    return pd.DataFrame(lignes, columns=COLONNES_RESUME)


def main():
    tickets_nettoyes = pd.read_csv(CSV_NETTOYE)
    resume = decrire_par_groupe(tickets_nettoyes)

    creer_dossiers_sortie()
    resume.to_csv(CSV_RESUME, index=False)
    print(resume.round(2).to_string(index=False))
    print(f"Sortie : {CSV_RESUME}")

    # Contrôle demandé par le README : effectifs cohérents.
    total = int(resume["nombre"].sum())
    attendu = len(tickets_nettoyes)
    print("Contrôle : la somme des effectifs égale le nombre de lignes nettoyées.")
    if total != attendu:
        raise ValueError(f"Effectifs incohérents : {total} != {attendu}")


if __name__ == "__main__":
    main()
