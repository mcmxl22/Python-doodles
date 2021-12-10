#!/usr/bin/env python3
"""
numli Version 1.2
Python 3.7
"""


class Menu:
    """
    Prepare a menu. 
    Example: Menu.list_choices(['Cat','Dog'])
    Output:
    1 Cat
    2 Dog
    """
    def add_numbers(num):
        """Add numbers to the menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)


    def list_choices(choose_conversion, **kwargs: list):
        """Give user a choice of actions."""
        return Menu.add_numbers(choose_conversion)
