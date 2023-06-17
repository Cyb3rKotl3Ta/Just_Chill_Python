def wave(people):
    return [people[:i] + people[i:].capitalize() for i in range(len(people)) if people[i].isalpha()]


#if register is upper
def wave2(people):
    return [people[:i].lower() + people[i:].capitalize() for i in range(len(people)) if people[i].isalpha()]


a = wave('TWO words')
print(a)
