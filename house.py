#! /usr/bin/env python
# By Micah M. 2018
# House version 1.01.01
# Python 3.6.4


import subprocess
import sys
from time import sleep


def frontPorch():

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
            print('%s' % i)
        choice = input(''''\nYou\'re in the upstairs hall.
There are 6 doors. Choose one. > ''')
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
        choice = input('Do you want to do laundry? y, n > ')
        if choice == 'y':
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
        room = ('kitchen', 'stairs', 'porch', 'basement', 'browse', 'rest')
        for i in room:
            print('%s' % i)
        choice = input('''\nYou\'re in the living room. 
Choose a room or activity. > ''')
        web = [sys.executable, 'web.py']
        count = [sys.executable, 'countDown.py']
        if choice == room[0]:
            kitchen()
        elif choice == room[1]:
            stairs()
        elif choice == room[2]:
            frontPorch()
        elif choice == room[3]:
            basement()
        elif choice == room[4]:
            subprocess.call(web)
        elif choice == room[5]:
            subprocess.call(count)
        else:
            print('That is not a valid answer.')


if __name__ == "__main__":
    frontPorch()
