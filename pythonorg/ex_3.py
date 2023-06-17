

list1 = [1, 2, 3, 4, 5, 13, 24, 16, 9, 23]
print(list1)
x = int(input("Enter quantity of elements in list: "))

list2 = []

for i in range(len(list1)):
    if list1[i] < x:
        print(list1[i])
        list2.append(list1[i])
    else:
        pass

print("/\/\/\/\/\/\/\/\/\/\/\\")

i = 0
while i < len(list2):
    if list2[i] < 20:
        print(list2[i])
    else:
        pass
    i += 1
