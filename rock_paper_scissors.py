
import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random_number = random.randint(1, 3)

computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f"The computer chose {computer_move}.")

# Rock beats scissors (the scissors get broken by the rock)
# Scissors beat paper (the paper gets cut by the scissors)
# Paper beats rock (the paper covers the rock)

if (computer_move == rock and player_move == scissors) or \
        (computer_move == scissors and player_move == paper) or \
        (computer_move == paper and player_move == rock):
    print("You lose!")
elif computer_move == player_move:
    print("Draw!")
else:
    print("You win!")
