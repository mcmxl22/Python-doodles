#!/usr/bin/env python3
"""
anagram version 1
Python 3.7
"""


def check_anagram():
    """Check if two words contain all the same letters."""
    word1 = input('Enter first word. ')
    word2 = input('Enter second word ')

    if sorted(word1) == sorted(word2):
        print('Anagram!')

    else:
        print('No anagram!')

if __name__ == "__main__":
    check_anagram()

