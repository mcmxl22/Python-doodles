#!/usr/bin/env python3
"""
Hangman version 3.5
Python 3.8
Requires a .txt file with a list of words.
Written for Windows
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""


from os import system
from random import choice
from sys import exit
from winsound import Beep


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
            you of duplicate guesses. 
          """
    )

    word_item = get_word()
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    letter_list = list(word_item)
    guesses = (list_length := len(letter_list)) * 2
    attempts = 0
    incorrect_letters = []
    spaces = ["-" for letter in word_item]  # Replaces letters with a dash.
    print(f"The word has {list_length} letters.")

    while attempts < guesses:
        try:
            guess_letter = input("Guess a letter. ")

        except KeyboardInterrupt:
            exit(0)

        if len(guess_letter) > 1:
            print("You can only guess a single letter!")

        elif guess_letter in number_list:
            print("You must guess a letter!")

        else:
            pass

        attempts += 1
        remaining_guesses = f"Guesses remaining: {guesses - attempts}"

        if guess_letter in letter_list:
            start = 0
            for letter in range(letter_list.count(guess_letter)):
                locate_letter = letter_list.index(guess_letter, start)
                spaces[locate_letter] = guess_letter
                start = locate_letter + 1
            format_word = "".join(spaces)

            if format_word in word_item:
                print(f"{format_word}\nYou win!")
                Beep(1000, 400)
                exit(0)

            else:
                print(f"{remaining_guesses}\n{format_word}")

            while attempts >= guesses / 2:
                guess_word = input("Guess the word, y/n? ")

                if guess_word in "y":
                    guess = input("What is the word? ")

                    if guess == word_item:
                        Beep(1000, 400)
                        print("Correct! You win!")
                        exit(0)

                    else:
                        Beep(400, 400)
                        print("Wrong!")
                        break
                else:
                    break

        elif guess_letter in ["exit", "quit"]:
            exit(0)

        else:
            Beep(400, 400)
            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)

            else:
                print(f"You already guessed {guess_letter}!")

            print(f"There is no {guess_letter}.\n{remaining_guesses}!")

    else:
        Beep(400, 400)
        print(f"You're hung! The word was {word_item}.")
        exit(0)


if __name__ == "__main__":
    main()
