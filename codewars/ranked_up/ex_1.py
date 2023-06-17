def solution(number):
    res = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    return res

def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def solution3(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))

print(solution(200))
