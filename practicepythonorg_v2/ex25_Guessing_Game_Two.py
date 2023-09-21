import random

def computer_guess(num, min, max):
    if num > min and num < max:
        return 'You win'
    

tries = 0

user_num = int(input("Enter number from 1 to 50\n"))
guess_number = random.randint(1, 10)
# computer = random.randint(1, 10)
min = 1
max = 100

while True:
    computer = random.randint(min, max)
    print(computer)
    tries += 1

    if computer == user_num:
        print("You win")
        break
    user = input("Enter guessing number greater(>) or lower(<)\n")
    if user == '<':
        max = computer
    if user == '>':
        min = computer
    # if user != computer and tries == 6:
    #     print("Nu ti vashe popusk")
    #     break
