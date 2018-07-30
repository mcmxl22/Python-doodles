#! /usr/bin/env python
# By Micah M. 2018
# weather version 1.2
# Python 3.7



def dewPoint():
    t = input('\nEnter the temperature in Celsius.\n> ')
    rh = input ('\nEnter the relative humidity\n> ')
    formula = (int(t) - ((100 - int(rh)) / 5))
    print(f'\nThe dew point is {int(formula)} degrees Celsius.\n')

def celsius():
    convert = input('\nEnter the temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')

def fahrenheit():
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')

def prompt():
    	while True:    
            options = ('1 Convert from Fahrenheit', '2 Convert from Celsius', '3 Find Dew Point', '4 Exit')
            print('\n'.join(options))
            unitChoice = input('\nWhat would you like to do?\n> ')
            if unitChoice == '1':
                fahrenheit()
            elif unitChoice == '2':
                celsius()
            elif unitChoice == '3':
                dewPoint()
            elif unitChoice == '4':
                raise SystemExit
            else:
                print('\nInvalid Entry\n')

prompt()
