"""
pip_up version 1.8
Python 3.7
"""

from subprocess import run
import os


def pkg_update():
    """Update pip packages."""
    while True:
        print("1 Yes")
        print("2 Exit")

        choice = input("Check for updates? ")

        if choice in "1":
            print("Checking for updates...")
            run("pip-review --local --interactive", check=True)
        else:
            try:
                os.system("cls")
            except OSError:
                os.system("clear")

            exit()


if __name__ == "__main__":
    pkg_update()
