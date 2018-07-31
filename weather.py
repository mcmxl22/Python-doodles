#! /usr/bin/env python
# By Micah M. 2018
# Weather version 1.3
# Python 3.7


def forecast():
    '''Gives a forecast based on barometric pressure trends
       and logs which trend is choosen.'''
    options = ['1 Rising', '2 Falling', '3 Steady']
    print('\n'.join(options))
    trend = input('\nChoose a barometric pressure trend.\n> ')
    logEntry = trend  # Logs chosen option.
    file = open('forecastLog.txt', 'a')
    file.write(logEntry)  # Writes log to file.
    rLog = open('forecastLog.txt').read()  # Reads log from file.
    most_common = max(rLog, key=rLog.count)  # Finds most common log entry.
    file.close()
    print(f'\nYour most common choice is {most_common}.')
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
    '''Uses a formula to calculate the dew point.
       t = temperature, rh = relative humidity'''
    t = input('\nEnter the temperature in Celsius.\n> ')
    rh = input('\nEnter the relative humidity\n> ')
    formula = (int(t) - ((100 - int(rh)) / 5))  # Formula to find dew point.
    print(f'\nThe dew point is {int(formula)} degrees Celsius.\n')


def cloudBase():
    '''Uses a formula to calculate the height of the clouds.'''
    temp = input('Enter current temperature in celsius.\n> ')
    dp = input('Enter current dew point in celsius.\n> ')  # dp = dew point.
    spread = int(temp) - int(dp)  # Spread = difference of temp and dew point.
    cloudCeiling = int(spread) / 2.5 * 1000  # Formula to find cloud ceiling.
    print(f'The cloud ceiling is {int(cloudCeiling)} feet above ground level.')
    
    
def celsius():
    '''Uses a formula to convert fahrenheit to celsius.'''
    convert = input('\nEnter the temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32  # Formula for celsius to fahrenheit.
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')


def fahrenheit():
    '''uses a formula to convert celsius to fahrenheit.'''
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8  # Formula for fahrenheit to celsius
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')


def prompt():
    '''Prompts user to choose from a list of options and logs which option
       is choosen.'''
    while True:
        options = ['1 Convert from Fahrenheit', '2 Convert from Celsius',
                   '3 Find Dew Point', '4 Weather Forcast', '5 Cloud Ceiling',
                   '6 Exit']
        print('\n'.join(options))
        unitChoice = input('\nWhat would you like to do?\n> ')
        if unitChoice == '1':
            fahrenheit()
        elif unitChoice == '2':
            celsius()
        elif unitChoice == '3':
            dewPoint()
        elif unitChoice == '4':
            forecast()
        elif unitChoice == '5':
            cloudBase()
        elif unitChoice == '6':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')


class main(object):
    def __init__(self):
        prompt()


if __name__ == "__main__":
    main()
