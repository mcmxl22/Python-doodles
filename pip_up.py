#!/usr/bin/env python3
"""
pip_up version 1
Python 3.7.3
"""

import os
import subprocess


def pkg_update():
    """Update pip packages."""
    options = ['1. Yes', '2. Exit']
    for option in options:
        print(option)
    choice = input('Check for updates? ')

    if choice in '1':
        print('Checking for updates.')
        results = os.system('pip list -o')

        if results == None:
            print('All packages are up to date.\n')
            pkg_update()

        else:
            os.system('pip-review --local --interactive')
            pkg_update()

    elif choice in '2':
        raise SystemExit

    else:
        pkg_update()


if __name__ == "__main__":
    pkg_update()
