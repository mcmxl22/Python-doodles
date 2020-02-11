#!/usr/bin/env python3
"""
format_time Version 1.1
Python 3.7
"""

from datetime import datetime, timedelta


DATE = datetime.now()

def format_3hour(three_hour):
    """gets time of day and adds 3 hours."""
    three_hours = DATE + timedelta(hours=3)
    new_time = format(three_hours, "%H:%M")
    print(new_time)


def format_time():
    """Extracts time of day."""
    time = DATE.strftime("%H:%M")
    print(time)


if __name__ == "__main__":
    format_3hour("three")
    format_time()
