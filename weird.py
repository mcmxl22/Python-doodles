#!/usr/bin/env python3
'''By Micah M. 2018
   weird version 1
   Python 3.7'''


def weird():

    while True:
        N = int(input('Pick a number: '))
        if N % 2 == 0:
            print('Not Weird!')

        else:
            print('Weird!')


weird()