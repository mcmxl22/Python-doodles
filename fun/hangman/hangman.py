#!/usr/bin/env python3
"""
Hangman version 3.7
Python 3.8
Requires a .txt file with a list of words.
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""

import config
from random import choice
from sys import exit


def get_word():
    """Get a random word."""
    with open("C:/Users/mcmxl/mystuff/hangman/resources/words_alpha.txt", "r") as file:
        lines = file.readlines()
        word_select = choice(lines)
    word = word_select.rstrip()  # Removes \n character.
    return word


def main():
    """Hangman game"""
    print(
        """
            This is a hangman game. It tells you how many letters are in the word.
            You have 2 guesses for each letter in the word. It will fill in the blanks
            when you guess a correct letter. It keeps track of wrong guesses and warns
            you of duplicate guesses. You can type exit or quit to end the game at any time.
          """
    )

    word_item = get_word()
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    letter_list = list(word_item)
    guesses = (list_length := len(letter_list)) * 2
    attempts = 0
    incorrect_letters = []
    spaces = ["-" for letter in word_item]  # Replaces letters with dashes.
    print(f"The word has {list_length} letters.")

    while attempts < guesses:
        try:
            guess_letter = input("Guess a letter. ")

        except KeyboardInterrupt:
            config.clear_screen
            config.quit_game

        if guess_letter in ["exit", "quit"]:
            config.clear_screen
            config.quit_game

        elif len(guess_letter) > 1:
            print("You can only guess a single letter!")

        elif guess_letter in number_list:
            print("You must guess a letter!")

        else:
            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)

            else:
                print(f"You already guessed {guess_letter}!")

            print(f"There is no {guess_letter}!")
        
        attempts += 1

        if guess_letter in letter_list:
            start = 0
            remaining_guesses = f"Guesses remaining: {guesses - attempts}"

            for letter in range(letter_list.count(guess_letter)):
                locate_letter = letter_list.index(guess_letter, start)
                spaces[locate_letter] = guess_letter
                start = locate_letter + 1
            format_word = "".join(spaces)

            if format_word in word_item:
                print(f"{format_word}\nYou win!")
                config.quit_game

            else:
                print(f"{remaining_guesses}\n{format_word}")

            while attempts >= guesses / 2:
                guess_word = input("Guess the word, y/n? ")

                if guess_word in "y":
                    guess = input("What is the word? ")

                    if guess in word_item:
                        print("Correct! You win!")
                        config.quit_game

                    else:
                        print("Wrong!")
                        break
                else:
                    break

    else:
        print(f"You're hung! The word was {word_item}.")
        config.quit_game


if __name__ == "__main__":
    main()
