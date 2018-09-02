#!/usr/bin/env python3
# By Micah M. 2018
# budget version 1.2
# Python 3.7


balance = 0.00


def budget():

    menu = ('1 Set Ballance', '2 Add Transaction', '3 Check Balance')
    print('\n'.join(menu))
    options = input('What do you want to do?\n> ')

    if options in {'1'}:
        amount = float(input('Enter amount:\n> '))
        global balance
        balance = amount
        print(f'Current balance:{balance}')
        with open('budget.txt', 'w') as f:
            f.write(f'Balance:{balance}\n')
        f.close
        budget()

    if options in {'2'}:
        print('Add or subtract amount?')
        formula = input('1 Add\n2 Subtract\n> ')
        if formula == '1':
            amount = float(input('Enter amount:\n> '))
            print(f'Your new balance is:{balance + amount}\n')

        elif formula == '2':
            amount = float(input('Enter amount:\n> '))
            print(f'Your new ballance is:{balance - amount}\n')

    if options in {'3'}:
        file = open('budget.txt', 'r')
        print(file.read())
        file.close
        budget()

budget()
