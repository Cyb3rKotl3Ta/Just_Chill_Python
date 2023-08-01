import random

cab = random.randint(1000, 9999)
print(cab)
cab_lst = [int(x) for x in str(cab)]
print(cab_lst)
while True:
    user_input = int(input('Guess a 4-digit number: '))
    user_input_lst = [int(x) for x in str(user_input)]
    if user_input not in range(1000, 10000):
        print('Incorrect input, must be 4-digit number: ')
        continue

    count = 0
    for i in cab_lst:
        if i in user_input_lst:
            count += 1

    if count == 4:
        print(f'Yeah you win, number: {cab}')
        break
    else:
        print(f'{count} cows, {4 - count} bulls')
