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

# Fonctions principales
- `df['<col>'].mode()` : Calcule les modes et le renvoie dans l'ordre de fréquence dans le dataset
- `df.sum([axis=0|1])` : Fais la somme des colonnes (axis=0) ou des lignes (axis=1).
- `df.value_counts('<col>')` : compte le nombre d'occurences de chaque valeur distincte de `<col>`
- `df.groupby('<col>')` : Regroupe les données par valeur de `<col>`, chaque groupe de valeur est prêt pour les opérations à effectuer.
  - `df.groupby('<col1>')['col2'].sum()` : chaque valeur unique de `<col1>` additionne sa valeur `<col2>`. Chaque occurence de `<col1>` aura donc un résultat de l'addition de `<col2>`
  - `df.groupby('<col1>')['col2'].agg([operations])` : Regroupe les données par valeur de `<col>` et créé une colonne par opération demmandées.
    - `df.groupby('<col1>')['col2'].agg([['sum', 'mean', 'count', 'max']])` : Donnera une colonne `'sum', 'mean', 'count', 'max'`, et les lignes correspondant aux regroupements de `<col1>`
