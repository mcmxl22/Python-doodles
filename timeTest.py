#!/usr/bin/env python3
# By Micah M. 2018
# timeTest version 1
# Python 3.7

import time

list = ('rest')

t0 = time.time()
print(list[1] + 'ing')
t1 = time.time()
total = t1 - t0
print(total)


t0 = time.time()
print('resting')
t1 = time.time()
total = t1 - t0
print(total)
