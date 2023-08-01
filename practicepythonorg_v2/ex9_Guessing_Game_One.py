import random

tries = 0
computer = random.randint(1, 10)

while tries < 3:
    user = int(input("Enter number from 1 to 50\n"))
    tries += 1

    if user > computer:
        print("Senpai it`s too big")
    if user < computer:
        print("Kohay it`s too small are you kidding me")
    if user == computer:
        print("Oh it`s mine sex")
        break
    if user != computer and tries == 6:
        print("Nu ti vashe popusk")
        break
