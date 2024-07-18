#!/usr/bin/env python3

"""
clear_screen version 1.2
python 3.8
"""

import os


def clear_screen() -> None:
    """Clears the screen."""
    try:
        os.system("cls")
    except OSError:
        os.system("clear")


if __name__ == "__main__":
    clear_screen()
