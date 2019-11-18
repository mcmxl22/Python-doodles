#!/usr/bin/env python3
"""
budget version 1.3
Python 3.7
"""

import numli


balance = 0.00

def budget():
    """budget"""
    menu_options = ["Set Balance", "Add Transaction", "Check Balance"]
    numli.addnum(menu_options)
    menu_choice = input("What do you want to do? ")

    if menu_choice in "1":
        amount = float(input("Enter amount:  "))
        global balance
        balance = amount
        print(f"Current balance:{balance}")
        with open("budget.txt", "w") as f:
            f.write(f"Balance:{balance}\n")
        budget()

    if menu_choice in "2":
        transaction_options = ["Add", "Subtract"]
        numli.addnum(transaction_options)
        transaction_choice = input("Add or subtract amount?")
        if transaction_choice in "1":
            amount = float(input("Enter amount: "))
            print(f"Your new balance is:{balance + amount}\n")

        elif transaction_choice in "2":
            amount = float(input("Enter amount: "))
            print(f"Your new ballance is:{balance - amount}\n")

    if menu_choice in "3":
        with open("budget.txt", "r") as f:
            print(f.read())
        budget()


if __name__ == "__main__":
    budget()
