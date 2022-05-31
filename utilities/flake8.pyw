#!/usr/bin/env python3
"""
flake8 version 1.2
requires: black
Python 3.7
"""

from os import system, path


def add_numbers(num):
        """Add numbers to menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)


def check_pep8():
    """Check file with black."""
    invalid = "\nInvalid File!\n"
    options = ["Yes", "Exit"]
    add_numbers(options)
    check = input("\nCheck a file? ")

    if check in "1":
        file_name = input("Enter file name. ")
        print("\nChecking!\n")

        if path.exists(f"{file_name}.py"):
            system(f"black {file_name}.py")

        else:
            print(f"{invalid}")
            check_pep8()

    elif check in "2":
        exit()

    else:
        print(f"{invalid}")
        check_pep8()


if __name__ == "__main__":
    check_pep8()
