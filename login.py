#!/usr/bin/env python3
"""
login Version 1
Python 3.7
"""

import numli


options = ["Register Account", "Cancel"]
numli.addnum(options)
selection1 = input("Select an option: ")

if selection1 in "1":
    Userid = input("Enter User ID: ")
    password = input("Enter Your Password: ")
    Userdata = [Userid, password]
    print("Your Account has been created.")
    chances = 3
    Balance = 0

    if chances >= 1:
        login = input("Login Id: ")
        password1 = input("Password: ")
        if login and password1 in Userdata:
            account_options = ["Account Balance", "Deposit", "Withdraw", "logout"]
            numli.addnum(account_options)
            selection2 = input("Select your option: ")

            if selection2 in "1":
                print(f"Your account balance is {Balance}")

            elif selection2 in "2":
                depositamt = int(input("Please enter amount: "))
                Balance = depositamt + Balance
                print(f"Your account balance is: {Balance}.")

            elif selection2 in "3":
                withdraw = int(input("Enter amount: "))
                if withdraw > Balance:
                    print(f"Insufficient funds! Your balance is: {Balance}")

                else:
                    Balance = Balance - withdraw
                    print(f"Your Account Balance is: {Balance}")

            else:
                print("Logging out...")

        else:
            print("Wrong Credentials")
            chances -= 1
            if chances in 1:
                print("You have one chance left!")

    else:
        print("Your Account has been blocked!")
        raise SystemExit

elif selection1 in "2":
    raise SystemExit

else:
    print("Invalid Option!")
