import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = sorted([random.randint(1, 10) for i in range(0, 10)])
d = sorted([random.randint(1, 10) for i in range(0, 10)])

lst1_comprehension = [i for i in set(a) if i in set(b)]
lst2_comprehension = [i for i in set(c) if i in set(d)]

print(a)
print(b)
print('///////////////////////////////////////////////////////////////')
print(c)
print(d)
print('//////////////////////////////////////////////////////////////')
print(lst1_comprehension)
print(lst2_comprehension)
