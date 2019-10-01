import mastermind as game
import game_config as conf

length, symbols, round_count = conf.prepare_game_parameters()

obj = game.Mastermind(length, symbols, round_count, False)

obj.play()

obj.print_log()
