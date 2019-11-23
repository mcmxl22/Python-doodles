#!/usr/bin/env python3
"""
pass_type Version 1
Python 3.7
"""


def replace_line():
    """Removes previous pass type from file."""
    with open("transfer.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line not in ["L", "R"]:
                file.write(line)
        file.truncate()


if __name__ == "__main__":
    replace_line()