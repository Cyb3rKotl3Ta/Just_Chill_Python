import  random


def rand_func(randlist: list):
    for i in range(0, 12):
        m = random.randint(0, 51)
        randlist.append(m)


def func1(list1: list):
    list2 = []
    for x in range(len(list1)):
        if list1[x] not in list2:
            list2.append(list1[x])
    return list2


def func2(x):
    return list(set(x))


list_a = [1, 1, 2, 3, 5, 5, 8, 13, 21, 21, 34, 55, 89]
list_b = []

print(list_a)
print(func1(list_a))
print(func2(list_a))
