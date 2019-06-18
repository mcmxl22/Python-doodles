#!/usr/bin/env python3
"""
age100 version 1.2
Python 3.7
"""

import datetime


def age100():
    """The year you will be 100"""
    get_name = input("What's your name? ")
    get_age = int(input("What's your age? "))
    current_year = datetime.datetime.now()
    age_100 = (current_year.year - get_age) + 100

    if get_age >= 100:
        print('Congratulations! You already reached 100!')

    else:
        print(f'{get_name}, you will be 100 years old in {age_100}!')

if __name__ == "__main__":
    age100()
