from itertools import combinations

def choose_best_sum(t, k, ls):
    comb = [sum(i) for i in list(combinations(ls, k))]
    find2 = [i for i in comb if i <= t]
    print()

    if t in comb:
        return comb[comb.index(t)]
    elif find2 != []:
        return max(find2)
    else: return None

def choose_best_sum2(t, k, ls):
    try: 
        return max(sum(i) for i in combinations(ls,k) if sum(i)<=t)
    except:
        return None

def choose_best_sum3(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)

def choose_best(t,k,ls):
    if k == 0: return 0
    best = -1
    for i, v in enumerate(ls):
        if v > t: continue
        b = choose_best(t - v, k - 1, ls[i+1:])
        if b < 0: continue
        b += v
        if b > best and b <= t:
            best = b
    return best

def choose_best_sum(t, k, ls):
    c = choose_best(t,k,ls)
    if c <= 0 : return None
    return c

kilometrs = 430
towns = 4
km_between_towns = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

print(choose_best_sum(kilometrs, towns, km_between_towns))
