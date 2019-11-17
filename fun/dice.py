#!/usr/bin/env python3
"""
dice version 1.2
Python 3.7
"""

import random


def dice():
    """Roll the dice"""
    while True:
        roll_dice = input("Roll? ")

<<<<<<< HEAD
        if roll_dice in ["y", ""]:
=======
        if roll_dice in ['y', '']:
>>>>>>> 79e836a62bc508e7179be3d138b87eade7614735
            print(random.randint(1, 6))

        elif roll_dice == "n":
            raise SystemExit

        else:
            print("Invalid Entry")


if __name__ == "__main__":
    dice()
