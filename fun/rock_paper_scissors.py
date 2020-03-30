#!/usr/bin/env python3
"""
rps version 2
python 3.7
"""

import numli


def rps():
    choices = ['Rock', 'Paper', 'Scissors']
    value = {'1': 10, '2': 1, '3': 5}
    numli.addnum(choices)

    player1 = input('Player 1 enter name. ')
    player2 = input('Player 2 enter name. ')

    turn_1 = input(f'{player1.capitalize()} enter choice. ')
    turn_2 = input(f'{player2.capitalize()} enter choice. ')

    play_1 = value[turn_1]
    play_2 = value[turn_2]

    if play_1 > play_2:
    	print(f"{player1.capitalize()} wins!")

    elif turn_1 == turn_2:
    	print("Tie!")

    else:
    	print(f"{player2.capitalize()} wins!")


if __name__ == "__main__":
    rps()
