def delete_nth(order: list,max_e: int):
    new_lst = []
    for i in order:
        if new_lst.count(i) < max_e:
            new_lst.append(i)

    return new_lst

def delete_nth_v2(order: list, max_e: int):
    return [i for idx, i in enumerate(order) if order[:idx + 1].count(i) <= max_e]

################################################
def delete_nth_v3(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans


print(delete_nth_v3([20,37,20,21], 1))

