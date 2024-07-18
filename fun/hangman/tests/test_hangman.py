# Test using pytest

import hangman

def test_hangman():
    assert(hangman)

def test_word_setup():
    assert(hangman.word_setup())

def test_check_version():
    assert(hangman.check_version())
    assert(hangman.check_version() == True)
    assert(type(hangman.check_version()) == bool)

def test_dashes():
    assert(hangman.dashes())
    assert(type(hangman.dashes()) == str)
