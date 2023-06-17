import random


guess_count = 0
guess_limit = 5
out_of_guesses = False

secret_num = random.randint(0, 10)
guess = int(input("Enter num from 0 to 10: "))


while guess != secret_num and not out_of_guesses:
    guess_count += 1
    if guess_count < guess_limit:
        if guess > secret_num:
            guess = int(input("Enter tinier num: "))
        if guess < secret_num:
            guess = int(input("Enter bigger num: "))
    else:
        out_of_guesses = True

if out_of_guesses:
    print(f"You lose and use {guess_count} times")
else:
    if guess_count > 3:
        print(f"You win and use {guess_count} times, not bad")
        print(f"The guessing number was {secret_num}")
    if guess_count > 4:
        print(f"You win and use {guess_count} times, uhh, you was close to lose")
        print(f"The guessing number was {secret_num}")
    if guess_count < 2:
        print(f"You win and use {guess_count} times, wow, just one try")
        print(f"The guessing number was {secret_num}")

