import unittest
import hangman


class Test_Hangman(unittest.TestCase):

    def test_hangman(self):
        self.assertTrue(hangman)

    def test_clr_exit(self):
        self.assertTrue(hangman.clear_and_exit)

    def test_clr_print(self):
        self.assertTrue(hangman.clear_and_print)

    def test_main(self):
        self.assertTrue(hangman.main)
