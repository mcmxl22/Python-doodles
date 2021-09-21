#!/usr/bin/env python3

"""
get_path version 1.1
Python 3.8
"""

import os

class Path:

    def get_path(path) -> str:
        os.chdir("resources")
        path = os.path.abspath("words_alpha.txt")
        return path


if __name__ == "__main__":
    exit(Path.get_path("path"))
