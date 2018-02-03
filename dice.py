#! /usr/bin/env python
# By Micah M. 2018
# dice version 1.0
# Python 3.6.4


import random


def dice():
    sides = [1, 2, 3, 4, 5, 6]
    rollDice = input('roll? ')
	
    if rollDice == 'y':
        i = random.choice(sides)
        print(i)
        dice()

    elif rollDice == 'n':
        quit()
    
    else:
        print('invalid entry')
        dice()

dice()
