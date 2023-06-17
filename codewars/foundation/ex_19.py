import string

def to_jaden_case(s):
    return ' '.join(string.capwords(word) for word in s.split(' '))

def to_jaden_case2(s):
    return string.capwords(s)



quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case2(quote))