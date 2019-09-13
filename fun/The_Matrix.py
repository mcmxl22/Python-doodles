#!/usr/bin/env python3
"""
the_matrix version 1.1
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
        "9" 
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

    while True:
        matrix = random.choice(characters)
        for i in matrix:
            print(i, end="\t")


if __name__ == "__main__":
    the_matrix()
