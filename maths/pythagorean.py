#!/usr/bin/env python3
"""
Pythagorean version 1.4
Python 3.7
"""
import math


def pythag():
    """Find the length of side C
       when sides A and B are known."""
    while True:
        length_a = input("Enter length a: ")
        length_b = input("Enter length b: ")
        length_c = math.sqrt(int(length_a) ** 2 + int(length_b) ** 2)
        return f"Length c is {length_c}."


if __name__ == "__main__":
    pythag = pythag()
    print(pythag)
