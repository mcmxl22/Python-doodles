#!/usr/bin/env python3
"""
Palindrome checker
Python 3.7
"""

def get_word():
    word = input("Enter a word: ")
    return word

def is_palindrome():
    word = get_word()
    return f'Palindrome: {word == word[::-1]}'

if __name__ == "__main__":
    while True:
        print(is_palindrome())
