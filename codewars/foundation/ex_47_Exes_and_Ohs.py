from collections import Counter

def xo(s: str):
    s = s.lower()
    return s.count('x') == s.count('o')

def xo_v2(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)

print(xo('xxooXOOx'))

print(xo('ooXOx'))