#!/usr/bin/env python3

"""
clear_screen version 1.1
python 3.8
"""

from os import system
from sys import platform

def clear_screen():
    """Clear the screen."""
    if platform in "win32":
        system("cls")

    else:
        system("clear")

if __name__ == "__main__":
    clear_screen()
