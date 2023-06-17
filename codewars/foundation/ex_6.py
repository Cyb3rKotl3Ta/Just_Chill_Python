def get_initials(name):

    names = name.split(' ')
    return ''.join([f"{n[0]}." for n in names])[:-1]

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

def abbrevName2(name):
    return '.'.join(filter(str.isupper,name.title()))

print(get_initials('John Doe'))
print(abbrevName2('John Doe'))