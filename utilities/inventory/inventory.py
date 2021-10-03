#!/usr/bin/env python3

"""
Inventory.py Version 2.7
Python 3.7
"""


import json
from os import path, system
from sys import platform


def clear_screen():
    """Clear the screen."""
    if platform in "win32":
        system("cls")

    else:
        system("clear")


def get_data() -> dict:
    """Get Json data from file."""
    with open("inventory.json", "r+") as file:
        try:
            existing_items = json.load(file)

        except ValueError:
            existing_items = {}
            json.dump(existing_items, file, indent=4)

    return existing_items


class Inventory_file:
    """Check and/or create inventory file."""
    def create_inventory_file():
        """Create file"""
        with open("inventory.json", "w+"):
            if path.exists("inventory.json"):
                print(f"inventory.json created!")
            else:
                return


    def check_inventory_file():
        """Check if file exists"""
        if path.exists("inventory.json"):
            pass
        else:
            Inventory_file.create_inventory_file()


class Menu:
    """Prepare a menu."""
    def add_numbers(num):
        """Add numbers to menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)


    def list_choices() -> list:
        """Give user a choice of actions."""
        inventory_actions = ["Add", "Take", "View", "Delete", "Exit"]
        Menu.add_numbers(inventory_actions)
        action_choice = input("What do you want to do? ")
        return action_choice


class Inventory:
    """Add, remove and view inventory."""
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

        except ValueError as e:
            print(e)

        clear_screen()
        return item


    def delete_item():
        """Delete items from inventory."""
        item = get_data()

        try:
            if item == {}:
                print("Nothing to delete.")
                pass

            else:
                delete = input("Enter item to delete: ")
                item.pop(delete)
                print(f"{delete} deleted!\n")
                with open("inventory.json", "w") as file:
                    json.dump(item, file, indent=4)

        except KeyError as e:
            print(e)

        return item


    def take_items():
        """Take items from inventory."""
        item = get_data()
        if item == {}:
            print("No inventory available!\n")


        else:
            try:
                take = input("What did you take? ")
                deduct = int(input(f"How many {take}? "))

                if deduct > item[take]:
                    print(f"Not enough {take} available!\n")
                elif take in item:
                    item[take] -= deduct
                    print(f"{item[take]} {take} left!\n")
                else:
                    print(f"{take} doesn't exist.\n")

            except ValueError:
                print("Invalid entry!\n")

        return item


    def view_items():
        """View items from inventory."""
        view_items = get_data()
        if view_items == {}:
            print("No inventory available!\n")

        else:
            for item, view in view_items.items():
                if view < 1:
                    print("No inventory available!\n")
                else:
                    print(item, "=", view)
            print("\n")


def main():
    """main"""
    while True:
        Inventory_file.check_inventory_file()
        choice = Menu.list_choices()

        # Process user's choice.
        if choice in "1":
            # Add items to inventory.
            clear_screen()
            with open("inventory.json", "r+") as file:
                add = Inventory.add_inventory()
                json.dump(add, file, indent=4)

        elif choice in "2":
            # Take items from inventory.
            clear_screen()
            taken_items = Inventory.take_items()
            with open("inventory.json", "w") as file:
                json.dump(taken_items, file, indent=4)

        elif choice in "3":
            clear_screen()
            Inventory.view_items()

        elif choice in "4":
            clear_screen()
            Inventory.delete_item()

        elif choice in "5":
            clear_screen()
            exit(0)

        else:
            clear_screen()
            print("Invalid entry.")
            choice = Menu.list_choices()
            


if __name__ == "__main__":
    clear_screen()
    main()
