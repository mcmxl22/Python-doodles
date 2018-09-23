#!/usr/bin/env python3
'''By Micah M. 2018
   forecast version 1.1
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
    print(f'\nYour most common choice is {mostCommon}.')
    if trend == '1':
        print('\nFairer weather on the way.\n')
    elif trend == '2':
        print('\nPoorer weather on the way.\n')
    elif trend == '3':
        print('\nNo significant change.\n')
    else:
        print('Invalid Entry!\n')
        forecast()


if __name__ == "__main__":
    forecast()
