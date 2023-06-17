

def isPrime1(n: int):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def isPrime2(n: int) -> None:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return print(d * d > n)


def isPrime3(n: int):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2


x = int(input("Enter your first number: "))
print(isPrime1(x))
print(isPrime2(x))
print(isPrime3(x))
