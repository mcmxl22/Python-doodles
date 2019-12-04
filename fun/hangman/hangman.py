#!/usr/bin/env python3
"""
Hangman version 3.2
Python 3.8
Requires a .txt file with a list of words.
Written for Windows
I used:
https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
"""


import random
import winsound


def get_word():
    """Get a random word."""
    with open("words_alpha.txt", "r") as file:
        lines = file.readlines()
        word_select = random.choice(lines)
    word = word_select.rstrip()  # Removes \n character.
    return word


def main():
    """Hangman game"""
    print("""
            This is a hangman game. It tells you how many letters are in the word.
            You have 2 guesses for each letter in the word. It will fill in the blanks
            when you guess a correct letter. It keeps track of wrong guesses and warns
            you of duplicate guesses. 
          """)

    word_item = get_word()
    letter_list = list(word_item)
    guesses = ((list_len := len(letter_list)) * 2)
    attempts = 0
    incorrect_letters = []
    spaces = ["-" for letter in word_item]
    print(f"The word has {list_len} letters.")

    while attempts < guesses:
        guess_letter = input("Guess a letter. ")
        attempts += 1
        remaining = f"Guesses remaining: {guesses - attempts}"

        if guess_letter in letter_list:
            win = winsound.Beep(1000, 400)
            start = 0
            for letter in range(letter_list.count(guess_letter)):
                locate = letter_list.index(guess_letter, start)
                spaces[locate] = guess_letter
                start = locate + 1
            print(remaining)
            print("".join(spaces))

            while attempts >= guesses / 2:
                guess_word = input("Guess the word, y/n? ")
                if guess_word in "y":
                    guess = input("What is the word? ")
                    if guess == word_item:
                        win
                        print("Correct! You win!")
                        raise SystemExit
                    else:
                        winsound.Beep(400, 400)
                        print("Wrong!")
                        break
                else:
                    break
        
        elif guess_letter in ["exit", "quit"]:
            raise SystemExit 

        else:
            winsound.Beep(400, 400)
            if guess_letter not in incorrect_letters:
                incorrect_letters.append(guess_letter)
            else:
                print(f"You already guessed {guess_letter}!")

            print(f"There is no {guess_letter}.\n{remaining}!")

    else:
        winsound.Beep(400, 400)
        print(f"You're hung! The word was {word_item}.")
        raise SystemExit


if __name__ == "__main__":
    main()
