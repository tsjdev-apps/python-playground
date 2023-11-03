import random

# start screen
print('------------------')
print('- HIGHER | LOWER -')
print('------------------')

# game variables
isGameRunning = True

# function to get player selection
def playerSelection():
    player = 0

    while not player:
        try:
            player = int(input('\nEnter a number between 1 and 100:\n'))
            if player not in range(1,100):
                raise ValueError
        except ValueError:
            player = 0
    
    return player

# game loop
while isGameRunning:

    # selection of player
    player = playerSelection()

    # selection of computer
    computer = random.randint(1, 100)

    # set counter
    counter = 1

    # game logic
    while player != computer:
        if player > computer:
            print('Your number is too high!')
        else:
            print('Your number is too low!')
        counter += 1
        player = playerSelection()

    print(f'Congratulations! You matched my number in {counter} steps!')

    # restart the game if needed
    restartGame = ''
    while restartGame not in ('y', 'n'):
        restartGame = input('Do you want to restart the game?\n[y] yes | [n] no\n')

    if restartGame != 'y':
        isGameRunning = False