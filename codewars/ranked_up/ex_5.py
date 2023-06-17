import re

txt = "abcde"
def solution(s):
    lst = []
    if s == '':
        return []

    for i in range(0, len(s)):
        word = s[i:i+2]
        lst.append(word)
        i = i + 3
    j = lst
    b = j[::2]
    
    if len(b[-1]) == 1:
        b[-1] = b[-1] + '_'
    return b 

def solution2(s):
    return re.findall(".{2}", s + "_")

def solution3(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

def solution4(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

print(solution2(txt))
