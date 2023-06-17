def digital_root(n):
    n_lst = [int(x) for x in str(abs(n))]
    while len(n_lst) > 1:
        n_lst = [int(x) for x in str([sum(n_lst)][0])]
    return n_lst[0]

def digital_root2(n):
    return n if abs(n) < 10 else digital_root(sum(map(int,str(abs(n)))))

def digital_root3(n):
	return abs(n)%9 or abs(n) and 9 

print(digital_root3(-144))

        