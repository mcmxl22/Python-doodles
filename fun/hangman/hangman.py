#!/usr/bin/env python3
"""
Hangman version 5.1
Python 3.8
Requires: get_word.py, clear_screen.py, clear_and_exit.py
"""

import sys


# Check Python version.
if sys.version_info[0] != 3 or sys.version_info[1] < 8:
    print("This script requires Python 3.8")
else:
    pass


from clear_and_exit import clear_and_exit
from clear_screen import clear_screen
from get_word import get_word


def prompt(word):
    """Prompt"""
    enter = input(f"{word} ")
    return enter.lower()


def clear_and_print(text):
    """Clear screen and print something."""
    clear_screen()
    print(text)


def main():
    """Hangman game"""
    word_item = get_word()
    available_guesses = (list_length := len(word_item)) * 2
    attempts = 0
    dashes = ["-" for letter in word_item]  # Replaces letters with dashes.
    incorrect_letters = []

    clear_and_print(
        f"""
This is a hangman game. It tells you how many letters are in the word.
You have 2 guesses for each letter. It fills in the blanks when
you guess a correct letter. It keeps track of guesses and warns
you of duplicate guesses. Type exit or quit to end the game at any time.
The word has {list_length} letters.
"""
    )

    while attempts < available_guesses:
        try:
            guess_letter = prompt("Guess a letter.")
        except KeyboardInterrupt:
            clear_and_exit()

        if guess_letter in ["exit", "quit"]:
            clear_and_exit()
        elif not guess_letter.isalpha() or len(guess_letter) > 1:
            clear_and_print("Please enter a single letter!")
        elif guess_letter not in incorrect_letters:
            incorrect_letters.append(guess_letter)
            clear_and_print(f"There is no {guess_letter}!")
        elif guess_letter in incorrect_letters:
            clear_and_print(f"You already guessed {guess_letter}!")
        else:
            break

        attempts += 1

        if guess_letter in word_item:
            clear_and_print(f"{guess_letter} is in the word!")
            remaining_guesses = f"Guesses remaining: {available_guesses - attempts}"

            # Puts guessed letters back in the word.
            start = 0
            for letter in range(list(word_item).count(guess_letter)):
                locate_letter = list(word_item).index(guess_letter, start)
                dashes[locate_letter] = guess_letter
                start = locate_letter + 1

            format_word = "".join(dashes)
            win = f"You win! Score: {available_guesses - attempts}"

            if format_word in word_item:
                sys.exit(clear_and_print(f"{format_word}\n{win}"))
            else:
                print((remaining := f"{remaining_guesses}\n{format_word}"))

            while attempts >= available_guesses / 2:
                guess_word = prompt("Guess the word? y/n")

                if guess_word in "y":
                    clear_and_print(format_word)
                    guess = prompt("What is the word?")

                    if guess in word_item:
                        sys.exit(clear_and_print(f"{guess}\n{win}"))
                    else:
                        clear_and_print(f"{guess} is incorrect!")
                        print(format_word)
                        break

                else:
                    clear_and_print(remaining)
                    break

    else:
        sys.exit(f"You're hung! The word was {word_item}.")


if __name__ == "__main__":
    sys.exit(main())
