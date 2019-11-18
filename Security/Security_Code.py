#!/usr/bin/env python3
"""
Security_Code Version 1
Python 3.7
"""

import datetime
import os.path
import random
import string


def check_file():
    """Check if file exists."""
    if os.path.exists("transfer.txt"):
        return

    else:
        with open("transfer.txt", "w+") as file:
            return


def expiration():
    """
    Set next day expiration date and generate a random, 2 letter
    security code that changes daily to indicate expiration.
    """
    # Sets letters to uppercase.
    letters = string.ascii_uppercase

    # Gets date and time.
    date = datetime.datetime.now()

    # Extracts time of day and adds 3 hours.
    future_time = date + datetime.timedelta(0, 10800)
    time = list(str(future_time))
    del time[0:11]
    del time[4:14]
    new_time = "".join(time)

    # Sets date format and adds a day.
    expires = f"{date.month}-{date.day + 1}-{date.year}"

    # Removes time from date.
    list_date = list(str(date))
    del list_date[10:26]
    new_date = "".join(list_date)
    print(new_date)

    with open("transfer.txt", "r") as file:
        current_data = file.readlines()
        print(str(current_data))

    if str(current_data) not in new_date:
        with open("transfer.txt", "w") as file:
            file.write(f"Expires: {expires} {'XX'} {new_time}")

    elif new_date in expires:
        with open("transfer.txt", "w") as file:
            code_1 = random.choice(letters)
            code_2 = random.choice(letters)
            day_code = f"{code_1}{code_2}"
            file.write(f"Expires: {day_code} {expires} {new_time}")

    else:
        raise SystemExit


if __name__ == "__main__":
    check_file()
    expiration()
