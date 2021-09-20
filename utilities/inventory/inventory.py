#!/usr/bin/env python3

"""
Inventory.py Version 2.2
Requires: numli.py, clear_screen.py
Python 3.7
"""


import json
from os import path
from clear_screen import clear_screen
from numli import add_numbers


def create_inventory_file():
    """Create file"""
    name = "inventory.json"

    with open(name, "w+"):
        if path.exists(name):
            print(f"{name} created!")
        else:
            return


def choices() -> list:
    """Give user a choice of actions."""
    inventory_actions = ["Add", "Take", "View", "Delete", "Exit"]
    add_numbers(inventory_actions)
    action_choice = input("What do you want to do? ")
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


def add_inventory() -> str:
    """Add items to inventory."""
    item = get_data()

    try:
        add_item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))

        if add_item in item:
            item[add_item] += quantity
        else:
            item[add_item] = quantity

    except ValueError:
        print("Please enter a valid item.")

    return item


def delete_item():
    """Delete items from inventory."""
    item = get_data()
    try:
        delete = input("Enter item to delete: ")
        item.pop(delete)
    except KeyError:
        print(f"{delete} doesn't exist.")

    return item


def take_items():
    """Take items from inventory."""
    item = get_data()

    try:
        take = input("What did you take? ")
        deduct = int(input(f"How many {take}? "))

        if take in item:
            item[take] -= deduct
        else:
            print(f"{take} doesn't exist.")

    except ValueError:
        print("Please enter a valid item.")

    return item


def main():
    """main"""
    while True:
        # Check for and/or create file.
        if path.exists("inventory.json"):
            pass
        else:
            create_inventory_file()

        # Get user's choice from choices().
        choice = choices()

        # Process user's choice.
        if choice in "1":
            # Add items to inventory.
            clear_screen()
            with open("inventory.json", "r+") as file:
                add = add_inventory()
                json.dump(add, file, indent=4)

        elif choice in "2":
            # Take items from inventory.
            clear_screen()
            taken_items = take_items()
            with open("inventory.json", "w") as file:
                json.dump(taken_items, file, indent=4)

        elif choice in "3":
            # View all inventory.
            clear_screen()
            view_items = get_data()
            if view_items == {}:
                print("No inventory available")
            else:
                for item, view in view_items.items():
                    print(item, "=", view)

        elif choice in "4":
            # Delete items from inventory.
            clear_screen()
            delete = delete_item()
            with open("inventory.json", "w") as file:
                json.dump(delete, file, indent=4)

        elif choice in "5":
            clear_screen()
            exit(0)


if __name__ == "__main__":
    exit(main())
