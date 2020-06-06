import unittest
from get_word import get_word


class Test_Get_Word(unittest.TestCase):

    def test_word(self):
        self.assertTrue(get_word)

    def test_type(self):
        self.assertTrue(str(get_word))
