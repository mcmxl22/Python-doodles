#!/usr/bin/env python3
"""
ten_print version 1.1
Python 3.7
"""

import random
import time


def ten_print():

    start = time.time()
    elapsed = 0

    while elapsed < 2:
        sticks = random.choice(["\\", "/", "|"])
        print(" ".join(sticks), end="")
        elapsed = time.time() - start


if __name__ == "__main__":
    ten_print()
