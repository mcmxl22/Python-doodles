#!/usr/bin/env python3
"""
clear_and_print version 1
Python 3.8
Requires: clear_screen.py
"""

from clear_screen import clear_screen


def clear_and_print(text):
"""Clears the screen and prints your choice of message"""
    clear_screen()
    print(text)


if __name__ == "__main__":
    exit(clear_and_print())
