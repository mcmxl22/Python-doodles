#!/use/bin/env python3
"""
Hangman version 1.1
Python 3.7
"""

import random


def hang_man():
    """Hangman game"""
    word_list = [
        "it",
        "crime",
        "stone",
        "member",
        "reports",
        "cry",
        "badge",
        "dude",
        "hang",
        "man",
    ]
    word = random.choice(word_list)
    letter_list = list(word)
    count = 0
    guesses = []
    incorrect_letters = []

    for count in range(len(letter_list * 3)):
        guess_letter = input("Guess a letter. ")

        if guess_letter in letter_list:
            guesses.append(guess_letter)
            locate = letter_list.index(guess_letter)
            print(f"There is a {guess_letter} at {locate}.")
            print(guesses)

            count += 1
            while count >= 1:
                guess_word = input("Guess the word, y/n? ")

                if guess_word is "y":
                    guess = input("What is the word? ")
                elif guess_word is "n":
                    break
                elif guess in word:
                    print("You avoided death!")
                    raise SystemExit
                else:
                    print("Wrong!")
                    break

        else:
            incorrect_letters.append(guess_letter)
            if guess_letter in incorrect_letters:

                if len(incorrect_letters) > 1:
                    print("You already guessed that letter!")
            print(f"There is no {guess_letter}.")

    else:
        print(f"You're hung! The word was {word}.")


if __name__ == "__main__":
    hang_man()
