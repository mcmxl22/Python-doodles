#!/usr/bin/env python
'''By Micah M. 2018
   Web version 1.2
   Python 3.7'''


import webbrowser


def web_site():
    '''website'''
    site_name = input('Type site name: ')
    make_url = f'http://www.{site}.com'
    webbrowser.open(make_url)


if __name__ == "__main__":
    web_site()
