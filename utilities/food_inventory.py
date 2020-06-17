#!/usr/bin/env python3
"""
food_inventory.py version 1
Python 3.7
"""

import json
import sys
from numli import add_numbers


with open("food.json", "r+") as file:
    try:
        food = json.load(file)
    except:
        food = {}
        json.dump(food, file)

inventory_actions = ["Add", "Eat", "View", "Exit"]
add_numbers(inventory_actions)
action_choice = input("What do you want to do? ")

if action_choice in "1":
    add = input("Enter item: ")
    quantity = input("Enter quantity: ")
    if add in food:
        food[add] += int(quantity)
    else:
        food[add] = int(quantity)

elif action_choice in "2":
    eat = input("What did you eat? ")
    deduct = input("how many? ")
    if eat in food:
        food[eat] -= int(deduct)
    else:
        pass

elif action_choice in "3":
    view_item = input("Enter item to view: ")
    if view_item in food:
        print(f"you have {food[view_item]} {view_item}")
    else:
        print(f"{view_item} does not exist.")

elif action_choice in "4":
    sys.exit(0)
else:
    pass


with open("food.json", "w") as file:
    file.seek(0)
    json.dump(food, file)
