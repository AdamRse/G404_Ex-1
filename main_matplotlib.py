# Pour afficher directement dans le terminal
import matplotlib
matplotlib.use('module://pyplotsixel')
# -------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.header.head import main, printSuccess, printError, printWrong, bcolors # NOQA

df = pd.read_csv('data/pokemon_clean.csv')
print(df)


fig, axs = plt.subplots(2,2)
graph_gen = df['Generation'].value_counts().sort_index()

# Idée : ajouter visuel légendaires et mega dans un .pie() exterieur
axs[0,0].pie(
    graph_gen,
    labels=[f"gen {ng}" for ng in graph_gen.index],
    autopct=lambda pourcent: f"{round(pourcent, 2)}%\n({round(pourcent * graph_gen.sum() / 100)})"
)
axs[0,0].set_title('Distribution des générations')
# --------------

n, b, _ = axs[0,1].hist(df['Total'], bins=10, edgecolor="Black", color="skyblue")
print(n, b)
axs[0,1].set_xticks(b)
axs[0,1].tick_params(axis='x', rotation=30)
axs[0,1].hist(df['Total'], bins=100, histtype="stepfilled")
axs[0,1].set_title('Distribution stats total')
axs[0,1].set_xlabel('Stats totales')
axs[0,1].set_ylabel('Nombre de Pokémon')
axs[0,1].grid()
# --------------

attaque = df['Attack']+df['Sp. Atk']
defense = df['Defense']+df['Sp. Def']
axs[1,0].scatter(attaque, defense, alpha=0.2, color='blue', label='Pokémon')

coeffs = np.polyfit(attaque, defense, 1)  # données en abscisse, données en ordonnée, courbe recherchée (1=droite)
fct_poly = np.poly1d(coeffs) # renvoie une fct qui permet de calculer f(x) (f(x)=ax + b)
print("polyfit : ",coeffs)

atk_min_max=[min(attaque),max(attaque)]
#def_min_max=[min(defense),max(defense)]
axs[1,0].plot(atk_min_max, fct_poly(atk_min_max), color='red', label='Tendance', linestyle="dashed")

axs[1,0].set_title('Équilibrage physique')
axs[1,0].set_xlabel('Potentiel offensif')
axs[1,0].set_ylabel('Potentiel défensif')
axs[1,0].grid(True, alpha=0.6)
axs[1,0].legend()
# --------------

df['Mega']=df['Name'].str.contains(r'^mega\s.+$', case=False, na=False, regex=True)
print(df[df['Mega'] == True])
lengendaires = df.loc[df['Legendary'] == True & df['Mega'] == False, 'Total']
normaux = df.loc[df['Legendary'] == False & df['Mega'] == False, 'Total']

axs[1,1].boxplot(
    [lengendaires, normaux],
    tick_labels=['Legendaires', 'Normaux']
)
# --------------


fig.suptitle("Stats pokémon")
fig.show()
