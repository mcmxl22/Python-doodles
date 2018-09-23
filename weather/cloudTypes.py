#!/usr/bin/env python3
'''By Micah M. 2018
   cloudTypes version 1
   Python 3.7'''

import webbrowser

def cloudTypes():
    '''under development'''
    clouds = ['1 Cumulus', '2 Stratus', '3 Cumulonimbus', '4 Cirus']
    cloudOptions = ['1 Cloud description', '2 Cloud image']

    print('\n'.join(cloudOptions))
    options = input('Choose an option. \n')

    if options == '1':

        print('\n'.join(clouds))
        description = input('Choose an option. \n')

        if desription == '1':
            url = 'https://en.wikipedia.org/wiki/Cumulus_cloud'
            webbrowser.open(url)
        elif desription == '2':
            url = 'https://en.wikipedia.org/wiki/Stratus_cloud'
            webbrowser.open(url)
        elif desription == '3':
            url = 'https://en.wikipedia.org/wiki/Cumulonimbus_cloud'
            webbrowser.open(url)
        elif desription == '4':
            url = 'https://en.wikipedia.org/wiki/Cirrus_cloud'
            webbrowser.open(url)
        else:
            print('Invalid Answer.')

    elif options == '2':

        print('\n'.join(clouds))
        img = input('Choose an option. \n')

        if picture == '1':
            url = 'https://en.wikipedia.org/wiki/Cumulus_mediocris_cloud#/media/File:Mt_Eden,_Auckland2.jpg'
            webbrowser.open(url)
        elif picture == '2':
            url = 'https://en.wikipedia.org/wiki/Stratus_cloud#/media/File:Stratus-Opacus-Uniformis.jpg'
            webbrowser.open(url)
        elif picture == '3':
            url = 'https://en.wikipedia.org/wiki/Cumulonimbus_cloud#/media/File:Fly00890_-_Flickr_-_NOAA_Photo_Library.jpg'
            webbrowser.open(url)
        if img == '4':
            url = 'https://en.wikipedia.org/wiki/Cirrus_cloud#/media/File:CirrusField-color.jpg'
            webbrowser.open(url)

        else:
            print('Invalid Answer.')

    else:
        print('Invalid Answer.')

if __name__ == "__main__":
    cloudTypes()
