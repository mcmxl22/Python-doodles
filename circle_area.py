#!/usr/bin/env python3
"""circle_area version 1.3
   Python 3.7.2"""


import math


def find_area():
    """Find the area of a user defined circle."""
    while True:
        radius = input('Enter the radius of the circle. ')
        result = math.pi * int(radius)**2
        
        try:
           number = int(radius) 
        except ValueError as e:
            print(f'Please enter a number.')
        else:
            return result


if __name__ == "__main__":
    area = find_area()
    print(f'The area of the circle is {area}.')
