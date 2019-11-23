#!/usr/bin/env python3
"""
transfers Version 1.1
Python 3.7
"""

from Security_Code import main, code_file


code_file()
main()

def replace_line():
    """Removes previous pass type from file."""
    with open("transfer.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line not in ["L", "R", "LY", "RY"]:
                file.write(line)
        file.truncate()


def select_type():
    """Select a type of pass."""
    zone_options = ["Regional", "Local"]
    for c, value in enumerate(zone_options, 1):
        print(c, value)

    region = input("Select a region. ")

    with open("transfer.txt", "a") as file:
        if region in "1":
            file.writelines("R")
        elif region in "2":
            file.writelines("L")
        else:
            print("Invalid!")

if __name__ == "__main__":
    replace_line()
    select_type()
