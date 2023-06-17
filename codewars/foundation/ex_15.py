import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

def disemvowel2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel3(string):
    vowels = 'aAeEiIoOuU' 
    string = [vowel for vowel in string if vowel not in vowels]
    return "".join(string)


print(disemvowel('asdfghrtdgsrfhbqarfe'))