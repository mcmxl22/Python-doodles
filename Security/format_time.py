#!/usr/bin/env python3
"""
format_time Version 1.2
Python 3.7
"""


from datetime import datetime, timedelta, date


def add_three_hours():
    """Add 3 hours to current time."""
    time = datetime.now()
    future_time = time + timedelta(hours=3)
    return future_time


def add_day():
    """Add a day."""
    tomorrow = date.today() + timedelta(days=1)
    return tomorrow


if __name__ == "__main__":
    add_three_hours()
    add_day()
