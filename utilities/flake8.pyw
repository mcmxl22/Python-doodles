#!/usr/bin/env python3
"""
flake8 version 1.1
requires: numli.py, black
Python 3.7
"""

import numli
from os import system, path


def check_pep8():
    """Check with black."""
    options = ["Yes", "Exit"]
    numli.add_numbers(options)
    check = input("Check file? ")

    if check in "1":
        file_name = input("Enter file name. ")
        print("Checking with black.")

        if path.exists(f"{file_name}.py"):
            system(f"black {file_name}.py")

        else:
            print("Invalid File!")
            check_pep8()

    elif check in "2":
        raise SystemExit

    else:
        check_pep8()


if __name__ == "__main__":
    exit(check_pep8())
