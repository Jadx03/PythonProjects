
"""
Dice Roll Stimulator

@author: Jainam
"""

import random

def dice_roll():
    while True:
        print("Your number is: " + str(random.randint(1,6)))
        play_again = input("Would you like to play again? (Y/N) ")
        while (play_again != 'y'and play_again != 'Y'):
            if (play_again == 'N' or play_again == 'n'):
                return print("Game Over")
            else:
                print("Input not recognized")
                play_again = input("Would you like to play again? ")

def main():
    game_start = input("Would you like to roll the dice?")
    if (game_start == 'Y'or game_start == 'y'):
        dice_roll()
    else:
        print('too bad')

if __name__ == '__main__':
    main()