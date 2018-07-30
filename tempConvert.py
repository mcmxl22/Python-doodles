#! /usr/bin/env python
# By Micah M. 2018
# tempConvert version 1.2
# Python 3.7



#class Conversion(object):
def celsius():
    convert = input('\nEnter the temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')

def fahrenheit():
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')
		
#class Main(object):
def prompt():

    	while True:
            options = ('1 Fahrenheit', '2 Celsius', '3 Exit')
            print('\n'.join(options))
            unitChoice = input('\nWhat unit would you like to convert from?\n> ')
            if unitChoice == '1':
                fahrenheit()
            elif unitChoice == '2':
                celsius()
            elif unitChoice == '3':
                raise SystemExit
            else:
                print('Invalid Entry')



#if __name__ == "__main__":
#m = Main()
prompt()
