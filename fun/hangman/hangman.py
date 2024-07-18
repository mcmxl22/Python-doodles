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
    if not (version_info[0] == 3 and version_info[1] >= 8):"""
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


def clear_and_print(text: str) -> None:
    """Clear screen and print something."""
    if platform in "win32":
        os.system("cls")
    else:
        os.system("clear")
    print(text)


def clear_and_exit() -> None:
    """Clear the screen and exit."""
    if platform in "win32":
        os.system("cls")
    else:
        os.system("clear")
    exit()


def get_path() -> str:
    """Returns path to word list."""
    file_path = os.path.abspath("words_alpha.txt")
    return file_path


def get_word(file_path: str) -> str:
    """Get a random word from file."""
    with open(file_path) as f:
        words = f.read().splitlines()
    return random.choice(words)


def word_setup() -> str:
    """Setup for hangman game."""
    path = get_path()
    word = get_word(path)
    return word


def dashes() -> str:
    """Dashes for word."""
    word = word_setup()
    dashes = ["-" for _ in word]
    return "".join(dashes)


def letter_input() -> str:
    """Get letter input."""
    try:
        letter = input("Guess a letter: ")
        assert letter.isalpha(), "Please enter a letter."
        assert len(letter) == 1, "Please enter a single letter."
    except KeyboardInterrupt:
        clear_and_exit()
    except AssertionError as error:
        print(error)
        return letter_input()
    return letter


def guess_word() -> None:
    """Guess the word."""
    attempts = 0
    incorrect_letters = []
    word = word_setup()
    dashes = ["-" for _ in word]
    available_guesses = len(word) * 2
    remaining_guesses = available_guesses - attempts
    while attempts < available_guesses:
        try:
            guess_letter = input("Guess a letter: ")
            assert guess_letter.isalpha(), "Please enter a letter."
            assert len(guess_letter) == 1, "Please enter a single letter."
        except KeyboardInterrupt:
            clear_and_exit()
        except AssertionError as error:
            print(error)
            continue

        if guess_letter not in incorrect_letters:
            incorrect_letters.append(guess_letter)
            clear_and_print(
                f"""There is no: {guess_letter}.
                            \rGuesses remaining: {available_guesses - attempts}"""
            )
        else:
            clear_and_print(
                f"""You already guessed: {guess_letter}.
                            \rGuesses remaining: {available_guesses - attempts}"""
            )

        attempts += 1

        if guess_letter in word:
            clear_and_print(f"There is a(n): {guess_letter}.")
            for i in range(len(word)):
                if word[i] == guess_letter:
                    dashes[i] = guess_letter

            if (format_word := "".join(dashes)) in word:
                exit(clear_and_print(f"{format_word}\nYou win!"))
            else:
                print(
                    f"Guesses remaining: {available_guesses - attempts}\n{format_word}"
                )
        else:
            continue

    else:
        clear_and_print(f"You're hung! The word was {word}.")
        exit()


def main() -> None:
    """Hangman game."""
    word = word_setup()
    clear_and_print(f"""Welcome to Hangman! You have {len(word) * 2} guesses.""")
    print(dashes())
    guess_word()


if __name__ == "__main__":
    check_version()
    main()

        print("This script requires Python 3.8+.")
        return False
    return True


def clear_and_print(text: str) -> None:
    """Clear screen and print something."""
    if platform in "win32":
        os.system("cls")
    else:
        os.system("clear")
    print(text)


def clear_and_exit() -> None:
    """Clear the screen and exit."""
    if platform in "win32":
        os.system("cls")
    else:
        os.system("clear")
    exit()


def get_path() -> str:
    """Returns path to word list."""
    file_path = os.path.abspath("words_alpha.txt")
    return file_path


def get_word(file_path: str) -> str:
    """Get a random word from file."""
    with open(file_path) as f:
        words = f.read().splitlines()
    return random.choice(words)

def word_setup() -> str:
    """Setup for hangman game."""
    path = get_path()
    word = get_word(path)
    return word

def dashes() -> str:
    """Dashes for word."""
    word = word_setup()
    dashes = ["-" for _ in word]
    return "".join(dashes)

def letter_input() -> str:
    """Get letter input."""
    try:
        letter = input("Guess a letter: ")
        assert letter.isalpha(), "Please enter a letter."
        assert len(letter) == 1, "Please enter a single letter."
    except KeyboardInterrupt:
        clear_and_exit()
    except AssertionError as error:
        print(error)
        return letter_input()
    return letter

def guess_word() -> None:
    """Guess the word."""
    attempts = 0
    incorrect_letters = []
    word = word_setup()
    dashes = ["-" for _ in word]
    available_guesses = len(word) * 2
    while attempts < available_guesses:
        try:
            guess_letter = input("Guess a letter: ")
            assert guess_letter.isalpha(), "Please enter a letter."
            assert len(guess_letter) == 1, "Please enter a single letter."
        except KeyboardInterrupt:
            clear_and_exit()
        except AssertionError as error:
            print(error)
            continue

        if guess_letter not in incorrect_letters:
            incorrect_letters.append(guess_letter)
            clear_and_print(f"There is no: {guess_letter}.")
        else:
            clear_and_print(f"You already guessed: {guess_letter}.")

        attempts += 1

        if guess_letter in word:
            clear_and_print(f"There is a(n): {guess_letter}.")
            for i in range(len(word)):
                if word[i] == guess_letter:
                    dashes[i] = guess_letter

            if (format_word := "".join(dashes)) in word:
                exit(clear_and_print(f"{format_word}\nYou win!"))
            else:
                print(f"Guesses remaining: {available_guesses - attempts}\n{format_word}")
        else:
            continue

    else:
        clear_and_print(f"You're hung! The word was {word}.")
        exit()

def main() -> None:
    """Hangman game."""
    word = word_setup()
    clear_and_print(f"""Welcome to Hangman! You have {len(word) * 2} guesses.""")
    print(dashes())
    guess_word()

if __name__ == "__main__":
    check_version()
    main()
