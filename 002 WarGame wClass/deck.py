from random import shuffle

suits = ["spades", "hearts", "diamonds", "clubs"]
figures = {"9": 0, "10": 1, "jack": 2, "queen": 3, "king": 4, "ace": 5}


def prepare_deck():
    # type: () -> list
    """This function prepare deck of cards for WarGame"""
    return [fig + " of " + su for fig in figures.keys() for su in suits]


def prepare_player_decks(deck):
    """This function prepare decks for two players"""
    return deck[:len(deck) // 2], deck[len(deck) // 2:]


def shuffle_deck(deck):
    """This function shuffle deck of cards"""
    shuffle(deck)
