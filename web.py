#!/usr/bin/env python3
# By Micah M. 2018
# Web version 1.2
# Python 3.7


import webbrowser


def website():

    site = input('Type site name: ')
    url = f'http://www.{site}.com'
    webbrowser.open(url)


if __name__ == "__main__":
    website()
