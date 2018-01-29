#! /usr/bin/env python
# By Micah M. 2018
# countDown version 1.01
# Python 3.6.4


import time


def count():
    seconds = int(input('How long? '))
    for i in reversed(range(seconds)):
        time.sleep(1)
        print("%s\r" % i),


if __name__ == "__main__":
    count()
