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
    assert(len(hangman.dashes()) == len(hangman.word_setup()))

def test_get_path():
    assert(hangman.get_path())
    assert(type(hangman.get_path()) == str)

def test_get_word():
    assert(hangman.get_word(hangman.get_path()))
    assert(type(hangman.get_word(hangman.get_path())) == str)

def test_clear_and_print():
    assert(hangman.clear_and_print("test")) is None
