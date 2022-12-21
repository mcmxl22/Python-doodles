#!/usr/bin/env python3

"""
Security_Code Version 3.3
Python 3.7
"""

import datetime
import os
import random
import string 


DATE = datetime.datetime.now()
DAY = DATE.day


def transfer_file() -> None:
    """
    Check if file exists and create it if it doesn't.
    """
    if not os.path.exists("transfer.txt"):
        with open("transfer.txt", "w+") as f:
            pass


def code_file() -> None:
    """
    Check if file exists and create it if it doesn't.
    """
    if not os.path.exists("code.txt"):
        with open("code.txt", "w") as f:
            pass


def set_expiration() -> str:
    """
    Get the expiration date as a string in the format "month/day/year".
    """
    return f"{DAY + 1}"


def set_letter_code() -> str:
    """
    Generate and return a random two-letter code using uppercase letters.
    """
    letters = string.ascii_uppercase
    first_letter = random.choice(letters)
    second_letter = random.choice(letters)
    day_code = f"{first_letter}{second_letter}"
    return day_code


def write_code() -> str:
    """
    Write code to code.txt. If file is empty or expired, generate and write a new code.
    """
    today = str(DAY)
    tomorrow = set_expiration()

    with open("code.txt", "r+") as file:
        code = file.read()
        if not code or today == tomorrow:
            file.truncate(0)
            file.write(set_letter_code())
        else:
            return code


def main() -> None:
    """
    Write the expiration date and security code to the transfer.txt file.
    """
    expiration_date = f"{DATE.month}/{set_expiration()}/{DATE.year}"

    with open("transfer.txt", "w") as file:
        code = write_code()
        file.write(f"Expires: {expiration_date}\n2:59am\n{code}")


if __name__ == "__main__":
    transfer_file()
    code_file()
    main()
