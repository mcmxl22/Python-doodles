#! /usr/bin/env python
# By Micah M. 2018
# House version 1.01.01
# Python 3.6.4


import subprocess
import sys
from time import sleep


def frontPorch():

    print('\nChoose a door.\n')
    portal = ('front', 'exit')
    for i in portal:
        print('%s' % i)

    choice = input('\n> ')
    if choice == portal[0]:
        livingRoom()

    elif choice == portal[1]:
        quit()

    else:
        print('That is not a valid answer.')
        frontPorch()


def stairs():

    print('\nYou\'re in the upstairs hall. There are 6 doors. Choose one.')
    for i in range(1, 7):
        print('%s' % i)

    choice = input('\n> ')
    if choice in {'1', '2', '3', '5'}:
        print('This door is locked.')
        stairs()

    elif choice in {'4', '6'}:
        print('This room is empty.')
        stairs()

    else:
        livingRoom()


def kitchen():

    print('The kitchen is being remodeled. Come back later.')
    livingRoom()


def basement():

    print('Do you want to do laundry?')
    answer = ('yes', 'no')
    for i in answer:
        print('%s' % i)

    choice = input('\n> ')
    if choice == answer[0]:
        quarters = int(input('How many quarters do you have? '))
        if quarters < 8:
            print('You need more money.')
            basement()

        elif quarters >= 8:
            print('washing')
            sleep(5)
            print('drying')
            sleep(10)
            print('done')
            livingRoom()

        else:
            basement()

    else:
        livingRoom()


def livingRoom():
    while True:
        print('\nYou\'re in the livingroom. Choose a room or activity.\n')
        web, count = [sys.executable, 'web.py'], [sys.executable, 'countDown.py']
        room = ('kitchen', 'stairs', 'porch', 'basement', 'browse', 'rest')

        for i in room:
            print('%s' % i)

        choice = input('\n> ')
        if choice == room[1]:
            stairs()

        elif choice == room[2]:
            frontPorch()

        elif choice == room[0]:
            kitchen()

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
