def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))




s = 'qwerty'
for i, c in enumerate(s):
    print(f'i: {c.upper()}, c: {c.lower() * i}')