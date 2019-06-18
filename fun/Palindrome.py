#!/usr/bin/env python3
"""
Palindrome version 1.2
Python 3.7
"""


def palindrome():
    word = input('Enter a word or phrase. ')
    letters = filter(str.strip, list(word))

    test = list(reversed(word))
    letter_test = filter(str.strip, test)

    if list(letter_test) == list(letters):
        print(f'{word} is a palindrome!')

else:
    print(f'{word} is not a palindrome!')

if __name__ == "__main__":
    palindrome()
