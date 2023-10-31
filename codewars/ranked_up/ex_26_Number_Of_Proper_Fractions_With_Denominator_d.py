from math import gcd

def proper_fractions(n):
    return 0 if n == 1 else sum(1 for i in range(1, n) if gcd(i, n) == 1)

print(proper_fractions(5))