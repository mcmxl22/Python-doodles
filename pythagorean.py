#!/usr/bin/env python3
'''By Micah M. 2018
   pythagorean version 1.1
   Python 3.7'''


def pythag():
    '''finds the length of side C
       when A and B are known.'''
    while True:
        a = input('Enter length a: ')
        b = input('Enter length b: ')
        c = int(a)**2 + int(b)**2
        print(f'Length c is {c}.')

pythag()
