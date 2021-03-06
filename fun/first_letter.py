#!/usr/bin/env python3
"""
first_letter version 1
Python 3.7
"""


def letter_switch():
    """Switch first letter of two words."""
    get_words = input("Enter two words. ")

    # Convert words to a list.
    word_list = list(get_words)

    # Find the space.
    space = word_list.index(' ')

    # Find first letter of the first word.
    first = word_list[0:1]

    # Remove first letter of each word.
    del word_list[0]
    del word_list[space]

    # Re-insert switched letters.
    word_list.insert(space, ''.join(first))
    word_list.insert(0, get_words[space + 1])

    result = ''.join(word_list)
    print(result)


if __name__ == "__main__":
    letter_switch()