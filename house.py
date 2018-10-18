#!/usr/bin/env python
'''By Micah M. 2018
   House version 1.2
   Python 3.7
   Requires web.py and count_down.py'''


import subprocess
import sys
from time import sleep


def porch():
    '''porch'''
    while True:
        choice = input('\nChoose a door. \n1 front \n2 exit \n>')
        if choice == '1':
            living_room()
        elif choice == '2':
            raise SystemExit
        else:
            print('Invalid answer.')


def stairs():
    '''stairs'''
    while True:
        for i in range(1, 7):
            print(i)
        choice = input('''\nYou\'re in the upstairs hall.
                       \rChoose a door. > ''')
        if choice in {'1', '2', '3', '5'}:
            print('This door is locked.')
        elif choice in {'4', '6'}:
            print('This room is empty.')
        else:
            living_room()


def kitchen():
    '''kitchen'''
    print('The kitchen is being remodeled. Come back later.')
    living_room()


def basement():
    '''basement'''
    while True:
        laundry = input('Do you want to do laundry? \n1 yes, \n2 no \n> ')
        if laundry == '1':
            quarters = int(input('How many quarters do you have? '))
            if quarters < 8:
                print(f'{quarters} is not enough money.')
            elif quarters >= 8:
                print('Washing!')
                sleep(5)
                print('Drying!')
                sleep(10)
                print('Done!')
        else:
            living_room()


def living_room():
    '''living_room'''
    while True:
        room_select = ('1 Kitchen', '2 Stairs', '3 Porch', '4 Basement',
                       '5 Browse', '6 Rest')
        print(' \n'.join(room_select))
        room = input('''\nYou\'re in the living room.
                     \rChoose a room or activity. > ''')
        web = [sys.executable, 'web.py']
        count = [sys.executable, 'countDown.py']
        if room == '1':
            kitchen()
        elif room == '2':
            stairs()
        elif room == '3':
            porch()
        elif room == '4':
            basement()
        elif room == '5':
            subprocess.run(web)
        elif room == '6':
            subprocess.run(count)
        else:
            print('Invalid Answer.')


if __name__ == "__main__":
    porch()
