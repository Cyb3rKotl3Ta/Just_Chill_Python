import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [random.randint(1, 100) for i in range(0, 10)]
d = [random.randint(1, 100) for i in range(0, 10)]
print(c)
print(d)
lst1 = []
lst2 = [i for i in b if i in a]
lst3 = [i for i in c if i in d and not d in c ]

for i in a:
    if i in b and i not in lst1:
        lst1.append(i)

print(lst1)
print(lst2)
print(lst3)
