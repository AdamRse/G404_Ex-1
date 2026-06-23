from ast import pattern


def listePatterns(pattern):
    def getNextPattern(id, patternString):
        if len(patternString)-1>id:
            return patternString[id+1]
        else:
            return False
    listPatterns=[]
    for id, p in enumerate(pattern):
        next_p=getNextPattern(id, pattern)
        if next_p == "*":
            listPatterns.append(p+next_p)
        elif not p == "*":
            listPatterns.append(p)
    return listPatterns

def get_segment(patterns):
    segment=[]
    for p in patterns:
        if len(p) == 1:
            segment.append(p)
            return segment
        else:
            segment.append(p)
    return segment

def is_star_pattern(pattern):
    return len(pattern)==2

# Le segment, c'est un nombre indéterminé de patter étoile, avec un pattern single à la fin
def test_segment(segment, string):# retourne [nombre de pattern à virer,nombre de string à virer] ou false
    # récupérer le dernier segment et tester s'il est bien single
    # On n'a pas besoin de faire des hypothèses sur tout, seulement les patterns qui sont identiques au dernier pattern sigle
    for s in string:
        p=segment[0]
        while s == p[0]:

    return [1,1]

def do_regex(string, pattern):
    pattern=listePatterns(pattern)

    while pattern:
        segment_p=get_segment(pattern)
        test_segments=test_segment(segment_p, string)
        if test_segments:
            pattern=test_segments[0]
            string=test_segments[1]
        else:
            return False


do_regex("ab", "a*a")
