import unittest
import mastermind


class TestMastermind(unittest.TestCase):

    def test_prepare_word_positive(self):
        game = mastermind.Mastermind(10, ['a', 'b', 'c'], 10)
        game.prepare_word()
        self.assertEqual(len(game.word), 10)

