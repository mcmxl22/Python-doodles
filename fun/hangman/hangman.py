"""
Author: M. McConnaughey
Hangman version 5.7
Date: 07/17/2024
Python 3.8+
"""

from sys import platform, version_info
import os
import random


def check_version() -> bool:
    """Checks version of Python."""
    if not (version_info[0] == 3 and version_info[1] >= 8):
        print("This script requires Python 3.8+.")
        return False
    return True


class Screen:
    """Screen class."""

    def clear_and_print(self, text: str) -> None:
        """Clear screen and print something."""
        if platform in "win32":
            os.system("cls")
        else:
            os.system("clear")
        print(text)

    def clear_and_exit(self) -> None:
        """Clear the screen and exit."""
        if platform in "win32":
            os.system("cls")
        else:
            os.system("clear")
        exit()


class Word:
    """Word class."""

    def get_path(self) -> str:
        """Returns path to word list."""
        file_path = os.path.abspath("words_alpha.txt")
        return file_path

    def get_word(self, file_path: str) -> str:
        """Get a random word from file."""
        with open(file_path) as f:
            words = f.read().splitlines()
        return random.choice(words)

    def guess_word(self) -> None:
        """Guess the word."""
        attempts = 0
        incorrect_letters = []
        word = word_setup()
        dashes = ["-" for _ in word]
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
                screen.clear_and_print(f"There is a: {guess_letter}.")
                for i in range(len(word)):
                    if word[i] == guess_letter:
                        dashes[i] = guess_letter

                if (format_word := "".join(dashes)) in word:
                    exit(screen.clear_and_print(f"{format_word}\nYou win!"))
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
            screen.clear_and_print(f"You're hung! The word was {word}.")
            exit()


def word_setup() -> str:
    """Setup for hangman game."""
    word = Word()
    path = word.get_path()
    word = word.get_word(path)
    return word


def dashes() -> str:
    """Dashes for word."""
    dashes = ["-" for _ in word_setup()]
    return "".join(dashes)


def main() -> None:
    """Hangman game."""
    screen = Screen()
    word = word_setup()
    screen.clear_and_print(
        f"""Welcome to Hangman! You have 2 guesses for each letter. 
The word has {len(word)} letters.\n"""
    )

    print(dashes())
    play_game = Word.guess_word
    play_game("")


if __name__ == "__main__":
    check_version()
    main()
