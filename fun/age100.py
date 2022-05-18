#!/usr/bin/env python3
"""
age100 version 1.4
Python 3.10.X
"""

import datetime

class User:
    def __init__(self):
        self.name = input('Enter name. ')
        self.age = int(input('Enter age. '))

    def show_name(self):
        return self.name
    
    def show_age(self):
        return self.age


def calculate():
    user = User()
    user.show_name()
    user.show_age()
    current_year = datetime.datetime.now()
    age_100 = (int(current_year.year) - user.age) + 100
    return f'{user.name} will be 100 in {age_100}!'
    

if __name__ == '__main__':
    print(calculate())
