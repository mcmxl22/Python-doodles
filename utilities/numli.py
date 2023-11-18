#!/usr/bin/env python3

"""
pip_up version 1.7
Python 3.7
"""

from subprocess import run


def pkg_update():
    """Update pip packages."""
    while True:
        print("1 Yes")
        print("2 Exit")

        choice = input("Check for updates? ")

        if choice in "1":
            print("Checking for updates...")
            run("pip-review --local --interactive", check=True)
        else:
            exit()


if __name__ == "__main__":
    pkg_update()
