#!/usr/bin/env python3
"""
Pythagorean version 1.5
Python 3.8
"""
import math


def pythag():
    """Find the length of side C
       when sides A and B are known."""
    while True:
        length_a = input("Enter length a: ")
        length_b = input("Enter length b: ")
        try:
            (len_a := float(length_a))
            (len_b := float(length_b))
        except ValueError as Error:
            print(f"Enter a number. ")
        else:
            length_c = math.sqrt(len_a ** 2 + len_b ** 2)
            return f"Length c is {round(length_c, 3)}."


if __name__ == "__main__":
    pythag = pythag()
    print(pythag)
