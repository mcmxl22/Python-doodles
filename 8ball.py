#!/bin/python3
"""8ball version 1
   Python 3.7.2"""


import random


def ball():
    """Shake the eight ball!"""
    phrases = ['Yes', 'No', 'Try Again', 'You are Doomed',
               'The Future is Bright']
    answer = random.choice(phrases)
    return answer

if __name__ == "__main__":
    magic = ball()
    print(magic)
