#!/usr/bin/env python3
'''By Micah M. 2018
   forecast version 1.1
   Python 3.7'''

def forecast():
    '''Forecasts based on barometric pressure trends
       and logs which trend is chosen.'''
    trend_options = ['1 Rising', '2 Falling', '3 Steady']
    print('\n'.join(trend_options))

    trend = input('\nChoose a trend.\n> ')
    log_entry = trend  # Logs chosen option.
    file = open('trendLog.txt', 'a')
    file.write(log_entry)  # Writes log to file.
    read_log = open('trendLog.txt').read()  # Reads log from file.
    most_common = max(read_log, key=read_log.count) # Finds most common log entry.
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


if __name__ == "__main__":
    forecast()
