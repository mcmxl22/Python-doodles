#!/usr/bin/env python3
"""
the_matrix version 1.2
Python 3.7
"""

import random


def the_matrix():
    characters = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "Z",
        "=",
        "+",
        "#",
        ".",
        "<",
        ":",
        "&",
        "$",
    ]

    yield random.choice(characters)


if __name__ == "__main__":
    while True:
        for i in the_matrix():
            print(i, end="\t")
