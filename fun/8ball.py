#!/usr/bin/env python3
"""
8ball version 1
Python 3.7
"""

import random


def ball():
    """Shake the eight ball!"""
    phrases = ["Yes", "No", "Try Again", "You're Doomed",
               "The Future is Bright"]
    answer = random.choice(phrases)
    return answer

if __name__ == "__main__":
    magic = ball()
    print(magic)
