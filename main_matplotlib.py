# Pour afficher directement dans le terminal
import matplotlib
matplotlib.use('module://pyplotsixel')
# -------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.snippets.pandas_snippets import convert_column_int, convert_column_float, get_list_from_multiple_value, get_list_from_column
from src.header.head import main, printSuccess, printError, printWrong, bcolors # NOQA

df = pd.read_csv('data/pokemon_clean.csv')
print(df)

fig, axs = plt.subplots(2,2)
graph_gen = df['Generation'].value_counts().sort_index()

axs[0,0].pie(
    graph_gen,
    labels=[f"gen {ng}" for ng in graph_gen.index],
    autopct=lambda pourcent: f"{round(pourcent * graph_gen.sum() / 100)}\n({pourcent}%)"
)
axs[0,0].pie(
    graph_gen,
    labels=[f"gen {ng}" for ng in graph_gen.index],
    autopct=lambda pourcent: f"{round(pourcent * graph_gen.sum() / 100)}\n({pourcent}%)"
)
axs[0,0].set_title('Distribution des générations')

n, b, _ = axs[0,1].hist(df['Total'], bins=10, edgecolor="Black", color="skyblue")
print(n, b)
axs[0,1].set_xticks(b)
axs[0,1].tick_params(axis='x', rotation=30)
axs[0,1].hist(df['Total'], bins=100, histtype="stepfilled")
axs[0,1].set_title('Distribution stats total')
axs[0,1].set_xlabel('Stats totales')
axs[0,1].set_ylabel('Nombre de Pokémon')
axs[0,1].grid()

#axs[1,0].pie(df.loc[df['Legendary'] == "True", 'Generation'].value_counts(), labels=["gen 1", "gen 2", "gen 3", "gen 4", "gen 5", "gen 6"])

fig.suptitle("Stats pokémon")
fig.show()
