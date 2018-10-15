#! /usr/bin/env python3
'''By Micah M. 2018
   Files Version 1.3
   Python 3.7'''

import os.path


def files():
    '''Create a file and/or confirm it.'''
    while True:
        file_name = input('Enter file name.\n> ')
        if os.path.exists(file_name) is True:
            print(f'{file_name} already exists!')
        else:
            f = open(file_name, 'w+')
            print('Creating file!')
            if os.path.exists(file_name) is True:
                print('Done!')
            f.close()


if __name__ == "__main__":
    files()
