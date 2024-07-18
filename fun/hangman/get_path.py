#!/usr/bin/env python3

"""
get_path version 1.3
Python 3.8
"""

import os

def get_path() -> str:
    """Returns path to word list."""
    file_path = os.path.abspath("words_alpha.txt")
    return file_path

if __name__ == "__main__":
    get_path()
