from string import ascii_letters

def find_missing_letter(chars):
    ascii_ = list(ascii_letters)
    for i in range(len(chars)):
        if ascii_.index(chars[i])+1 != ascii_.index(chars[i+1]):
            return ascii_[ascii_.index(chars[i])+1]
        
def find_missing_letter_(chars):
    for i in range(len(chars)):
        if ord(chars[i])+1 != ord(chars[i+1]):
            return chr(1+ord(chars[i]))

def find_missing_letter2(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))

def find_missing_letter3(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
    


a = find_missing_letter_(['a','b','c','d','f'])
b = find_missing_letter2(['O','Q','R','S'])
print()
print(a)
print()
print(b)