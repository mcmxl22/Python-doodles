#!/usr/bin/env python3
"""
Hangman version 2.1
Python 3.7
requires a txt file with a list of word.
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""


import random


def hang_man():
    """Hangman game"""

    with open("words_alpha.txt", "r") as f:
        lines = f.readlines()
        raw_word = random.choice(lines)

    letter_list = list(raw_word)
    del letter_list[-1] # Deletes \n charater.
    final_word = "".join(letter_list)

    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    incorrect_letters = []
    spaces = ["-" for letter in final_word]

    for count in range(len(letter_list * 2)):
        print(f"There are {len(letter_list)} letters in the word.")
        guess_letter = input("Guess a letter. ")

        if guess_letter in letter_list:
            locate = letter_list.index(guess_letter)
            spaces[locate] = guess_letter
            
            if guess_letter in vowels:
                print(f"There is an {guess_letter} at {locate}.")
            else:
                print(f"There is a {guess_letter} at {locate}.")

            print("".join(spaces))

            count += 1
            while count >= 2:
                guess_word = input("Guess the word, y/n? ")
                if guess_word == "y":
                    guess = input("What is the word? ")
                    if guess in final_word:
                        print("You avoided death!")
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

            print(f"There is no {guess_letter}.")

    else:
        print(f"You're hung! The word was {final_word}.")


if __name__ == "__main__":
    hang_man()
