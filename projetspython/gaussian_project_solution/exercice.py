import pandas as pd
import plotly.express as px
transactions = pd.read_csv("/home/adam/dev/projets/exercice-python/projetspython/gaussian_project_solution/data/purchase_transactions.csv")

def main():
    figure = px.scatter(
        transactions,
        x="age",
        y="purchase_amount",
        color="group",
        opacity=0.4,
    )
    figure.show()
