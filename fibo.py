#! /usr/bin/env python
# By Micah M. 2018
# Fibo version 1.01
# Python 3.6.4


def F():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def subfib(StartNumber, endNumber):
    for cur in F():
        if cur > endNumber:
            return
        if cur >= StartNumber:
            yield cur

for i in subfib(2, 400):
    a = [int(x) for x in str(i)]
    print (a)

quit()
