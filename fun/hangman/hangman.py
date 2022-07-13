#!/usr/bin/env python3

"""
Author: M. McConnaughey
Hangman version 5.6
Date: 07/13/2022
Python 3.6+
"""

from sys import platform, version_info
from os import system, path
import random


def check_version() -> bool:
    """Checks version of Python."""
    if version_info[0] != 3 or version_info[1] < 6:
        print("This script requires Python 3.6+.")
    else:
        pass


class Screen:
    """Screen class."""
    def clear_and_print(self, text) -> str:
        """Clear screen and print something."""
        if platform in "win32":
            system("cls")
        else:
            system("clear")
        return print(text)

    def clear_and_exit(self) -> None:
        """Clear the screen and exit."""
        if platform in "win32":
            system("cls")
        else:
            system("clear")
        exit()


class Word:
    """Word class."""  
    def get_path(self) -> str:
        """Returns path to word list."""
        file_path = path.abspath('words_alpha.txt')
        return file_path

    def get_word(self, file_path) -> str:
        """Get a random word from file."""
        with open(file_path, 'r') as file:
            lines = file.readlines()
            word_select = random.choice(lines)
        random_word = word_select.rstrip()# Removes \n character.
        return random_word


    def guess_word(self):
        """Guess the word."""
        attempts = 0
        incorrect_letters = []
        word = word_setup()
        dashes = ['-' for letter in word]
        screen = Screen()
        available_guesses = len(word) * 2
        while attempts < available_guesses:
            try:
                guess_letter = input("Guess a letter: ")
                assert guess_letter.isalpha(), "Please enter a letter."
                assert len(guess_letter) == 1, "Please enter a single letter."
            except KeyboardInterrupt:
                screen.clear_and_exit()
            except AssertionError as error:
                print(error)
                continue

            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)
                screen.clear_and_print(f"There is no: {guess_letter}.")
            else:
                screen.clear_and_print(f"You already guessed: {guess_letter}.")

            attempts += 1

            if guess_letter in word:
                screen.clear_and_print(f"There is a(n): {guess_letter}.")

                # Puts guessed letters back in the word.
                # pylint: disable=unused-variable
                start = 0
                for letter in range(list(word).count(guess_letter)):
                    locate_letter = list(word).index(guess_letter, start)
                    dashes[locate_letter] = guess_letter
                    start = locate_letter + 1
                # pylint: enable=unused-variable

                if (format_word := "".join(dashes)) in word:
                    exit(screen.clear_and_print(f"{format_word}\nYou win!"))
                else:
                    print(
                        (f"""Guesses remaining: {available_guesses - attempts}
                            \r{format_word}"""))
            else:
                continue

        else:
            screen.clear_and_print(f"You're hung! The word was {word}.")
            exit()


def word_setup() -> str:
    """Setup for hangman game."""
    word = Word()
    path = word.get_path()
    word = word.get_word(path)
    return word


def dashes():
    """Dashes for word."""
    dashes = ['-' for letter in word_setup()]
    return ''.join(dashes)


def main():
    """Hangman game."""
    screen = Screen()
    word = word_setup()
    screen.clear_and_print(
f"""Welcome to Hangman!
You have 2 guesses for each letter. 
The word has {len(word)} letters.\n""")
    
    print(dashes())
    play_game = Word.guess_word
    play_game('')


if __name__ == "__main__":
    check_version()
    main()
