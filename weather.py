#!/usr/bin/env python3
'''By Micah M. 2018
   Weather version 1.4
   Python 3.7'''


def forecast():
    '''Forecasts based on barometric pressure trends
       and logs which trend is chosen.'''
    trendOptions = ['1 Rising', '2 Falling', '3 Steady']
    print('\n'.join(trendOptions))
    trend = input('\nChoose a trend.\n> ')
    logEntry = trend  # Logs chosen option.
    file = open('trendLog.txt', 'a')
    file.write(logEntry)  # Writes log to file.
    rLog = open('trendLog.txt').read()  # Reads log from file.
    mostCommon = max(rLog, key=rLog.count) # Finds most common log entry.
    file.close()
    print(f'\nYour most common choice: {mostCommon}.')
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
    '''Formula to calculate the dew point.'''
    temp = input('\nEnter temperature in Celsius.\n> ')
    relativeHumidity = input('\nEnter relative humidity\n> ')
    formula = (int(temp) - ((100 - int(relativeHumidity)) / 5))
    print(f'\nThe dew point is {int(formula)} degrees Celsius.\n')


def cloudBase():
    '''Formula to calculate the height of the clouds.'''
    temp = input('Enter temperature in celsius.\n> ')
    dewPoint = input('Enter dew point in celsius.\n> ')
    spread = int(temp) - int(dewPoint)  # Spread = difference temp/dew point.
    cloudCeiling = int(spread) / 2.5 * 1000  # Formula to find cloud ceiling.
    print(f'The cloud ceiling is {int(cloudCeiling)} feet above the ground.')


def celsius():
    '''Formula to convert fahrenheit to celsius.'''
    convert = input('\nEnter temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32  # Formula for celsius to fahrenheit.
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')


def fahrenheit():
    '''Formula to convert celsius to fahrenheit.'''
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8  # Formula for fahrenheit to celsius
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')

def windSpeed():
    '''Formula to convert knots to MPH'''
    convert = input('Enter wind speed on knots.\n ')
    formula = ((int(convert) * 6067) / 5280)
    print(f'{convert} knots is {formula} MPH.\n')

def prompt():
    '''Prompts user to choose from a list of options and will log which option
       is chosen.'''
    while True:
        promptOptions = [
            '1 Convert from Fahrenheit', '2 Convert from Celsius',
            '3 Find Dew Point', '4 Weather Forcast', '5 Cloud Ceiling',
            '6 Convert knots to MPH', '7 Exit']
        print('\n'.join(promptOptions))
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
            windSpeed()
        elif unitChoice == '7':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')


if __name__ == "__main__":
    prompt()
