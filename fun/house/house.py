#!/usr/bin/env python3

"""
House version 1.5
requires: numli.py, count_down.py
Python 3.7
"""

import sys
from count_down import count
from numli import add_numbers
from time import sleep
from web import get_web_site


def porch():
    """porch"""
    while True:
        porch_options = ["Front", "Exit"]
        add_numbers(porch_options)

        porch_choice = input("Choose an option. ")

        if porch_choice in "1":
            living_room()

        elif porch_choice in "2":
            sys.exit(0)

        else:
            print("Invalid answer!")


def stairs():
    """stairs"""
    while True:
        for i in range(1, 7):
            print(i)
        hall_choice = input(
            """\nYou're in the upstairs hall.
                               \rChoose a door. """
        )

        if hall_choice in ["1", "2", "3", "5"]:
            print("This door is locked.")

        elif hall_choice in ["4", "6"]:
            print("This room is empty.")

        else:
            living_room()


def kitchen():
    """kitchen"""
    pass


def basement():
    """basement"""
    while True:
        laundry_option = ["Yes", "No"]
        add_numbers(laundry_option)
        laundry = input("Do you want to do laundry? ")

        if laundry in "1":
            quarters = int(input("How many quarters do you have? "))

            if quarters < 8:
                print(f"{quarters} is not enough money.")

            elif quarters >= 8:
                print("Washing!")
                sleep(3)
                print("Drying!")
                sleep(6)
                print("Done!")

        else:
            living_room()


def living_room():
    """living_room"""
    while True:
        room_select = [
            "Kitchen",
            "Stairs",
            "Porch",
            "Basement",
            "Browse",
            "Rest",
            "Weather",
        ]
        add_numbers(room_select)
        room_choice = input(
            """\nThis is the living room.
                               \rChoose a room or activity. """
        )

        if room_choice in "1":
            kitchen()

        elif room_choice in "2":
            stairs()

        elif room_choice in "3":
            porch()

        elif room_choice in "4":
            basement()

        elif room_choice in "5":
            get_web_site(room_choice)

        elif room_choice in "6":
            count(room_choice)

        else:
            print("Invalid Answer.")


if __name__ == "__main__":
    sys.exit(porch())
