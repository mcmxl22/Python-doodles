#! /usr/bin/env python
# By Micah M. 2017
# web version 1.01
# Python 3.6.4


import webbrowser


def websites():
    new = 2
    choice = input('Type site name:\n> ')
    site = choice
    url1 = 'www..com'
    url = 'http://' + url1[:4] + site + url1[4:]
    webbrowser.open(url, new)


if __name__ == "__main__":
    websites()
