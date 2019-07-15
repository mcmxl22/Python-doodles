print("""Welcome, Please select (1) for registering new account
         press (2) for cancel""")

selection1 = int(input("Please select one option: "))

if selection1 in 1:
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
        if login Userdata and password1 in Userdata:
            print("""Welcome, Please select 
            (1) for Account Balance
            (2) for Deposit
            (3) for Withdraw
            (4) for logout
            """)
            selection2 = int(input("Select your option: "))
            if selection2 not in (1, 2, 3, 4):
                print("Please select (1) or (02) or (03) or (4) only")

            else:
                if selection2 in 1:
                    print(f"Your account balance is {Balance}")
                    
                elif selection2 in 2:
                    depositamt = int(input("Please enter amount: "))
                    Balance = depositamt + Balance
                    print(f"Your account balance is: {Balance}.") 
                    
                elif selection2 in 3:
                    withdraw = int(input("Enter amount: "))
                    if withdraw > Balance:
                        print(f"Insufficient Funds! Your balance is: {Balance}")

                    else:
                        Balance = Balance - withdraw
                        print(f"Your Account Balance is: {Balance}") 

                else selection2 in 4:
                    print("Logging out...")

        else:
            print("Wrong Credentials")
            chances -= 1
            if chances in 1:
                print("You have only one chance left")

    else:
        print("Your Account has been blocked")
        exit(99)

if selection1 in 2:
    print("Exiting...")
    raise SystemExit

else:
    print("Select (1) or (2) only")