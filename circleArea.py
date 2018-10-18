#!/usr/bin/env python
'''By Micah M. 2018
   circleArea version 1.1
   Python 3.7'''


import math


def circle_area():
   '''Find the area of a circle'''
    while True:
        radius = input('Enter the radius of the circle.\n> ')
        result = math.pi * int(radius)**2
        print(f'The area is {round(result, 2)}.')

circle_area()
