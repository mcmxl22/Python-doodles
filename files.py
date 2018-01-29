#! /usr/bin/env python
# By Micah M. 2018
# Files Version 1.01
# Python 3.6.4


import os.path


class Files(object):
    #Create a file and confirm it.
    def create():
        fi = Files()
        #create file.
        filename = input('Enter file name. ')
        if os.path.exists(filename) == True:
            print ('File already exists!')
            fi.create()
        f = open(filename, 'w+')
        print ('Creating file!')
        #confirm file.
        if os.path.exists(filename) == True:
            print ('Done!')
        f.close()
		
class main(object):
    def __init__(self):
        files = Files()
        Files.create()		
		
if __name__ == "__main__":
    main()
