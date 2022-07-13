#!/usr/bin/env python3

"""
Author: M. McConnaughey
Hangman version 5.5
Requires: get_word.py, clear_and_exit.py
Date: 07/13/2022
Python 3.8+
"""

from sys import platform, version_info
from os import system
from get_word import get_word
from clear_and_exit import clear_and_exit


def check_version() -> bool:
    """Checks version of Python."""
    if version_info[0] != 3 or version_info[1] < 8:
        print("This script requires Python 3.8+.")
    else:
        pass


def clear_and_print(text) -> str:
    """Clears screen and prints something."""
    if platform in "win32":
        system("cls")
    else:
        system("clear")
    return print(text)


def main():
    """Hangman game"""
    word_item = get_word()
    clear_screen = clear_and_print
    available_guesses = (list_length := len(word_item)) * 2
    attempts = 0
    dashes = ["-" for letter in word_item]  # Replaces letters with dashes.
    incorrect_letters = []

    clear_screen(
        f"""
This is a hangman game. It tells you how many letters are in the word.
You have 2 guesses for each letter. It fills in the blanks when
you guess a correct letter. It keeps track of guesses and warns
you of duplicate guesses. Type exit or quit to end the game at any time.
The word has {list_length} letters.\n"""
    )

    while attempts < available_guesses:
        try:
            guess_letter = input("Guess a letter: ")
            assert guess_letter.isalpha(), "Please enter a letter!"
            assert len(guess_letter) == 1, "Please enter a single letter!"
        except KeyboardInterrupt:
            clear_and_exit()
        except AssertionError as error:
            print(error)
            continue

        if guess_letter not in incorrect_letters:
            incorrect_letters.append(guess_letter)
            clear_screen(f"There is no: {guess_letter}!")
        else:
            clear_screen(f"You already guessed: {guess_letter}!")

        attempts += 1

        if guess_letter in word_item:
            clear_screen(f"There is a(n): {guess_letter}!")

            # Puts guessed letters back in the word.
            # pylint: disable=unused-variable
            start = 0
            for letter in range(list(word_item).count(guess_letter)):
                locate_letter = list(word_item).index(guess_letter, start)
                dashes[locate_letter] = guess_letter
                start = locate_letter + 1
            # pylint: enable=unused-variable

            if (format_word := "".join(dashes)) in word_item:
                exit(clear_screen(f"{format_word}\nYou win!"))

            else:
                print(
                    (
                        f"""Guesses remaining: {available_guesses - attempts}
                            \r{format_word}"""
                    )
                )

        else:
            continue

    else:
        exit(f"You're hung! The word was {word_item}.")


if __name__ == "__main__":
    check_version()
    main()
