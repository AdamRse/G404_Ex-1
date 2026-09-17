### Présentation
- Pour valider un changement dans le dataframe, il faut utiliser `df=`.
  - Par exemple `df['<col>']=df['<col>'].str.title()`
#### Types
- `pd.DataFrame()` : *Dataframe* avec un *index* (0, 1, 2, ...) et des noms de *colonnes* (<col1>, <col2>, ...) qui ne font pas partie des données qui seront calculées par les opérateurs. Ce sont des outils qui permettent la sélection.
- `pd.Series()` : *Série* avec un index, la Série n'a qu'une suele colonne.
- `df[['<col>']]` renvoie un dataframe, tandis que `df['<col>']` revoie une série.
### Opérations d'observation générales
- `df = pd.read_csv("dataset.csv")`
- `df.info()`
- `df.describe()`
### Opérations de transformation
- `df.T` : Bascule le dataFrame, chaque lignes devient une colonne
### valeur la plus récurente
- `df.value_counts("<col>").idmax()`
ou
- `df['<col>'].mode()[0]`
### Sélection
- `df[['col1' [, 'col2'] ]]` : sélection des colonnes en, utilisant une liste contenant les noms de colonne. Si une seule colonne est sélectionnées avec une liste, renvoie un dataframe, contrairement à l'exemple suivant :
- `df['col']` : renvoie une colonne sous forme de série (pd.Series)
- `df.loc['<masque ligne>'[, nom colone]]` : `<masque ligne>` peut être l'acumulation de plusieurs masques, doit utiliser `&` ou `|` et mettre les masques *entre parenthèses*. Par exemple : `df.loc[(df['col1']==True) & (df['col2']<3)]`
- `df.loc[n1:n2]` : Affiche uniquement les lignes `n1` à `n2`
### Opération multiples par colonnes (séries)
- `df['<col1']=df['<col2>']+df['<col3>']` : Les séries s'aditionnent ligne par ligne automatiquement (les Séries doivent être de taille similaire)
### Gestion des NaN
- `df.fillna(df2)` : Comble les données de df avec les données de df2 dans la même position. Les dataframes doivent être similaires. Attention, `fillna()` ne fait rien s'il est utilisé avec un dataframe et une série !
- `df['<col>'].isna()` : Retourne un masque de booléens, avec True quand la valeur est NaN
  - `df['<col>'].isna().sum()` : On peut ainsi compter les NaN dans une série
- `df.dropna()` : enlève les lignes ou colonnes avec des NaN.
  - `df.dropna(axis=0, how="all")` : Supprime les lignes qui ne comportent que des NaN
### Strings (Séries)
- `df["<col>"].str.replace("A", "B")` : remplace A par B
  - Regex : `df["<col>"].str.replace("pattern ", "remplacement" ,regex=True)`
# Fonctions principales
- `df['<col>'].mode()` : Calcule les modes et le renvoie dans l'ordre de fréquence dans le dataset
- `df.sum([axis=0|1])` : Fais la somme des colonnes (axis=0) ou des lignes (axis=1).
  - Par défaut ignore les `NaN`, si `sum()` est utilisé sur un masque, alors contera le nombre de `True`
- `df.value_counts('<col>')` : compte le nombre d'occurences de chaque valeur distincte de `<col>`
- `df.head(<nb>)` et `df.tail(<nb>)` : sélectionne `<nb>` premières et dernières lignes.
- `df.drop("<col>", axis=1)` : suprimme une colonnes.
- `df.mean()` et `df.median()` : Faire la moyenne/médiane, par ligne ou colonnes avec `axis=0|1`
- `df.groupby('<col>')` : Regroupe les données par valeur de `<col>`, chaque groupe de valeur est prêt pour les opérations à effectuer.
  - `df.groupby('<col1>')['col2'].sum()` : chaque valeur unique de `<col1>` additionne sa valeur `<col2>`. Chaque occurence de `<col1>` aura donc un résultat de l'addition de `<col2>`
  - `df.groupby('<col1>')['col2'].agg([operations])` : Regroupe les données par valeur de `<col>` et créé une colonne par opération demmandées.
    - `df.groupby('<col1>')['col2'].agg([['sum', 'std', 'mean', 'count', 'max', 'size']])` : Donnera une colonne `'sum', 'std' 'mean', 'count', 'max', 'size'`, et les lignes correspondant aux regroupements de `<col1>`
