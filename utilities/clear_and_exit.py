#!/usr/bin/env python3
"""
clear_and_exit version 1
Python 3.8
Requires: clear_screen.py
"""

from clear_screen import clear_screen


def clear_and_exit():
"""Clears the screen and exits"""
    exit(clear_screen())


if __name__ == "__main__":
    exit(clear_and_exit())
