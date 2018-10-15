#!/usr/bin/env python3
'''By Micah M. 2018
   Files Version 1.3
   Python 3.7'''


import os.path


def files():
'''Create a file and/or confirm it.'''
    fileName = input('Enter file name.\n> ')
    if os.path.exists(fileName) is True:
        print(f'File {fileName} already exists!')
        Files.create()
    f = open(fileName, 'w+')
    print('Creating file!')
    if os.path.exists(fileName) is True:
        print('Done!')
    f.close()


if __name__ == "__main__":
    files()
