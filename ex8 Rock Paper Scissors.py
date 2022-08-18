import random


def plyr_trn(player_turn):
    return 1 if player_turn == 2 else 2


should_continue = True

while should_continue:
    user_choice = input("Enter R - rock, P - paper, S - scissors: ").lower()

    if user_choice not in ['r', 's', 'p']:
        print("You choose not r, s or p. Enter valid choose")
        continue

    gen = {
        1: 'r',
        2: 's',
        3: 'p'
    }

    comp_choice = random.choice(gen)
    win_comb = [('r', 's'), ('s', 'p'), ('p', 'r')]
    print(f'Player: {user_choice}\nComputer: {comp_choice}')

    if user_choice == comp_choice:
        print('Tie')
    if (user_choice, comp_choice) in win_comb:
        print('You win')
    else:
        print('Computer win')

    should_continue = input("Want to proceed? [y/n]").lower() == 'y'
