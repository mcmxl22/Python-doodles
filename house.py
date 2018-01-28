#! /usr/bin/env python
# By Micah M. 2017
# House version 1.0
# Python 2.7.13


import subprocess
import sys
from time import sleep


def front_porch():

    print ('\nChoose a door.\n')
    portal = ('front', 'exit')
    for i in portal:
        print ('%s' % i)

    choice = raw_input('\n> ')
    if choice == portal[0]:
        living_room()

    else:
        print ('Come back soon!')
        quit()


def stairs():

    print ('\nYou\'re in the upstairs hall. There are 6 doors. Choose one.')
    doors = [range(1, 7)]
    for i in doors:
        print ('\n%s' % i)

    choice = raw_input('\n> ')
    if choice in {'1', '2', '3', '5'}:
        print ('This door is locked.')
        stairs()

    elif choice in {'4', '6'}:
        print ('This room is empty.')
        stairs()

    else:
        living_room()


def kitchen():

    print ('The kitchen is being remodeled. Come back later.')
    living_room()


def basement():

    print ('Do you want to do laundry?')
    answer = ('yes', 'no')
    for i in answer:
        print ('\n%s' % i)

    choice = raw_input('\n> ')
    if choice == answer[0]:
        quarters = raw_input('How many quarters do you have? ')
        if quarters < 8:
            print ('You need more money.')

        elif quarters > 8:
            time = [sys.executable, 'countd.py']
            print ('washing')
            sleep(5)
            print ('drying')
            sleep(10)
            print ('done')
            basement()

        else:   			
            basement()

    else:
        living_room()


def living_room():

    print ('\nYou\'re in the livingroom. Choose a room or activity.\n')
    web, count = [sys.executable, 'web.py'], [sys.executable, 'countd.py']
    room = ('kitchen', 'stairs', 'porch', 'basement', 'browse', 'rest')

    for i in room:
        print ('%s' % i)

    choice = raw_input('\n> ')
    if choice == room[1]:
        stairs()

    elif choice == room[2]:
        front_porch()

    elif choice == room[0]:
        kitchen()

    elif choice == room[3]:
        basement()

    elif choice == room[4]:
        subprocess.call(web)
        living_room()

    else:
        print ('That is not a valid answer.')
        living_room()


if __name__ == "__main__":
    front_porch()
