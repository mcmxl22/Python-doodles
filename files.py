#By Micah M. 2017 
#Files Version 1.0            
#Python 2.7.12

import os.path

class Files(object):
    #Create a file and confirm it.
    def create(self):
        #create file.
        filename = raw_input('Enter file name. ')
        f = open(filename, 'w+')
        print ('Creating file!')
        #confirm file.
        if os.path.exists(filename) == True:
            print ('Done!')
        f.close()

	#Edit a file.
    def edit(self):
        FileOpen = raw_input('Enter file name. ')
        f = open(FileOpen, 'w')
        FileEdit = raw_input('> ')
        f.write(FileEdit)
        #...
        f.close()
        print ('Done!')

class questions(object):

    def start(self):

        Start_Actions = ('1 Create file',
        '2 Edit file', '3 Exit')

        for i in Start_Actions:
            print ('%s' % i)
        Ask = raw_input('Choose an option. ')
        f = Files()
        if Ask == '1':
            f.create()

        elif Ask == '2':
            f.edit()

        elif Ask == '3':
           quit()

        else:
            print ('Invalid entry!')
            start()
		
class main(object):
    def __init__(self):
        q = questions()
        q.start()   

main()
