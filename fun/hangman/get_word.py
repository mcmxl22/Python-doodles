#!/usr/bin/env python3
"""
get_word version 1.2
Python 3.8
Requires get_path.py
"""

from get_path import Path
from random import choice


def get_word(file_path: str) -> str:
    """Get a random word from file."""
    with open(file_path) as f:
        words = f.read().splitlines()
    return random.choice(words)


if __name__ == "__main__":
    get_word()
