#!/usr/bin/env python3
"""
Inventory.py Version 1.6
Requires: files.py, numli.py, clear_screen.py
Python 3.7
"""

import json
import sys
from os import path
from clear_screen import clear_screen
from files import create_files
from numli import add_numbers


def prompt(phrase):
    """Format user prompt."""
    enter = input(f"{phrase} ")
    return enter.capitalize()


def choices():
    """Give user a choice of actions."""
    inventory_actions = ["Add", "Take", "View", "Delete", "Exit"]
    add_numbers(inventory_actions)
    action_choice = prompt("What do you want to do?")
    return action_choice


def get_data():
    """Get data from file."""
    with open("inventory.json", "r+") as file:
        try:
            existing_items = json.load(file)
        except ValueError:
            existing_items = {}
            json.dump(existing_items, file, indent=4)

    return existing_items


def add_inventory():
    """Add items to inventory"""
    item = get_data()
    add_item = prompt("Enter item:")
    quantity = prompt("Enter quantity: ")

    if add_item in item:
        item[add_item] += int(quantity)
    else:
        item[add_item] = int(quantity)

    return item


def delete_item():
    """Delete items from inventory."""
    item = get_data()
    try:
        delete = prompt("Enter item to delete:")
        item.pop(delete)
    except KeyError:
        print(f"{delete} doesn't exist.")

    return item


def take_items():
    """Take items from inventory."""
    item = get_data()
    take = prompt("What did you take?")
    deduct = prompt(f"How many {take}? ")

    if take in item:
        item[take] -= int(deduct)
    else:
        print(f"{take} doesn't exist.")

    return item


def view():
    """View inventory."""
    view_item = get_data()
    return view_item


def main():
    """main"""
    while True:
        # Check for and/or create file.
        if path.exists("inventory.json"):
            pass
        else:
            create_files("inventory")

        # Get user's choice from choices().
        choice = choices()

        # Process user's choice.
        if choice in "1":
            # Add items to inventory.
            clear_screen()
            with open("inventory.json", "r+") as file:
                try:
                    add = add_inventory()
                    json.dump(add, file, indent=4)
                except ValueError:
                    print("Enter a number.")
        elif choice in "2":
            # Take items from inventory.
            clear_screen()
            taken_items = take_items()
            with open("inventory.json", "w+") as file:
                json.dump(taken_items, file, indent=4)
        elif choice in "3":
            # View all inventory.
            clear_screen()
            view_items = view()
            for k, v in view_items.items():
                print(k, "-", v)
        elif choice in "4":
            # Delete items from inventory.
            clear_screen()
            delete = delete_item()
            with open("inventory.json", "w+") as file:
                json.dump(delete, file, indent=4)
        elif choice in "5":
            clear_screen()
            sys.exit(0)


if __name__ == "__main__":
    sys.exit(main())
