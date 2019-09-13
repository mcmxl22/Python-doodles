#!/usr/bin/env python3
"""
timeTest version 1.2
Python 3.7
"""

import time

lst = ["rest"]

t0 = time.time_ns()
print(list[0] + "ing")
t1 = time.time_ns()
total = t1 - t0
print(total, "list")

t0 = time.time_ns()
print("resting")
t1 = time.time_ns()
total = t1 - t0
print(total, "string")

t0 = time.time_ns()
suffix = "ing"
print(f"rest{suffix}")
t1 = time.time_ns()
total = t1 - t0
print(total, "fstring")

t0 = time.time_ns()
suffix = "ing"
print("rest%s" % suffix)
t1 = time.time_ns()
total = t1 - t0
print(total, "%string")
