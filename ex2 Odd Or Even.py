

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 % 2 == 0:
    print(f'Number {num1} is even')
if num1 % 2 != 0:
    print(f'Number {num1} is odd')
if num1 % 4 == 0:
    print(f'Number {num1} is multiple of 4')
if num1 % num2 == 0:
    print(f'Number {num1} is evently divide on number {num2}')
else:
    print(f'Number {num1} is oddly divide on number {num2}')
