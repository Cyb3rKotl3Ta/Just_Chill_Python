def simple_multiplication(number) :
    if number % 2 == 0: return number * 8
    else: return number * 9

def simple_multiplication2(number) :
    return number * 9 if number % 2 else number * 8

def simple_multiplication3(n) :
    return n * (8 + n%2)

print(simple_multiplication(8))