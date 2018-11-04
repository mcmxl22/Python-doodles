#!/usr/bin/env python
'''By Micah M. 2018
   countDown version 1.1
   Python 3.7.1'''


import time


def count(seconds):
    '''Count down in seconds.'''
    seconds = int(input('How long? '))
    for i in reversed(range(seconds)):
        time.sleep(1)
        print(i, end='\r')

if __name__ == "__main__":
    count()
