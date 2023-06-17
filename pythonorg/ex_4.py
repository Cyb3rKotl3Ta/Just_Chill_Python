

x = range(5, 51)
list1 = []

y = int(input("Enter the number of divisors: "))

for i in range(len(x)):
    if x[i] % y == 0:
        list1.append(x[i])
    else:
        pass

print(list1)


