#!/usr/bin/env python3
"""
log_in Version 1
Python 3.7
"""
import numli


def create_login():
    options = ["Create Account", "Cancel"]
    numli.addnum(options)
    selection1 = input("Select an option: ")

    if selection1 in "1":
        Userid = input("Enter User ID: ")
        password = input("Enter Your Password: ")
        Userdata = [Userid, password]
        print("Your Account has been created.")
        chances = 3
        if chances >= 1:
            login = input("Login Id: ")
            password1 = input("Password: ")
            if login and password1 in Userdata:
                pass
            else:
                pass


    else:
        raise SystemExit


if __name__ == "__main__":
    create_login()
