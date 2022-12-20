#!/usr/bin/env python3

"""
get_path version 1.2
Python 3.8
"""

import os

class Path:

    @staticmethod
    def get_path() -> str:
        os.chdir("resources")
        path = os.path.abspath("words_alpha.txt")
        return path

if __name__ == "__main__":
    Path.get_path()
