import  random


def rand_func(randlist: list):
    for i in range(0, 12):
        m = random.randint(0, 51)
        randlist.append(m)


def func(list1: list, list2: list, list3: list):
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list1[x] == list2[y]:
                list3.append(list1[x])
            else:
                pass


list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_c = []

list1 = []
list2 = []

list_d = []

rand_func(list1)
rand_func(list2)



func(list1, list2, list_d)
func(list_a, list_b, list_c)

print(list_c)
print(list1)
print(list2)
print(list_d)
