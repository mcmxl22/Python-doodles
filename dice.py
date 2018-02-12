#! /usr/bin/env python
# By Micah M. 2018
# dice version 1.0.01
# Python 3.6.4


import random
 
def dice():
    while True:
        roll_dice = input('Roll? ')
        if roll_dice in ['y', '']:
            print(random.randint(1, 6))
        elif roll_dice == 'n':
            raise SystemExit
        else:
            print('invalid entry')
 
dice()
