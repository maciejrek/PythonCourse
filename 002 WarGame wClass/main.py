import wargame
import os

"""
TODO:
    - Fix infinite loop in case of specific shuffle
"""
game = wargame.WarGame()

while not game.check_decks():
    game.single_round()
