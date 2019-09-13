#!/usr/bin/env python3
"""
file_check Version 1
Python 3.7
"""
import os.path


def check_file(file):
    """Check if file exists."""
    if os.path.exists("transfer.txt"):
        return

    else:
        with open("transfer.txt", "w+") as file:
            # file = file
            return file


if __name__ == "__main__":
    check_file("file")
