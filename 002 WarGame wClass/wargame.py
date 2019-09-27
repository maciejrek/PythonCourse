import deck


class WarGame:
    # init
    def __init__(self):
        """ WarGame class init method """
        self.deck = deck.prepare_deck()
        deck.shuffle_deck(self.deck)
        self.p1, self.p2 = deck.prepare_player_decks(self.deck)
        self.p1_help_deck = []
        self.p2_help_deck = []
        self.winner = 0

    # Check decks method
    def check_decks(self):
        """This method check status of player's deck"""
        if 0 == len(self.p1):
            print("Game Over! Player One wins!")
            self.winner = 1
            return True
        elif 0 == len(self.p2):
            print("Game Over! Player Two wins!")
            self.winner = 2
            return True
        print(f'P1 has {len(self.p1)} cards, P2 has {len(self.p2)} cards')
        return False

    # Draw card method
    def draw_card(self):
        """This method performs draw operation"""
        return self.p1.pop(0), self.p2.pop(0)

    # Put cards method
    def put_cards(self, p1_cards: list = None, p2_cards: list = None):
        """ This method put card back to the deck """
        if p1_cards is None:
            self.p2.extend(p2_cards)
        elif p2_cards is None:
            self.p1.extend(p1_cards)
        else:
            self.p1.extend(p1_cards)
            self.p2.extend(p2_cards)

    def clear_help_decks(self):
        """ This method clear help decks """
        self.p1_help_deck = []
        self.p2_help_deck = []

    # Single round method
    def single_round(self):
        """This method performs one round"""
        p1_card, p2_card = self.draw_card()
        self.p1_help_deck.append(p1_card)
        self.p2_help_deck.append(p2_card)
        if deck.figures.get(str(p1_card.split(" ", 1)[0])) > deck.figures.get(str(p2_card.split(" ", 1)[0])):
            print(f"P1 won with {p1_card} over {p2_card}")
            self.put_cards(p1_cards=self.p1_help_deck + self.p2_help_deck)
            self.clear_help_decks()
        elif deck.figures.get(str(p1_card.split(" ", 1)[0])) < deck.figures.get(str(p2_card.split(" ", 1)[0])):
            print(f"P2 won with {p2_card} over {p1_card}")
            self.put_cards(p2_cards=self.p1_help_deck + self.p2_help_deck)
            self.clear_help_decks()
        else:
            print(f"TIE! P1: {p1_card} P2: {p2_card}")
