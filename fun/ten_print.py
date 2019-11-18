#!/usr/bin/env python3
"""
ten_print version 1.2
Python 3.7
"""

import random
import time


def ten_print():
    sticks = random.choice(["\\", "/", "|"])
    yield sticks



if __name__ == "__main__":
    start = time.time()
    elapsed = 0

    while elapsed < 2:
        for i in ten_print():
            print("".join(i), end="")
            elapsed = time.time() - start
