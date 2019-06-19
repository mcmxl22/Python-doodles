#!/usr/bin/env python3
"""
dice version 1.1
Python 3.7
"""


import random

def dice():
   """Roll the dice"""
    while True:
        roll_dice = input('Roll? ')

        if roll_dice in ['y', '']
            print(random.randint(1, 6)

        elif roll_dice == 'n':
            raise SystemExit

        else:
            print('Invalid Entry')

if __name__ == "__main__":            
    dice()
