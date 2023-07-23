def exp_sum(n):
    lst_of_1 = []
    lst_num = [n]
    count = 0
    while len(lst_of_1) != n:
        for i in range(len(lst_num)):
            if lst_num[i] > 1:
                lst_num[i] -= 1
                lst_num.append(lst_num[i]-1)
                lst_of_1.append(1)
            print(lst_of_1)
        count+=1
    return(lst_of_1, lst_num, count)

print(exp_sum(3))