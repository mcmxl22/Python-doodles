#! /usr/bin/env python
# By Micah M. 2018
# Weather version 1.3
# Python 3.7


def forecast():
    '''Produces a forecast based on barometric pressure trends
       and logs which trend is choosen.'''
    options = ['1 Rising', '2 Falling', '3 Steady']
    print('\n'.join(options))
    trend = input('\nChoose a trend for the barometric pressure.\n> ')
    logEntry = f'{trend}'
    f = open('forecastLog.txt', 'a')
    f.write(f'{logEntry}')
    look = open('forecastLog.txt').read()
    most_common = max(look, key = look.count)
    print(f'\n{most_common}')
    if trend == '1':
        print('\nFairer weather on the way.\n')
    elif trend == '2':
        print('\nPoorer weather on the way.\n')
    elif trend == '3':
        print('\nNo significant change.\n')
    else:
        print('Invalid Entry!\n')
        forecast()


def dewPoint():
    '''Uses a formula to find the dew point. 
       t = temperature, rh = relative humidity'''
    t = input('\nEnter the temperature in Celsius.\n> ')
    rh = input('\nEnter the relative humidity\n> ')
    formula = (int(t) - ((100 - int(rh)) / 5))
    print(f'\nThe dew point is {int(formula)} degrees Celsius.\n')


def celsius():
    '''Uses a formula to convert fahrenheit to celsius.'''
    convert = input('\nEnter the temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')


def fahrenheit():
    '''uses a formula to convert celsius to fahrenheit.'''
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')


def prompt():
    '''Prompts user to choose from a list of options and logs which options
       is choosen.'''
    while True:
        options = ['1 Convert from Fahrenheit', '2 Convert from Celsius',
                   '3 Find Dew Point', '4 Weather forcast', '5 Exit']
        print('\n'.join(options))
        unitChoice = input('\nWhat would you like to do?\n> ')
        logEntry = f'prompt{unitChoice}'
        if unitChoice == '1':
            fahrenheit()
        elif unitChoice == '2':
            celsius()
        elif unitChoice == '3':
            dewPoint()
        elif unitChoice == '4':
            forecast()
        elif unitChoice == '5':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')

class main(object):
    def __init__(self):
        prompt()


if __name__ == "__main__":
    main()
