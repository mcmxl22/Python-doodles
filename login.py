print("""Welcome, Please select (1) for registering new account
         press (2) for cancel""")

selection1 = input("Please select an option: ") # You don't need int() here because you won't be doing math.

# When selection1 is entered as a string you can use in instead of ==.
if selection1 in '1': # Putting the 1 in quotes make it a string so you don't need int() in selection1.
    Userid = input("Enter User ID: ")
    password = input("Enter Your Password: ")
    Userdata = [Userid, password]
    print("Your Account has been created")
    print("You will be logout automatically")
    chances = 3
    Balance = 0

    if chances >=1:
        login = input("Login Id: ")
        password1 = input("Password: ")
        if login and password1 in Userdata:
            print("""Welcome, select an option.
            (1) Account Balance
            (2) Deposit
            (3) Withdraw
            (4) logout
            """)
            selection2 = int(input("Select your option: "))
            if selection2 not in range(1,5):
                print("Please select (1) or (02) or (03) or (4) only")

            else:
                if selection2 == 1:
                    print(f"Your account balance is {Balance}") # this is an f-string. It's a simple way of inserting variables in string
                    
                elif selection2 == 2:
                    depositamt = int(input("Please enter amount: "))
                    Balance = depositamt + Balance
                    print(f"Your account balance is: {Balance}.") 
                    
                elif selection2 == 3:
                    withdraw = int(input("Enter amount: "))
                    if withdraw > Balance:
                        print(f"Insufficient Funds! Your balance is: {Balance}")

                    else:
                        Balance = Balance - withdraw
                        print(f"Your Account Balance is: {Balance}") 

                else:
                    print("Logging out...")

        else:
            print("Wrong Credentials")
            chances -= 1
            if chances in 1:
                print("You have only one chance left")

    else:
        print("Your Account has been blocked")
        exit(99)

if selection1 in '2':
    print("Exiting...")
    raise SystemExit

else:
    print("Select (1) or (2) only")
