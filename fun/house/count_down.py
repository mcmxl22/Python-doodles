#!/usr/bin/env python3

"""
countDown version 1.3
Python 3.7
"""

import time
import sys


def count(seconds):
    """Count down in seconds."""
    seconds = int(input("How long? "))
    for i in reversed(range(seconds)):
        time.sleep(1)
        print(i, end="\r")


if __name__ == "__main__":
    count("seconds")
