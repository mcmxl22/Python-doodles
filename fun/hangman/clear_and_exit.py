#!/usr/bin/env python3

"""
clear_and_exit version 1.1
Python 3.8
"""

from os import system
from sys import platform

def clear_and_exit():
    """Clear the screen."""
    if platform in "win32":
        system("cls")
        exit(0)

    else:
        system("clear")
        exit(0)

if __name__ == "__main__":
    clear_and_exit()
