from random import randint as rand
import json


class Mastermind:

    def __init__(self, length: int, symbols: str, round_count: int, mode: bool):
        """
        Mastermind class init method
        :param length: Length of word to guess
        :param symbols: Symbols used to generate word
        :param round_count: Number of rounds
        :param mode: True - additional prints (easy mode)
        """
        self.len = length
        self.sym = sorted(tuple(set(symbols)))
        self.rounds_limit = round_count
        self.round = 0
        self.word = []
        self.players_word = []
        self.wrong_letters = []
        self.symbols = {'correct': 0, 'wrong position': 0, 'wrong': 0}
        self.counted_symbols = {}
        self.game_over = True
        self.mode = mode

        self.traceback = {'word length': self.len, 'symbols': self.sym, 'rounds': self.round, 'player_words': []}

    def prepare_word(self, sym: list, length: int):
        """
        Prepare word for player
        :return: No return statement
        """
        for i in range(0, length):
            self.word.append(self.sym[rand(0, len(sym)) - 1])
        self.game_over = False
        self.traceback['guess_word'] = self.word
        return self.word

    def game_status(self):
        """
        Return game status
        :return: Status of game: False - game is over, True - game is on
        """
        return self.game_over

    """ read one word from keyboard """
    def read_word(self):
        if self.mode:
            print(f"Wrong symbols already used by player {self.wrong_letters}")
        self.players_word = list(input("Enter your guess\n"))
        self.verify_input_len()
        self.traceback['player_words'].append(self.players_word)
        return self.players_word

    def verify_input_len(self):
        """
        Verify length of input
        :return: Raise ValueError in case of mismatch
        """
        if len(self.players_word) != self.len:
            raise ValueError(f"Your word should contain {self.len} characters, entered {len(self.players_word)}")

    def clear_symbols(self):
        """
        This method clear aux dictionary
        :return:
        """
        for i in self.symbols:
            self.symbols[i] = 0

    def count_symbols(self, word: list):
        """
        Counts quantity of each symbol in word
        :param word:
        :return:
        """
        counted_symbols = {}
        for i in set(word):
            counted_symbols[i] = word.count(i)
        return counted_symbols

    def check_word(self, players_word: list, guess_word: list):
        """
        This method perform single round of game
        :return: No return statement
        """
        if players_word == guess_word:
            print(f"{players_word} is correct answer!")
            self.game_over = True
            return
        if self.mode:
            print(f"{guess_word}")
        self.clear_symbols()
        for x, y in zip(players_word, guess_word):
            if x == y:
                self.symbols['correct'] += 1
            elif x in guess_word:
                self.symbols['wrong position'] += 1
            else:
                self.wrong_letters.append(x)
                self.symbols['wrong'] += 1
        self.round += 1
        self.traceback['rounds'] = self.round
        print(
            f"{players_word} contains: "
            f"\033[32m {self.symbols['correct']} correct \033[1m "
            f"\033[33m {self.symbols['wrong position']} on wrong position \033[1m "
            f"\033[31m {self.symbols['wrong']} wrong symbols \033[1m \033[0m")
        print(f"{self.rounds_limit - self.round} rounds left")

    def play(self):
        guess_word = self.prepare_word(self.sym, self.len)
        self.counted_symbols = self.count_symbols(self.word)
        while not self.game_status() and self.rounds_limit > 0:
            while True:
                try:
                    players_word = self.read_word()
                except ValueError as err:
                    print(f"{err} TRY AGAIN")
                    continue
                else:
                    break

            self.check_word(players_word, guess_word)
        print(f"Game has ended.\n Word : {self.word}")

    def print_log(self):
        print(json.dumps(self.traceback))
        with open('data.json', 'w') as file:
            json.dump(self.traceback, file, indent=2)
