import random


list1 = {"paper", "rock", "scissors"}



def prs():
    player = int(input("Choose [0]paper, [1]rock or [2]scissors: "))
    computer = random.randint(0, 2)

    print(player)
    print(computer)

    if player > 2 or player < 0:
        print("Choose [0]paper, [1]rock or [2]scissors, baka")
    elif player == 0 and computer == 0\
            or player == 1 and computer == 1\
            or player == 2 and computer == 2:
        print("Tie")
    elif player == 0 and computer == 1\
            or player == 1 and computer == 2\
            or player == 2 and computer == 0:
        print("Player win")
    elif player == 0 and computer == 2\
            or player == 1 and computer == 0\
            or player == 2 and computer == 1:
        print("Computer win win")



while True:
    exit = input("Enter exit if want to quit the game: ")
    if exit == "exit":
        break
    elif exit == "play":
        prs()
