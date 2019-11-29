#!/usr/bin/env python3
"""
Security_Code Version 3
Python 3.7
"""

import datetime
import os.path
import random
import string


DATE = datetime.datetime.now()
DAY = DATE.day

def transfer_file():
    """Check if file exists."""
    if os.path.exists("transfer.txt"):
        return
    else:
        with open("transfer.txt", "w") as file:
            return


def code_file():
    """Check if file exists."""
    if os.path.exists("code.txt"):
        return
    else:
        with open("code.txt", "w") as file:
            return


def format_time():
    """Extracts time of day."""
    future_time = DATE + datetime.timedelta(0)
    time = list(str(future_time))
    del time[0:11], time[4:14]
    new_time = "".join(time)
    return new_time


def set_expiration():
    """Sets date format and adds a day."""
    expires = f"{str(DAY)}"
    return expires


def set_code():
    """Sets random two letter code."""
    letters = string.ascii_uppercase
    code_1 = random.choice(letters)
    code_2 = random.choice(letters)
    day_code = f"{code_1}{code_2}"
    return day_code


def write_code():
    """Writes day_code to code.txt"""
    with open("code.txt", "r") as file:
        code = "".join(file.readlines())
        
        if not code:
            file.write(set_code())
            print("1")
        else:
            return code

        if str(DAY) == (DAY + 1):
            with open("code.txt", "w") as file:
                file.write(set_code())
                print("2")
        else:
            return code


def main():
    """
    Set next day expiration date and print a random, 2 letter
    security code that changes daily to indicate expiration.
    """
    with open("transfer.txt", "w") as file:
        day_format = f"{DATE.month}/{set_expiration()}/{DATE.year}"
        file.write(f"Expires: {day_format}\n2:59am\n{write_code()}\r")


if __name__ == "__main__":
    transfer_file()
    code_file()
    main()