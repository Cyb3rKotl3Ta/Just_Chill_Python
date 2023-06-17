

def isPrime(n: int) -> None:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return print(d * d > n)


def isOdd(x: int) -> None:
    if x % 4 == 0 and x % 2 == 0:
        return print("Is even and multiple to 4")
    elif x % 2 == 0:
        return print("Is even")
    else:
        return print("Is odd")


x = float(input("Enter your first number: "))
isOdd(x)

y = float(input("Enter your first number: "))

z = x / y
isPrime(z)
