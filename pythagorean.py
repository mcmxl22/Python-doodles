#!/usr/bin/env python3
"""Pythagorean version 1.3
   Python 3.7.2"""


def pythag():
    """Find the length of side C
       when sides A and B are known."""
    while True:
        a = input('Enter length a: ')
        b = input('Enter length b: ')
        c = int(a)**2 + int(b)**2
        return c

if __name__ == "__main__":
    pythag = pythag()
    print(f'Length c is {pythag}.')
