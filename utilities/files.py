#!/usr/bin/env python3

"""
files Version 1.7
requires: numli.py
Python 3.7
"""

import sys
from os import path, remove
from numli import add_numbers


def create_files(file_name):
    """Create a file and/or confirm it."""
    file_name = input("Enter file name. ")

    if path.exists(file_name):
        print(f"{file_name} already exists!")

    else:
        with open(file_name, "w+"):

            if path.exists(file_name):
                print(f"{file_name} created!")
            else:
                return


def delete_file(file_name):
    """Delete files."""
    file_name = input("Enter file to be deleted: ")
    confirm_file = input(f"Are you sure you want to delete {file_name}? ")

    if confirm_file in "y":
        remove(file_name)
        print(f"{file_name} deleted!")
    else:
        sys.exit(0)


def file_options(file_name):
    """Choose what to do with a file."""
    while True:
        options = ["Create file", "Delete file", "Exit"]
        add_numbers(options)
        file_choice = input("Choose an option. ")

        if file_choice in "1":
            create_files(file_name)
        elif file_choice in "2":
            delete_file(file_name)
        else:
            exit(0)


if __name__ == "__main__":
    sys.exit(file_options("file_name"))
