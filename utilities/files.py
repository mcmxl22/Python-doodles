#!/usr/bin/env python3

"""
files Version 1.8
requires: numli.py
Python 3.7
"""

import sys
from os import path, remove
from numli import add_numbers


class Options:
    def __init__(self):
        pass

    def file_options(self):
        """Choose what to do with a file."""
        while True:
            file_options = ["Create file", "Delete file", "Exit"]
            add_numbers(file_options)
            file_choice = input("Choose an option. ")

            if file_choice in "1":
                Files.create_files("")
            elif file_choice in "2":
                Files.delete_file("")
            else:
                exit(0)


class Files:
    def __init__(self, name):
        self.name = name

    def create_files(self):
        """Create a file and/or confirm it."""
        name = input("Enter file name. ")

        if path.exists(name):
            print(f"{name} already exists!")

        else:
            with open(name, "w+"):

                if path.exists(name):
                    print(f"{name} created!")
                else:
                    return

    def delete_file(self):
        """Delete files."""
        file_name = input("Enter file to be deleted: ")
        confirm_file = input(f"Are you sure you want to delete {file_name}? ")

        if confirm_file in "y":
            remove(file_name)
            print(f"{file_name} deleted!")
        else:
            sys.exit(0)


def main():
    Options.file_options("")


if __name__ == "__main__":
    main()
