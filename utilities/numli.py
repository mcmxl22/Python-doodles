#!/usr/bin/env python3
"""
numli Version 1.1
Python 3.7
"""


def add_numbers(num):
    """Add numbers to a list"""
    for c, value in enumerate(num, 1):
        print(c, value)


if __name__ == "__main__":
    exit(add_numbers("num"))
