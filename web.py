#! /usr/bin/env python
# By Micah M. 2018
# web version 1.0
# Python 2.7.13


import webbrowser


def websites():

    new = 2
    choice = raw_input('Type site name:\n> ')
    site = choice
    url1 = 'www..com'
    url = 'http://' + url1[:4] + site + url1[4:]
    webbrowser.open(url, new)

if __name__ == "__main__":
    websites()
