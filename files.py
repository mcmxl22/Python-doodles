#!/usr/bin/env python3
# By Micah M. 2018
# Files Version 1.2
# Python 3.7


import os.path


class Files(object):
    ''' Creates a file and confirms it.'''
    def create():
        files = Files()
        fileName = input('Enter file name. ')
        if os.path.exists(fileName) is True:
            print('File already exists!')
            files.create()
        f = open(fileName, 'w+')
        print('Creating file!')
        if os.path.exists(fileName) is True:
            print('Done!')
        f.close()


if __name__ == "__main__":
        files = Files()
        Files.create()
