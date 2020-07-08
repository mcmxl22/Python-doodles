#!/usr/bin/env python3
"""
numli Version 1.2
Python 3.7
"""

import sys


def add_numbers(num):
    """Add numbers to a list"""
    for c, value in enumerate(num, 1):
        print(c, value)


if __name__ == "__main__":
    sys.exit(add_numbers("num"))
