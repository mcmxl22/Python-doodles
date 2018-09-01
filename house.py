#!/usr/bin/env python3
# By Micah M. 2018
# House version 1.2
# Python 3.7


import subprocess
import sys
from time import sleep


'''This program requires web.py and countDown.py'''
def Porch():

    while True:
        choice = input('\nChoose a door. \n1 front \n2 exit \n>')
        if choice == '1':
            livingRoom()
        elif choice == '2':
            raise SystemExit
        else:
            print('That is not a valid answer.')


def stairs():

    while True:
        for i in range(1, 7):
            print(f'{i}')
        choice = input('''\nYou\'re in the upstairs hall.
                       \rThere are 6 doors. Choose one. > ''')
        if choice in {'1', '2', '3', '5'}:
            print('This door is locked.')
        elif choice in {'4', '6'}:
            print('This room is empty.')
        else:
            livingRoom()


def kitchen():

    print('The kitchen is being remodeled. Come back later.')
    livingRoom()


def basement():

    while True:
        laundry = input('Do you want to do laundry? \n1 yes, \n2 no \n> ')
        if laundry == '1':
            quarters = int(input('How many quarters do you have? '))
            if quarters < 8:
                print('You need more money.')
            elif quarters >= 8:
                print('washing')
                sleep(5)
                print('drying')
                sleep(10)
                print('done')
                livingRoom()
        else:
            livingRoom()


def livingRoom():

    while True:
        roomSelect = ('1 Kitchen', '2 Stairs', '3 Porch', '4 Basement',
                      '5 Browse', '6 Rest')
        print(' \n'.join(roomSelect))
        room = input('''\nYou\'re in the living room.
                     \rChoose a room or activity. > ''')
        web = [sys.executable, 'web.py']
        count = [sys.executable, 'countDown.py']
        if room == '1':
            kitchen()
        elif room == '2':
            stairs()
        elif room == '3':
            Porch()
        elif room == '4':
            basement()
        elif room == '5':
            subprocess.call(web)
        elif room == '6':
            subprocess.call(count)
        else:
            print('Invalid Answer.')


if __name__ == "__main__":
    Porch()
