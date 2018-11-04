#!/usr/bin/env python
'''By Micah M. 2018
   Web version 1.3
   Python 3.7'''


import webbrowser


def web_site(site):
    '''website'''
    site = input('Type site name: ')
    url = f'http://www.{site}.com'
    webbrowser.open(url)


if __name__ == "__main__":
    web_site()
