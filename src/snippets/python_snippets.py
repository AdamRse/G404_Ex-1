import re

def word_list(texte):
    wordList = []
    if isinstance(texte, str):
        text_split = re.split(r"[,\s;.)(:?+\[\]!{}=#]+", texte)
        for word in text_split:
            if word != "":
                wordList.append(word)
    return wordList
