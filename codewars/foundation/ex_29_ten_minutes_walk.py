from collections import Counter

def is_valid_walk_v2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x, y = 0, 0
    
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    
    return x == 0 and y == 0


def is_valid_walk_test(walk):
    walk = Counter(walk)
    for i in walk.values():
        print(i)


lst1 = ['n','s','n','s','n','s','n','s','n','s']

print(is_valid_walk(lst1))