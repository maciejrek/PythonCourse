from random import shuffle

# Game config
use_limit = True
turn_count = 0
turn_limit = 10000

suits = ["spades", "hearts", "diamonds", "clubs"]
figures = {"9": 0, "10": 1, "jack": 2, "queen": 3, "king": 4, "ace": 5}

# prep deck
deck = [fig + " of " + su for fig in figures.keys() for su in suits]

# shuffle deck
shuffle(deck)

# prepare player decks
p_one_deck = deck[:len(deck) // 2]
p_two_deck = deck[len(deck) // 2:]
p_one_help_deck = []
p_two_help_deck = []

while True:
    if turn_count > turn_limit and use_limit:
        print("Too many turns, game stopped")
        break
    if 0 == len(p_one_deck):
        print("Game Over! Player One wins!")
        break
    elif 0 == len(p_two_deck):
        print("Game Over! Player Two wins!")
        break
    else:
        print("P1 has {} cards, P2 has {} cards".format(len(p_one_deck), len(p_two_deck)))
    turn_count += 1
    print("Drawing a card")
    p_one_card = p_one_deck.pop(0)
    p_two_card = p_two_deck.pop(0)
    p_one_help_deck.append(p_one_card)
    p_two_help_deck.append(p_two_card)
    if figures.get(str(p_one_card.split(" ", 1)[0])) > figures.get(str(p_two_card.split(" ", 1)[0])):
        print("P1 won with {} over {}".format(p_one_card, p_two_card))
        p_one_deck.extend(p_one_help_deck)
        p_one_deck.extend(p_two_help_deck)
        p_one_help_deck = []
        p_two_help_deck = []
    elif figures.get(str(p_one_card.split(" ", 1)[0])) < figures.get(str(p_two_card.split(" ", 1)[0])):
        print("P2 won with {} over {}".format(p_two_card, p_one_card))
        p_two_deck.extend(p_one_help_deck)
        p_two_deck.extend(p_two_help_deck)
        p_one_help_deck = []
        p_two_help_deck = []
    else:
        print("TIE! P1: {} P2: {}".format(p_one_card, p_two_card))
        continue
