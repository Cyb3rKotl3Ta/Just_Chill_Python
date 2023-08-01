

num = int(input('Enter num to find all divisors: '))
lst1 = [i for i in range(1, num + 1) if num % i == 0]

print(lst1)


