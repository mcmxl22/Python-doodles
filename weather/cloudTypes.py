#!/usr/bin/env python3
'''By Micah M. 2018
   cloudTypes version 1
   Python 3.7'''


def cloudTypes():
    '''under development'''
    clouds = ['1 Cumulus', '2 Stratus', '3 Cumulonimbus', '4 Cirus', '5 Back']
    cloudOptions = ['1 Cloud description', '2 Cloud image']
    print('\n'.join(cloudOptions))
    input('Choose an option. \n')
    if cloudOptions == '1':
        print('\n'.join(clouds))
        description = input('Choose an option. \n')
        if desription == '1':
            print('Cumulus clouds are...')
        elif desription == '2':
            print('Stratus clouds are...')
        elif desription == '3':
            print('Cumulonimbus clouds are...')
        elif desription == '4':
            print('Cirus clouds are...')
        prompt()
    elif cloudOptions == '2':
        print('\n'.join(clouds))
        picture = input('Choose an option. \n')
        if picture == '1':
            #webbrowser.open('')
            pass
        elif picture == '2':
            #webbrowser.open('')
            pass
        elif picture == '3':
            #webbrowser.open('')
            pass
        elif picture == '4':
            #webbrowser.open('')
            pass

if __name__ == "__main__":
    cloudTypes()
