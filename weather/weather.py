#!/usr/bin/env python3
'''By Micah M. 2018
   Weather version 1.6
   Python 3.7
   Requires forecast.py and cloudTypes.py'''

import subprocess
import sys

def dew_point():
    '''Formula to calculate the dew point.'''
    temp = input('\nEnter temperature in Celsius.\n> ')
    relative_humidity = input('\nEnter relative humidity\n> ')
    formula = (int(temp) - ((100 - int(relative_humidity)) / 5))
    print(f'\nThe dew point is {int(formula)} degrees Celsius.\n')


def cloud_base():
    '''Formula to calculate the height of the clouds.'''
    temp = input('Enter temperature in celsius.\n> ')
    dew = input('Enter dew point in celsius.\n> ')
    spread = int(temp) - int(dew)  # Spread = difference temp and dew point.
    cloud_ceiling = int(spread) / 2.5 * 1000  # Formula to find cloud ceiling.
    print(f'The cloud ceiling is {int(cloud_ceiling)} feet above the ground.\n')


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


def wind_speed():
    '''Formula to convert knots to MPH'''
    convert = input('Enter wind speed in knots.\n ')
    formula = ((int(convert) * 6067) / 5280)
    print(f'{convert} knots is {round(formula, 3)} MPH.\n')



def prompt():
    '''Prompts user to choose from a list of options and logs which option
       is chosen.'''
    while True:
        prompt_options = [
            '1 Convert from Fahrenheit', '2 Convert from Celsius',
            '3 Find Dew Point', '4 Weather Forcast', '5 Cloud Ceiling',
            '6 Convert knots to MPH', '7 Cloud Types', '8 Exit']

        print('\n'.join(prompt_options))
        unit_choice = input('\nWhat would you like to do?\n> ')
        log_entry = unit_choice  # Logs chosen option.
        file = open('promptLog.txt', 'a')
        file.write(log_entry)  # Writes log to file.
        read_log = open('promptLog.txt').read()  # Reads log from file.
        most_common = max(read_log, key=read_log.count) # Finds most common log entry.
        file.close()
        print(f'\nYour most common choice is {most_Common}.')


        if unit_choice == '1':
            fahrenheit()
        elif unit_choice == '2':
            celsius()
        elif unit_choice == '3':
            dew_point()
        elif unit_choice == '4':
            forecast = [sys.executable, 'forecast.py']
            subprocess.call(forecast)
        elif unit_choice == '5':
            cloud_base()
        elif unit_choice == '6':
            wind_speed()
        elif unit_choice == '7':
            cloud_types = [sys.executable, 'cloudTypes.py']
            subprocess.call(cloud_types)
        elif unit_choice == '8':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')



if __name__ == "__main__":
    prompt()
