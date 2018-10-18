#!/usr/bin/env python
'''By Micah M. 2018
   weird version 1
   Python 3.7'''


def weird():
    '''weird'''
    while True:
        pick_number = int(input('Pick a number: '))
        if pick_number % 2 == 0:
            print('Not Weird!')
        else:
            print('Weird!')


weird()
