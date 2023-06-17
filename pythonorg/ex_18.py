import random


def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        cowbull[0]+=user_guess.count(number[i])
    return cowbull

def print_cows_n_bulls(cows, bulls):
    if cows > 1 and bulls > 1:
        print(f"{cows} cows, {bulls} bulls")
    elif cows == 1 and bulls > 1:
        print(f"{cows} cow, {bulls} bulls")
    elif cows > 1 and bulls == 1:
        print(f"{cows} cows, {bulls} bull")
    else:
        print(f"{cows} cow, {bulls} bull")

def cows_n_bulls(rand_num):
    guesses = 0
    print(rand_num)

    while True:
        user_num = input("Enter 4-digit number:\n>>> ")
        if user_num == "exit":
            break

        cowbullcount = compare_numbers(rand_num,user_num)
        print(cowbullcount)
        guesses+=1

        print_cows_n_bulls(cowbullcount[0], cowbullcount[1])

        if cowbullcount[1] == 4:
            print(f"U use {guesses} guesses")
            print('You win!!!')
            return False
            



rand_num = str(random.randint(1000, 9999))  

cows_n_bulls(rand_num)