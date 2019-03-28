#!/bin/python3
"""pythagorean version 1.2
   Python 3.7.2"""


def pythag():
    """find the length of side C
       when A and B are known."""
    while True:
        a = input('Enter length a: ')
        b = input('Enter length b: ')
        c = int(a)**2 + int(b)**2
        print(f'Length c is {c}.')

if __name__ == "__main__":
    pythag()
