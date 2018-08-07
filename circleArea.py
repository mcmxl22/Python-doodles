#!/usr/bin/env python
# By Micah M. 2018
# circleArea version 1.1
# Python 3.7


import math


def area():
    while True:
        radius = input('Enter the radius of the circle.\n> ')
        result = math.pi * int(radius)**2
        print(f'The area is {round(result, 2)}.')

area()
