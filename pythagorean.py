#!/usr/bin/env python
# By Micah M. 2018
# pythagorean version 1.1
# Python 3.7


def pythag():
    while True:
        a = input('Enter length a.\n> ')
        b = input('Enter length b.\n> ')
        c = int(a)**2 + int(b)**2
        print(f'Length c is {c}.')

pythag()
