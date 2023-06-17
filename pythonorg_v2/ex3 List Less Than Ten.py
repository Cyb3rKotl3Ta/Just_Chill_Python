
num = int(input("Enter limit of border number: "))
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lst_less_then_5 = [i for i in lst1 if i <= 5]
lst_less_then_user = [print(i) for i in lst1 if i <= num]

print(lst_less_then_5)
