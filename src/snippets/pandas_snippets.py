import pandas as pd
from src.snippets.python_snippets import word_list

# convertit le type des colonnes passées en gérant des exception.

# Fixe les données manquantes à 0
def convert_int(df:pd.DataFrame, liste_columns_name:list, round=False):
    df[liste_columns_name].fillna(0)
    df[liste_columns_name].round()
    df[liste_columns_name] = df[liste_columns_name].astype(int)

# Supprime les caractères non alphanumériques, gère le o = 0
def convert_float(df:pd.DataFrame, liste_columns_name:list, round=False):
    df[liste_columns_name] = df[liste_columns_name].astype(str)
    for c in liste_columns_name:
        df[c] = df[c].str.lower().str.replace('o', '0')
        df[c] = df[c].str.replace(r'[^\d.,]', '', regex=True)
    df[liste_columns_name] = df[liste_columns_name].astype(float)
    if round:
        df[liste_columns_name] = df[liste_columns_name].round()

def get_list_from_multiple_value(ser:pd.Series) ->list:
    splitted=[]
    for s_line in ser:
        split_s=word_list(s_line)
        for s in split_s:
            if s not in splitted:
                splitted.append(s)
    return splitted
