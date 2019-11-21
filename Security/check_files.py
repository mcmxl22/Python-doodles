#!/usr/bin/env python3
"""
check_files Version 1
Python 3.7
"""

import os.path


def transfer_file():
    """Check if file exists."""
    if os.path.exists("transfer.txt"):
        return
    else:
        with open("transfer.txt", "w") as file:
            return


def code_file():
    """Check if file exists."""
    if os.path.exists("code.txt"):
        return
    else:
        with open("code.txt", "w") as file:
            return

if __name__ == "__main__":
    transfer_file()
    code_file()
