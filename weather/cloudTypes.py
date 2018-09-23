#!/usr/bin/env python3
'''By Micah M. 2018
   cloudTypes version 1.1
   Python 3.7'''

import webbrowser

def cloudTypes():
    '''cloudTypes'''
    clouds = ['1 Cumulus', '2 Stratus', '3 Cumulonimbus', '4 Cirus']
    cloudOptions = ['1 Cloud description', '2 Cloud image']

    print('\n'.join(cloudOptions))
    options = input('Choose an option. \n')

    if options == '1':

        print('\n'.join(clouds))
        description = input('Choose an option. \n')

        if description == '1':
            url = 'https://en.wikipedia.org/wiki/Cumulus_cloud'
            webbrowser.open(url)
        elif description == '2':
            url = 'https://en.wikipedia.org/wiki/Stratus_cloud'
            webbrowser.open(url)
        elif description == '3':
            url = 'https://en.wikipedia.org/wiki/Cumulonimbus_cloud'
            webbrowser.open(url)
        elif description == '4':
            url = 'https://en.wikipedia.org/wiki/Cirrus_cloud'
            webbrowser.open(url)
        else:
            print('Invalid Answer.')

    elif options == '2':

        print('\n'.join(clouds))
        img = input('Choose an option. \n')

        if img == '1':
            url = 'https://bit.ly/2xH55Er'
            webbrowser.open(url)
        elif img == '2':
            url = 'https://bit.ly/2xxD42N'
            webbrowser.open(url)
        elif img == '3':
            url = 'https://bit.ly/2Nwns9V'
            webbrowser.open(url)
        if img == '4':
            url = 'https://bit.ly/2xMDgKG'
            webbrowser.open(url)

        else:
            print('Invalid Answer.')

    else:
        print('Invalid Answer.')

if __name__ == "__main__":
    cloudTypes()
