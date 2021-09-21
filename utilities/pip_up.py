#!/usr/bin/env python3

"""
pip_up version 1.6
requires: numli.py
Python 3.7
"""

from subprocess import run
from numli import add_numbers


def pkg_update():
    """Update pip packages."""
    while True:
        options = ["Yes", "Exit"]
        add_numbers(options)

        choice = input("Check for updates? ")

        if choice in "1":
            print("Checking for updates.")
            run("pip-review --local --interactive", check=True)
        else:
            exit(0)


if __name__ == "__main__":
    exit(pkg_update())
