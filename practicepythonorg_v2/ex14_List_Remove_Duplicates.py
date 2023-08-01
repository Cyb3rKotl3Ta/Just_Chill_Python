

def no_duplicates_lst(lst1, lst2):
    return list(set(lst1).difference(lst2))


list1 = [1, 2, 3, 4, 5, 6, 23, 21, 14, 14, 14]
list2 = [2, 4, 6, 8, 14, 14]

print(list1, list2)

print(no_duplicates_lst(list1, list2))
