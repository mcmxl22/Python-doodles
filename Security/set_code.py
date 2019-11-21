#!/usr/bin/env python3
"""
set_code Version 1
Python 3.7
"""

import random
import string


def set_code():
    """Sets random two letter code."""
    letters = string.ascii_uppercase
    code_1 = random.choice(letters)
    code_2 = random.choice(letters)
    day_code = f"{code_1}{code_2}"
    return day_code


if __name__ == "__main__":
    set_code()
