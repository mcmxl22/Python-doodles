#By Micah M. 2017


import os.path


def files():
    filename = raw_input('Enter file name. ')
    file = open(filename, 'w+')
    print ('Creating file!')
    if os.path.exists(filename) == True:
        print ('Done!')
    file.close()
    
files()

