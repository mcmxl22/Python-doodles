#!/usr/bin/env python3
"""
pip_up version 1
requires: numli.py
Python 3.7
"""

import numli
import os


def pkg_update():
    """Update pip packages."""
    options = ['Yes', 'Exit']
    numli.addnum(options)
    choice = input('Check for updates? ')

    if choice in '1':
        print('Checking for updates.')
        results = os.system('pip list -o')

        os.system('pip-review --local --interactive')
        pkg_update()

    elif choice in '2':
        raise SystemExit

    else:
        pkg_update()


if __name__ == "__main__":
    pkg_update()
