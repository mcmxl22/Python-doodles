#!/usr/bin/env python3
"""
format_time Version 1
Python 3.7
"""

import datetime


DATE = datetime.datetime.now()

def format_3hour(three_hour):
    """Extracts time of day and adds 3 hours."""
    three_hour = DATE + datetime.timedelta(0, 10800)
    time = list(str(three_hour))
    del time[0:11], time[4:14]
    new_time = "".join(time)
    return new_time


def format_time():
    """Extracts time of day."""
    future_time = DATE + datetime.timedelta(0)
    time = list(str(future_time))
    del time[0:11], time[4:14]
    new_time = "".join(time)
    return new_time


if __name__ == "__main__":
    format_3hour("three")
    format_time()
