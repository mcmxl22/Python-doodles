#!/usr/bin/env python
"""By Micah M. 2019
   circle_area version 1.2
   Python 3.7.1"""


import math


def find_area(radius):
    """Find the area of a user defind circle."""
    while True:
        radius = input('Enter the radius of the circle. ')
        result = math.pi * int(radius)**2
        if radius == int():
            print(f'The area is {round(result, 2)}.')
        elif radius == str:
            print('Entry must be an intiger!')


if __name__ == "__main__":
    find_area('radius')
