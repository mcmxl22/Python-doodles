#!/usr/bin/env python3
"""
weird version 1
Python 3.7
"""


def is_weird():
    '''Is a number odd or even?'''
    while True:
        pick_number = int(input('Pick a number: '))

        if pick_number % 2 == 0:
            print('Not Weird!')

        else:
            print('Weird!')

weird()
