# Pour afficher directement dans le terminal
import matplotlib
matplotlib.use('module://pyplotsixel')
# -------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate
from src.snippets.pandas_snippets import convert_column_int, convert_column_float, get_list_from_multiple_value, get_list_from_column
from src.header.head import main, printSuccess, printError, printWrong, bcolors # NOQA

test=None
df = pd.read_csv("data/Pokemon_dataset.csv", delimiter=";")
df=df.T.set_axis(df.iloc[:,0], axis=1).drop("Unnamed: 0", axis=0)
df[df.columns[6].split(" / ")]=df[df.columns[6]].str.split(" / ", n=1, expand=True)
df=df.drop(df.columns[6], axis=1)
number_columns=['#', 'Total', 'HP', 'Speed', 'Generation', 'Attack',"Sp. Atk", "Sp. Def", 'Defense % of Attack']
convert_column_float(df, number_columns)
df = df.sort_values("#", ascending=True)
df[df[['Speed', 'Attack',"Sp. Atk", "Sp. Def", 'HP']] > 255]=np.nan
df[df[number_columns] < 1]=np.nan
df=df.dropna(axis=0, how="all")

# nettoyage de # ID
convert_column_int(df, ["#"])

# nettoyage des HP

# correction de l'Attack
stats_no_attack = ['HP', 'Speed', 'Sp. Atk', 'Sp. Def']
missing_atk=((df['Total'] - df[stats_no_attack].sum(axis=1)) / (1+df['Defense % of Attack']/100)).round()
df['Attack']=df['Attack'].fillna(missing_atk)

# nettoyage Name
df["Name"] = df["Name"].str.lower()
df["Name"] = df["Name"].str.replace(".+mega ", "mega " ,regex=True)
df["Name"] = df["Name"].str.title()

# création colonne défense
df['Defense'] = ((df['Attack'] * df['Defense % of Attack']) / 100).round()
#df=df.drop("Defense % of Attack", axis=1)
convert_column_float(df, ["Defense"])

# nettoyage Generation
df["Generation"]=df["Generation"].replace(0, np.nan)
df["Generation"]=df["Generation"].bfill()
convert_column_int(df, ["Generation"])

# nettoyage Types
df["Types"] = df["Types"].str.replace(r",\s*$", "" ,regex=True)
types=get_list_from_multiple_value(df["Types"])

# nettoyage stats
stats_col = ['HP', 'Speed', 'Attack', 'Sp. Atk', 'Sp. Def', 'Defense']
is_calculable = df[stats_col].isna().sum(axis=1) < 2
diff = df['Total'] - df[stats_col].sum(axis=1)
for col in stats_col:
    condition = is_calculable & df[col].isna()
    df.loc[condition, col] = diff[condition]

# fix les sommes
is_calculable = df[stats_col].isna().sum(axis=1) == 0
df.loc[is_calculable, "Total"]=df[stats_col].sum(axis=1)

# fix les double NaN dans les stats
missing_double= df[stats_col].isna().sum(axis=1)
for col in stats_col:
    df.loc[missing_double >= 2, col] = round(diff[missing_double >= 2]/missing_double)

df=df[["#", "Name", "Types", "Generation", "Legendary", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]]


fig, axs = plt.subplots(2,2)
axs[0,0].pie(df['Generation'].value_counts().sort_index(), labels=["gen 1", "gen 2", "gen 3", "gen 4", "gen 5", "gen 6"])
axs[0,0].set_title('Distribution des générations')

axs[0,1].hist(df['Total'], bins=10, histtype="bar", edgecolor="Black")
axs[0,1].hist(df['Total'], bins=200, histtype="stepfilled")
axs[0,1].set_title('Distribution stats total')
axs[0,1].set_xlabel('Stats totales')
axs[0,1].set_ylabel('Nombre de Pokémon')

print(df.loc[df['Legendary'] == "True", ['Legendary', "Generation"]])
axs[1,0].pie(df.loc[df['Legendary'] == "True", 'Generation'].value_counts(), labels=["gen 1", "gen 2", "gen 3", "gen 4", "gen 5", "gen 6"])

fig.suptitle("Stats pokémon")
fig.show()
