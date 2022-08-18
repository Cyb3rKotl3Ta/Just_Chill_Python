

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lst1 = [i for i in a if i % 2 == 0]
lst2 = []

for i in a:
    if i % 2 == 0:
        lst2.append(i)

print(lst1)
print(lst2)

