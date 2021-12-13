#!/usr/bin/env python3
"""
numli Version 1.3
Python 3.7
"""


class Menu:
    """
    Create a menu. 
    Example: Menu.list_choices(['Cat','Dog'])
    Output:
    1 Cat
    2 Dog
    """
    def add_numbers(num):
        """Add numbers to the menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)


    def list_choices(options_list, **kwargs: list):
        """Give user a choice of actions."""
        return Menu.add_numbers(options_list)
