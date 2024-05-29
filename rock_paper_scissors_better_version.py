
import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = ''
player_choice = ''

while player_choice != 'n':
    while player_move != 'r' or player_move != 'p' or player_move != 's':
        player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
        print()

        if player_move == 'r':
            player_move = rock
            break
        elif player_move == 'p':
            player_move = paper
            break
        elif player_move == 's':
            player_move = scissors
            break
        else:
            print("Invalid input !")
            player_choice = input("If you want to try again, please enter [y]: ")
            print()
            if player_choice == 'y':
                continue
            else:
                print("Thank You for Your time !")
                raise SystemExit("Have a good day !")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")
    print()

    # Rock beats scissors (the scissors get broken by the rock)
    # Scissors beat paper (the paper gets cut by the scissors)
    # Paper beats rock (the paper covers the rock)

    if (computer_move == rock and player_move == scissors) or \
            (computer_move == scissors and player_move == paper) or \
            (computer_move == paper and player_move == rock):
        print("You lose!")
        print()
    elif computer_move == player_move:
        print("Draw!")
        print()
    else:
        print("You win!")
        print()

    player_choice = input("If you want to try again, please enter [y]: ")
    print()
    if player_choice == 'y':
        continue
    else:
        print("Thank You for Your time !")
        raise SystemExit("Have a good day !")
