import re

def break_camel_case_v2(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

def break_camel_case(s):
    words = []
    current_word = ''
    for char in s:
        if char.isupper() and current_word != '':
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    words.append(current_word)
    return ' '.join(words)

# Test cases
print(break_camel_case("camelCasing"))  # Output: "camel Casing"
print(break_camel_case("identifier"))   # Output: "identifier"
print(break_camel_case(""))             # Output: ""
