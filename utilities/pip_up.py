#!/usr/bin/env python3
"""
pip_up version 1.1
requires: numli.py
Python 3.7
"""

from numli import add_numbers
from os import system


def pkg_update():
    """Update pip packages."""
    options = ["Yes", "Exit"]
    add_numbers(options)
    choice = input("Check for updates? ")

    if choice in "1":
        print("Checking for updates.")
        results = system("pip list -o")

        system("pip-review --local --interactive")
        pkg_update()

    elif choice in "2":
        exit(0)

    else:
        pkg_update()


if __name__ == "__main__":
    exit(pkg_update())
