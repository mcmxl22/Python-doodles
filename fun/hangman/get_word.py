#!/usr/bin/env python3
"""
get_word version 1.2
Python 3.8
Requires get_path.py
Requires a .txt file with a list of words.
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""

from get_path import Path
from random import choice


def get_word() -> str:
    """Get a random word."""
    file_path = Path.get_path("")
    with open(file_path, "r") as file:
        lines = file.readlines()
        word_select = choice(lines)
    word = word_select.rstrip()  # Removes \n character.
    return word


if __name__ == "__main__":
    exit(get_word())
