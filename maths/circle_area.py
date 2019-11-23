#!/usr/bin/env python3
"""
circle_area version 1.5
Python 3.7
"""

import math


def find_area():
    """Find the area of a circle."""
    while True:
        radius = input("Enter the radius of a circle. ")

        try:
            float(radius)
        except ValueError as Error:
            print(f"Enter a number. ")
        else:
            result = math.pi * float(radius) ** 2
            return result


if __name__ == "__main__":
    area = find_area()
    print(f"The area of the circle is {round(area, 2)}.")
