#!/usr/bin/env python3

"""
Security_Code Version 3.2
Python 3.7
"""

from datetime import datetime
from os import path
from random import choice
from string import ascii_uppercase


DATE = datetime.now()
DAY = DATE.day


def transfer_file():
    """
    Check if file exists.
    """
    if path.exists("transfer.txt"):
        return
    else:
        with open("transfer.txt", "w+") as file:
            return


def code_file():
    """
    Check if file exists.
    """
    if path.exists("code.txt"):
        return
    else:
        with open("code.txt", "w") as file:
            return


def set_expiration():
    """
    Sets date format and adds a day.
    """
    expires = f"{DAY + 1}"
    return expires


def set_letter_code():
    """
    Sets random, two letter code.
    """
    letters = ascii_uppercase
    first_letter = choice(letters)
    second_letter = choice(letters)
    day_code = f"{first_letter}{second_letter}"
    return day_code


def write_code():
    """
    Writes day_code to code.txt.
    """
    tomorrow = set_expiration()
    today = str(DAY)

    with open("code.txt", "r+") as file:
        file.truncate()
        code = "".join(file.readlines())
        file_code = file.write(set_letter_code())

        if not code:
            file_code
        else:
            return code
        if today == tomorrow:
            with open("code.txt", "w") as file:
                file_code
        else:
            return code


def main():
    """
    Set next day expiration date and print a random, 2 letter
    security code that changes daily to indicate expiration.
    """
    with open("transfer.txt", "w") as file:
        day_format = f"{DATE.month}/{set_expiration()}/{DATE.year}"

        if not write_code():
            file.write(f"Expires: {day_format}\n2:59am\nxx")
        else:
            file.write(f"Expires: {day_format}\n2:59am\n{write_code()}")


if __name__ == "__main__":
    transfer_file()
    code_file()
    main()
