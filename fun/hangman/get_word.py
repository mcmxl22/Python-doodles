#!/usr/bin/env python3
"""
get_word version 1
Python 3.8
Requires a .txt file with a list of words.
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""

from random import choice


def get_word():
    """Get a random word."""
    word_list_url = "C:/Users/mcmxl/mystuff/hangman/resources/words_alpha.txt"
    with open(word_list_url, "r") as file:
        lines = file.readlines()
        word_select = choice(lines)
    word = word_select.rstrip()  # Removes \n character.
    return word


if __name__ == "__main__":
    get_word()
