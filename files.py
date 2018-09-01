#!/usr/bin/env python3
# By Micah M. 2018
# Files Version 1.1
# Python 3.7


import os.path


class Files(object):
    # Create a file and confirm it.
    def create():
        files = Files()
        # create file.
        fileName = input('Enter file name. ')
        if os.path.exists(fileName) is True:
            print('File already exists!')
            files.create()
        f = open(fileName, 'w+')
        print('Creating file!')
        # confirm file.
        if os.path.exists(fileName) is True:
            print('Done!')
        f.close()


class main(object):
    def __init__(self):
        files = Files()
        Files.create()


if __name__ == "__main__":
    main()
