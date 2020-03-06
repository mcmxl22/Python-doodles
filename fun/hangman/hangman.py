#!/usr/bin/env python3
"""
Hangman version 4.1
Python 3.8
Requires: get_word.py, clear_screen.py
"""

from clear_screen import clear_screen
from get_word import get_word


def main():
    """Hangman game"""
    clear_screen()
    print(
        """
        This is a hangman game. It tells you how many letters are in the word.
        You have 2 guesses for each letter. It will fill in the blanks when
        you guess a correct letter. It keeps track of wrong guesses and warns
        you of duplicate guesses. You can type exit or quit to end the game at any time.
        """
    )
    
    word_item = get_word()
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    letter_list = list(word_item)
    guesses = (list_length := len(letter_list)) * 2
    attempts = 0
    dashes = ["-" for letter in word_item]  # Replaces letters with dashes.
    incorrect_letters = []
    print(f"The word has {list_length} letters.")

    while attempts < guesses:
        try:
            guess_letter = input("Guess a letter. ")

        except KeyboardInterrupt:
            clear_screen()
            exit(0)

        if guess_letter in ["exit", "quit"]:
            clear_screen()
            exit(0)

        elif len(guess_letter) > 1:
            clear_screen
            print("You must guess a single letter!")

        elif guess_letter in number_list:
            clear_screen()
            print("You must guess a letter!")

        else:
            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)

            else:
                clear_screen()
                print(f"You already guessed {guess_letter}!")
            
            print(f"There is no {guess_letter}!")


        attempts += 1

        if guess_letter in letter_list:
            start = 0
            remaining_guesses = f"Guesses remaining: {guesses - attempts}"

            # Puts guessed letters back in the word.
            for letter in range(letter_list.count(guess_letter)):
                locate_letter = letter_list.index(guess_letter, start)
                dashes[locate_letter] = guess_letter
                start = locate_letter + 1
            win = f"You won in {attempts} guesses!"
            format_word = "".join(dashes)

            if format_word in word_item:
                clear_screen()
                print(win)
                exit(0)

            else:
                clear_screen()
                print(f"{remaining_guesses}\n{format_word}")

            while attempts >= guesses / 2:
                guess_word = input("Guess the word, y/n? ")

                if guess_word in "y":
                    clear_screen()
                    print(format_word)
                    guess = input("What is the word? ")

                    if guess in word_item:
                        clear_screen()
                        print(f"{guess}\n{win}")
                        exit(0)

                    else:
                        clear_screen()
                        print(f"{guess} is incorrect!")
                        print(format_word)
                        break
                else:
                    clear_screen()
                    print(format_word)
                    break

    else:
        print(f"You're hung! The word was {word_item}.")
        exit(0)


if __name__ == "__main__":
    exit(main())
