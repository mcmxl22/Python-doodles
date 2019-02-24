#!/usr/bin/env python
"""By Micah M. 2019
   count_down version 1.1
   Python 3.7.1"""


import time


def count(seconds):
    """Counts down seconds."""
    seconds = int(input('How long? '))
    for i in reversed(range(seconds)):
        time.sleep(1)
        print(i, end='\r')

if __name__ == "__main__":
    count()
