### Opérations d'observation générales
- `df.info()`
- `df.describe()`
### Opérations de transformation
- `df.T` : Bascule le dataFrame, chaque lignes devient une colonne
### valeur la plus récurente
- `df.value_counts("<col>").idmax()`
ou
- `df['<col>'].mode()[0]`


# Fonctions principales
- `df['<col>'].mode()` : Calcule les modes et le renvoie dans l'ordre de fréquence dans le dataset
- `df.value_counts('<col>')` : compte le nombre d'occurences de chaque valeur distincte de `<col>`
- `df.groupby('<col>')` : Regroupe les données par valeur de `<col>`, chaque groupe de valeur est prêt pour les opérations à effectuer.
  - `df.groupby('<col1>')['col2'].sum()` : chaque valeur unique de `<col1>` additionne sa valeur `<col2>`. Chaque occurence de `<col1>` aura donc un résultat de l'addition de `<col2>`
  - `df.groupby('<col1>')['col2'].agg([operations])` : Regroupe les données par valeur de `<col>` et créé une colonne par opération demmandées.
    - `df.groupby('<col1>')['col2'].agg([['sum', 'mean', 'count', 'max']])` : Donnera une colonne `'sum', 'mean', 'count', 'max'`, et les lignes correspondant aux regroupements de `<col1>`
