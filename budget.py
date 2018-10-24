#!/usr/bin/env python
'''By Micah M. 2018
   budget version 1.2
   Python 3.7'''


balance = 0.00


def budget():
    '''budget'''
    menu = ['1 Set Ballance', '2 Add Transaction', '3 Check Balance']
    print('\n'.join(menu))
    options = input('What do you want to do? ')

    if options in '1':
        amount = float(input('Enter amount:  '))
        global balance
        balance = amount
        print(f'Current balance:{balance}')
        with open('budget.txt', 'w') as f:
            f.write(f'Balance:{balance}\n')
        f.close
        budget()

    if options in '2':
        formula = ['1 Add', '2 Subtract']
        print('\n'.join(formula))
        transaction_choice = input('Add or subtract amount?')
        if transaction_choice in '1':
            amount = float(input('Enter amount: '))
            print(f'Your new balance is:{balance + amount}\n')

        elif transaction_choice in '2':
            amount = float(input('Enter amount: '))
            print(f'Your new ballance is:{balance - amount}\n')

    if options in '3':
        file = open('budget.txt', 'r')
        print(file.read())
        file.close
        budget()

if __name__ == "__main__":
    budget()
