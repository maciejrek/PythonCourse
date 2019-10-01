import unittest
import wargame


class TestWarGame(unittest.TestCase):

    def test_draw_card(self):
        game = wargame.WarGame()
        self.assertEqual(len(game.p1), 12)
        self.assertEqual(len(game.p2), 12)
        p1_card, p2_card = game.draw_card()
        self.assertEqual(len(game.p1), 11)
        self.assertEqual(len(game.p2), 11)
        self.assertNotIn(p1_card, game.p1)
        self.assertNotIn(p2_card, game.p2)
        for i in range(3):
            p1_card, p2_card = game.draw_card()
            self.assertNotIn(p1_card, game.p1)
            self.assertNotIn(p2_card, game.p2)
        self.assertEqual(len(game.p1), 8)
        self.assertEqual(len(game.p2), 8)
        del game

    def test_check_decks_method(self):
        print("Case 1: Both players should have 12 cards")
        game = wargame.WarGame()
        self.assertEqual(len(game.p1), 12)
        self.assertEqual(len(game.p2), 12)
        self.assertFalse(game.check_decks())
        del game

        print("Case 2: Player one wins")
        game = wargame.WarGame()
        game.p1 = []
        self.assertTrue(game.check_decks())
        self.assertEqual(game.winner, 2)
        del game

        print("Case 3: Player two wins")
        game = wargame.WarGame()
        game.p2 = []
        self.assertTrue(game.check_decks())
        self.assertEqual(game.winner, 1)
        del game

    def test_put_cards(self):
        game = wargame.WarGame()
        self.assertEqual(len(game.p1), 12)
        self.assertEqual(len(game.p2), 12)
        p1, p2 = game.draw_card()
        p1_help = []
        p2_help = []
        p1_help.append(p1)
        p2_help.append(p2)
        self.assertEqual(len(game.p1), 11)
        self.assertEqual(len(game.p2), 11)
        game.put_cards(p1_cards=p1_help)
        self.assertEqual(len(game.p1), 12)
        self.assertEqual(len(game.p2), 11)
        game.put_cards(p2_cards=p2_help)
        self.assertEqual(len(game.p1), 12)
        self.assertEqual(len(game.p2), 12)
        del game

    def test_clear_help_decks(self):
        game = wargame.WarGame()
        p1_card, p2_card = game.draw_card()
        game.p1_help_deck.append(p1_card)
        game.p2_help_deck.append(p2_card)
        self.assertEqual(len(game.p1_help_deck), 1)
        self.assertEqual(len(game.p2_help_deck), 1)
        game.clear_help_decks()
        self.assertEqual(len(game.p1_help_deck), 0)
        self.assertEqual(len(game.p2_help_deck), 0)
