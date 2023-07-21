import string

def is_pangram(s):
    return set(s.lower()) >= set(string.ascii_lowercase)

def is_pangram_v2(s):
    return set(string.ascii_lowercase).issubset(s.lower())

print(is_pangram('The quick, brown fox jumps over the lazy dog!'))