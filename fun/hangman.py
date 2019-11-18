#!/usr/bin/env python3
"""
Hangman version 2.4
Python 3.8
Requires a .txt file with a list of words.
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""


import random


def hang_man():
    """Hangman game"""
    print("""
            This is a hangman game. It tells you how many letters are in the word.
            You have 2 guesses for each letter in the word. It will fill in the blanks
            when you guess a correct letter. It keeps track of wrong guesses and warns
            you of duplicates.
          """)

    with open("words_alpha.txt", "r") as f:
        lines = f.readlines()
        word = random.choice(lines)

    word.rstrip()

    letter_list = list(word)
    guesses = ((l := len(letter_list)) * 2)

    attempts = 0
    incorrect_letters = []
    spaces = ["-" for letter in word]
    print(f"There are {l} letters in the word.")

    while attempts < guesses:
        guess_letter = input("Guess a letter. ")
        attempts += 1
        remaining = f"You have {guesses - attempts} guesses left."

        if guess_letter in letter_list:
            start = 0
            while True:
                try:
                    locate = letter_list.index(guess_letter, start)
                    spaces[locate] = guess_letter
                    start = locate + 1
                    print(f"Letter {locate + 1} is: {guess_letter}")
                    print(remaining)
                    print("".join(spaces))
                except:
                    break

            while attempts >= guesses / 2:
                guess_word = input("Guess the word, y/n? ")
                if guess_word in "y":
                    guess = input("What is the word? ")
                    if guess == word:
                        print("Correct! You avoided death!")
                        raise SystemExit
                    else:
                        print("Wrong!")
                        break
                else:
                    break
        else:
            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)
            else:
                print("You already guessed that letter!")

            print(f"There is no {guess_letter}.\n{remaining}")

    else:
        print(f"You're hung! The word was {word}.")


if __name__ == "__main__":
    hang_man()
