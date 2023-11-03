import random

# start screen
print('---------------------------')
print('- ROCK | PAPER | SCISSORS -')
print('---------------------------')

# game variables
possibleChoices = ('Rock', 'Paper', 'Scissors')
isGameRunning = True

# game loop
while isGameRunning:

    # selection of player
    playerSelection = 0

    while not playerSelection:
        try:
            playerSelection = int(input('\n[1] Rock | [2] Paper | [3] Scissors\n'))
            if playerSelection not in (1,2,3):
                raise ValueError
        except ValueError:
            playerSelection = 0

    player = possibleChoices[playerSelection-1]

    # selection of computer
    computer = possibleChoices[random.randint(0,2)]

    if player == computer:
        print(f'Draw! Computer selected {computer}\n')
    else:
        if player == possibleChoices[0]:
            if computer == possibleChoices[1]:
                print(f'You lost the game! Computer selected {computer}\n')
            else:
                print(f'You won the game! Computer selected {computer}\n')
        elif player == possibleChoices[1]:
            if computer == possibleChoices[2]:
                print(f'You lost the game! Computer selected {computer}\n')
            else:
                print(f'You won the game! Computer selected {computer}\n')
        elif player == possibleChoices[2]:
            if computer == possibleChoices[0]:
                print(f'You lost the game! Computer selected {computer}\n')
            else:
                print(f'You won the game! Computer selected {computer}\n')

    # restart game if needed
    restartGame = ''
    while restartGame not in ('y', 'n'):
        restartGame = input('Do you want to restart the game?\n[y] yes | [n] no\n')

    if (restartGame != 'y'):
        isGameRunning = False