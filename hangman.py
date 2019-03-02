#!/usr/bin/env python
"""Hangman version 1
   Python 3.7.1"""


import random


def hang_man():
    """Hangman game"""
    word_list = ['it']
    word = random.choice(word_list)
    letter_list = list(word)
    count = 0
    for count in range(len(letter_list * 2)):
        guess_letter = input('Guess a letter. ')
        if guess_letter in letter_list:
            print(f'There is a {guess_letter}.')
            count += 1
            while count >= 2:
                guess_word = input('Guess the word, y/n? ')
                if guess_word == 'y':
                    guess = input('What is the word? ')
                    if guess in word:
                        print('You avoided death!')
                        raise SystemExit
                    else:
                        print('Wrong!')
                        break
                else:
                    break
        else:
            print(f'There is no {guess_letter}.')
    else:
        print('You\'re hung!')


if __name__ == "__main__":
    hang_man()
