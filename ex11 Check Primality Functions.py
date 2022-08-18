

def is_prime(number):
    lst = []
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
            lst.append(i)
        else:
            pass
    if count > 0:
        print('Isn`t Prime')
        print(lst)
        return False
    else:
        print('Is Prime')
        print(lst)
        return True

is_prime(174)
