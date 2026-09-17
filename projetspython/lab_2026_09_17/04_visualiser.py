"""Étape 04 : rendre les distributions visibles et comparables.

Deux figures HTML autonomes (include_plotlyjs=True, lisibles hors connexion) :

1. ``distributions_temps_resolution.html`` : trois histogrammes séparés de
   ``resolution_minutes``, un panneau par canal. Les trois panneaux partagent
   les mêmes axes et utilisent des classes de 10 minutes décalées (bords 5,
   15, 25, …). Un trait (rug) par observation est tracé sous chaque
   histogramme ; les observations inhabituelles (même règle robuste que
   l'étape 02 : durée nulle ou > Q3 + 3 x IQR, calculé par canal) sont
   distinguées par la couleur.

2. ``boite_temps_resolution.html`` : boîtes à moustaches par canal pour
   comparer médianes, dispersions (IQR, moustaches) et valeurs atypiques.

Justification des classes : largeur 10 minutes = compromis entre lisibilité
et détail ; bords décalés de 5 (5, 15, 25, …) pour éviter qu'une valeur ronde
comme 10 ou 20 tombe exactement sur une frontière de classe.

Note technique : avec ``shared_xaxes=True``, Plotly ne crée pas de propriétés
``xaxis2``/``xaxis3`` dans le layout (un seul axe x partagé). On manipule
donc les axes via ``update_xaxes``/``update_yaxes`` (référencement par
ligne/colonne), jamais par accès direct au layout.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from chemins_projet import (
    CANAUX_ATTENDUS,
    CSV_NETTOYE,
    HTML_BOITE,
    HTML_DISTRIBUTIONS,
    creer_dossiers_sortie,
)

LARGEUR_CLASSE = 10
DEBUT_CLASSES = 5  # bords 5, 15, 25, …
TITRE_COMMON = "Durée de résolution des tickets par canal (minutes)"


def nom_axe_annotation(lettre, position):
    """Nom d'axe pour une annotation : x, y (panneau 1) ; x2, y2, … ensuite.

    Plotly n'accepte pas 'x1' : le premier axe s'appelle 'x'.
    """
    return lettre if position == 1 else f"{lettre}{position}"


def est_inhabituelle(durees):
    """Même règle robuste que l'étape 02, appliquée à un ensemble de durées."""
    q1, q3 = durees.quantile([0.25, 0.75])
    return (durees == 0) | (durees > q3 + 3 * (q3 - q1))


def ecrire_histogrammes(tickets_nettoyes):
    """Figure 1 : trois histogrammes séparés, mêmes axes, rug en dessous."""
    canaux = [c for c in CANAUX_ATTENDUS if c in set(tickets_nettoyes["channel"])]
    xmax = tickets_nettoyes["resolution_minutes"].max()
    fin_classes = DEBUT_CLASSES + LARGEUR_CLASSE * (
        1 + int((xmax - DEBUT_CLASSES) // LARGEUR_CLASSE)
    )

    figure = make_subplots(
        rows=len(canaux), cols=1, shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=[f"Canal : {canal}" for canal in canaux],
    )

    for position, canal in enumerate(canaux, start=1):
        durees = tickets_nettoyes.loc[tickets_nettoyes["channel"] == canal,
                                      "resolution_minutes"]
        figure.add_trace(
            go.Histogram(
                x=durees,
                xbins=dict(start=DEBUT_CLASSES, end=fin_classes, size=LARGEUR_CLASSE),
                marker_line_color="white", marker_line_width=1,
                name=f"{canal} (n={len(durees)})",
                showlegend=False,
            ),
            row=position, col=1,
        )

        # Rug : un trait par observation sous l'histogramme.
        inhabituelles = est_inhabituelle(durees)
        couleurs = ["#d62728" if flag else "#1f77b4" for flag in inhabituelles]
        figure.add_trace(
            go.Scatter(
                x=durees, y=[0] * len(durees),
                mode="markers",
                marker=dict(color=couleurs, symbol="line-ns-open", size=12,
                            line=dict(width=2)),
                name="observations", showlegend=False,
            ),
            row=position, col=1,
        )
        figure.add_annotation(
            text=f"Observations inhabituelles (rouge) : {int(inhabituelles.sum())}",
            xref=f"{nom_axe_annotation('x', position)} domain",
            yref=f"{nom_axe_annotation('y', position)} domain",
            x=0.99, y=0.95, showarrow=False, align="right",
            font=dict(size=11, color="#d62728"),
        )

    figure.update_layout(
        title_text=f"{TITRE_COMMON}<br>"
                   f"<sup>Classes de {LARGEUR_CLASSE} minutes (bords {DEBUT_CLASSES}, "
                   f"{DEBUT_CLASSES + LARGEUR_CLASSE}, "
                   f"{DEBUT_CLASSES + 2 * LARGEUR_CLASSE}, …) — axe commun, "
                   f"un trait par observation en dessous de chaque panneau</sup>",
        height=280 * len(canaux),
    )
    # Titres d'axes via les méthodes dédiées (compatible axes partagés).
    figure.update_xaxes(title_text="Durée de résolution (minutes)")
    figure.update_yaxes(title_text="Nombre de tickets")
    figure.write_html(HTML_DISTRIBUTIONS, include_plotlyjs=True)


def ecrire_boites(tickets_nettoyes):
    """Figure 2 : boîtes à moustaches pour comparer centres et dispersions."""
    figure = px.box(
        tickets_nettoyes,
        x="channel", y="resolution_minutes",
        category_orders={"channel": CANAUX_ATTENDUS},
        points="outliers",
        color="channel",
        color_discrete_sequence=px.colors.qualitative.Set2,
        labels={"channel": "Canal de contact",
                "resolution_minutes": "Durée de résolution (minutes)"},
        title=f"{TITRE_COMMON}<br>"
              f"<sup>Ligne centrale = médiane, boîte = Q1–Q3 (50 % centraux), "
              f"moustaches = 1,5 x IQR, points = observations atypiques</sup>",
    )
    figure.update_layout(showlegend=False,
                         yaxis_title="Durée de résolution (minutes)")
    figure.write_html(HTML_BOITE, include_plotlyjs=True)


def ecrire_graphiques(tickets_nettoyes):
    """Écrire les deux graphiques HTML utilisables hors connexion."""
    ecrire_histogrammes(tickets_nettoyes)
    ecrire_boites(tickets_nettoyes)


def main():
    tickets_nettoyes = pd.read_csv(CSV_NETTOYE)
    creer_dossiers_sortie()
    ecrire_graphiques(tickets_nettoyes)

    print(f"Vue des formes : {HTML_DISTRIBUTIONS}")
    print(f"Vue centre/dispersion : {HTML_BOITE}")
    print("Contrôle : ouvrir les deux fichiers et expliquer chaque graphique.")


if __name__ == "__main__":
    main()
