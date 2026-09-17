"""Étape 02 : appliquer et tracer vos décisions de qualité.

Décisions écrites avant de programmer
-------------------------------------
1. Unité d'observation : un ticket. Le CSV brut n'est jamais modifié.
2. ``ligne_source`` = numéro de ligne dans le CSV brut, en-tête compté comme
   ligne 1, créé avant tout tri ou filtre.
3. Identifiants :
   - identifiant vide -> exclusion (une ligne non identifiable n'est pas traçable) ;
   - identifiant répété, lignes strictement identiques -> la première occurrence
     est conservée, les doublons exacts exclus ;
   - identifiant répété, lignes contradictoires -> toutes les occurrences
     exclues : sans source complémentaire, aucune version n'est préférable.
4. Canal : normalisation (espaces, casse, accents, tirets) puis recodage
   évident vers {phone, chat, email}. Canal vide ou inconnu -> exclusion.
5. Durées : vide ou non numérique -> exclusion ; strictement négative ->
   exclusion. Durée nulle ou > Q3 + 3 x IQR -> conservée mais signalée
   (rare n'est pas impossible).
"""

import unicodedata

import pandas as pd

from chemins_projet import (
    CANAUX_ATTENDUS,
    CSV_BRUT,
    CSV_JOURNAL_QUALITE,
    CSV_NETTOYE,
    creer_dossiers_sortie,
)

COLONNES_JOURNAL = ["ligne_source", "ticket_id", "regle", "decision", "justification"]

RECODE_CANAUX = {
    "phone": "phone",
    "telephone": "phone",
    "chat": "chat",
    "email": "email",
    "mail": "email",
}


def normaliser_texte(valeur):
    """Minuscules, sans accents, sans espaces ni tirets autour."""
    texte = unicodedata.normalize("NFKD", str(valeur))
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    return texte.strip().lower().replace("-", "").replace(" ", "")


def tracer(journal, lignes, regle, decision, justification):
    """Ajouter une entrée par ligne concernée, avec le repère ligne_source."""
    for _, ligne in lignes.iterrows():
        journal.append({
            "ligne_source": int(ligne["ligne_source"]),
            "ticket_id": ligne["ticket_id"],
            "regle": regle,
            "decision": decision,
            "justification": justification,
        })


def preparer_tickets(donnees_brutes):
    """Renvoyer deux tableaux : tickets_nettoyes, journal_qualite."""
    # 1. Copie de travail + repère de traçabilité créé avant tout tri/filtre.
    donnees = donnees_brutes.copy()
    donnees["ligne_source"] = donnees.index + 2  # en-tête = ligne 1

    donnees["duree_numerique"] = pd.to_numeric(
        donnees["resolution_minutes"].str.strip(), errors="coerce"
    )
    donnees["canal_normalise"] = donnees["channel"].map(normaliser_texte)
    donnees["canal_recode"] = donnees["canal_normalise"].map(RECODE_CANAUX)

    journal = []

    # 2. Identifiant vide -> exclusion.
    masque = donnees["ticket_id"].str.strip() == ""
    tracer(journal, donnees.loc[masque], "identifiant_vide", "exclu",
           "Ticket non identifiable : impossible à tracer et à dédoublonner.")
    donnees = donnees.loc[~masque]

    # 3. Identifiants répétés.
    est_repete = donnees.duplicated(subset="ticket_id", keep=False)
    for ticket_id, groupe in donnees.loc[est_repete].groupby("ticket_id"):
        versions = groupe.drop_duplicates(subset=["channel", "resolution_minutes"])
        if len(versions) == 1:
            conserver = groupe.head(1)
            exclure = groupe.iloc[1:]
            tracer(journal, exclure, "doublon_exact", "exclu",
                   "Même ticket enregistré plusieurs fois : une seule occurrence "
                   "conservée (première apparition).")
            donnees = pd.concat([donnees.drop(index=groupe.index), conserver])
        else:
            tracer(journal, groupe, "identifiant_contradictoire", "exclu",
                   "Deux enregistrements différents portent le même ticket_id ; "
                   "aucune version n'est vérifiable : toutes sont exclues.")
            donnees = donnees.drop(index=groupe.index)

    # 4. Canal invalide -> exclusion ; correction évidente -> tracée.
    masque_valide = donnees["canal_recode"].isin(CANAUX_ATTENDUS)
    tracer(journal, donnees.loc[~masque_valide], "canal_invalide", "exclu",
           "Canal vide ou inconnu après normalisation : groupe indéterminé, "
           "la comparaison par canal n'aurait pas de sens.")
    donnees = donnees.loc[masque_valide].copy()

    corriges = donnees["canal_normalise"] != donnees["canal_recode"]
    tracer(journal, donnees.loc[corriges], "canal_recoded", "corrige",
           "Variante d'écriture d'un canal attendu (casse, accents, tirets) : "
           "recodage sans ambiguïté.")

    # 5. Durées invalides -> exclusion.
    masque_vide = donnees["resolution_minutes"].str.strip() == ""
    tracer(journal, donnees.loc[masque_vide], "duree_vide", "exclu",
           "Durée manquante : la valeur ne peut pas être estimée sans hypothèse "
           "arbitraire.")
    donnees = donnees.loc[~masque_vide]

    masque_non_numerique = donnees["duree_numerique"].isna()
    tracer(journal, donnees.loc[masque_non_numerique], "duree_non_numerique", "exclu",
           "Durée illisible (non numérique) : conversion impossible.")
    donnees = donnees.loc[~masque_non_numerique]

    masque_negative = donnees["duree_numerique"] < 0
    tracer(journal, donnees.loc[masque_negative], "duree_negative", "exclu",
           "Une durée de résolution ne peut pas être négative : valeur incohérente.")
    donnees = donnees.loc[~masque_negative].copy()

    # 6. Valeurs rares plausibles -> conservées mais signalées.
    q1, q3 = donnees["duree_numerique"].quantile([0.25, 0.75])
    borne_haute = q3 + 3 * (q3 - q1)
    est_zero = donnees["duree_numerique"] == 0
    est_extreme = donnees["duree_numerique"] > borne_haute
    tracer(journal, donnees.loc[est_zero], "observation_inhabituelle",
           "conserve_signale",
           "Durée nulle : plausible (résolution immédiate) mais à vérifier "
           "auprès de la responsable support.")
    tracer(journal, donnees.loc[est_extreme], "observation_inhabituelle",
           "conserve_signale",
           "Durée très au-dessus de Q3 + 3 x IQR : rare mais pas impossible ; "
           "conservée pour ne pas biaiser les estimations, à investiguer.")

    # 7. Tableaux de sortie, colonnes et ordre contractuels.
    tickets_nettoyes = pd.DataFrame({
        "ticket_id": donnees["ticket_id"],
        "channel": donnees["canal_recode"],
        "resolution_minutes": donnees["duree_numerique"],
    }).reset_index(drop=True)

    journal_qualite = pd.DataFrame(journal, columns=COLONNES_JOURNAL)
    journal_qualite = journal_qualite.sort_values("ligne_source").reset_index(drop=True)

    return tickets_nettoyes, journal_qualite


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
