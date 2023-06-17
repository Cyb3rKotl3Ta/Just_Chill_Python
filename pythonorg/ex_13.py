

def fibonnaci1(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci1(n - 1) + fibonnaci1(n - 2)


FibArray = [0, 1]


def fibonacci2(n):
    # Check is n is less
    # than 0
    if n <= 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci2(n - 1) +\
        fibonacci2(n - 2)
    FibArray.append(temp_fib)
    return temp_fib


# Driver Program



def fibonacci3(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program


#x = int(input("Enter num: "))

print(fibonacci3(9))
print(fibonacci2(9))
print(fibonnaci1(9))
