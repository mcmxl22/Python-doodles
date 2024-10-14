"""
pip_up version 1.9
Python 3.7
"""

from os import system


def pkg_update():
    """Update pip packages."""
    while True:
        print("1 Yes")
        print("2 Exit")

        choice = input("Check for updates? ")

        if choice == "1":
            print("Checking for updates...")
            system("pip-review --local --interactive")
        else:
            try:
                system("cls")
            except OSError:
                system("clear")

            exit()


if __name__ == "__main__":
    pkg_update()
