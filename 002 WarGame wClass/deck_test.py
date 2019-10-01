import unittest
import deck


class TestDeck(unittest.TestCase):

    def test_prepare_deck_positive(self):
        self.deck = deck.prepare_deck()
        self.assertEqual(len(self.deck), 24)
        self.assertEqual(sorted(self.deck), sorted(set(self.deck)))

    def test_prepare_player_decks_positive(self):
        self.deck = deck.prepare_deck()
        self.p1, self.p2 = deck.prepare_player_decks(self.deck)
        self.assertEqual(len(self.p1), 12)
        self.assertEqual(len(self.p2), 12)
        self.assertNotIn(self.p1, self.p2)
        self.assertNotIn(self.p2, self.p1)

    def test_prepare_player_decks_negative(self):
        self.deck = []
        self.p1, self.p2 = deck.prepare_player_decks(self.deck)
        self.assertEqual(self.p1, [])
        self.assertEqual(self.p2, [])

    def test_shuffle_deck(self):
        self.deck = deck.prepare_deck()
        self.deck2 = deck.prepare_deck()
        self.assertEqual(self.deck, self.deck2)
        deck.shuffle_deck(self.deck2)
        self.assertNotEqual(self.deck, self.deck2)
        for i in self.deck:
            self.assertIn(i,self.deck2)
