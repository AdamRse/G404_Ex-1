def is_match(s: str, p: str) -> bool:
    string_len=len(s)
    pattern_len=len(p)
    def match(index_string: int, index_pattern: int) -> bool:
        if index_pattern == pattern_len:
            return index_string == string_len

        first_match = index_string < string_len and (p[index_pattern] == '.' or p[index_pattern] == s[index_string])

        if index_pattern + 1 < pattern_len and p[index_pattern + 1] == '*':
            return match(index_string, index_pattern + 2) or (first_match and match(index_string + 1, index_pattern))
        else:
            # Simple pattern, 1 char = 1 p
            return first_match and match(index_string + 1, index_pattern + 1)
    return match(0, 0)

test_cases = {
    "s" : ["aa", "aa", "ab", "aab", "ab", "aaa", "a", "mississippi", "bbbba", "ab", "bb", "bbab", "abbabaaaaaaacaa", "bcbabcaacacbcabac"],
    "p" : ["a", "a*", ".*", "c*a*b", ".*c", "a*a", "ab*", "mis*is*p*.", ".*a*a", ".*..c*", ".bab", "b*a*", "a*.*b.a.*c*b*a*c*", "a*c*a*b*.*aa*c*a*a*"],
    "expected_answer" : [False, True, True, True, False, True, True, False, True, True, False, False, True, True]
    }
errors=False
for i in range(len(test_cases["s"])):
    result=is_match(test_cases["s"][i], test_cases["p"][i])
    if result == test_cases["expected_answer"][i]:
        print("Pattern "+test_cases["p"][i]+" (string : '"+test_cases["s"][i]+"') correct !")
    else:
        errors="Erreur sur le pattern "+test_cases["p"][i]+" (string : '"+test_cases["s"][i]+"'), renvoie "+str(result)+" au lieu de "+str(test_cases["expected_answer"][i])
        break
if errors:
    print(errors)
else:
    print("--- Les tests sont bien passés ! ---")
