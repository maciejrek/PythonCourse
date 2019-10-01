def prepare_game_parameters():
    while True:
        try:
            length = int(input("Enter length of string\n"))
            if length < 1:
                raise ValueError("Length must be greater than 0")
        except ValueError as err:
            print(err)
            continue
        else:
            break

    while True:
        try:
            symbols = str(input("Enter symbols u wanna use as a string\n"))
            if not symbols:
                raise IndexError("Empty list of symbols\n")
        except IndexError as err:
            print(err)
            continue
        else:
            break

    while True:
        try:
            round_count = int(input("Enter number of rounds\n"))
            if round_count < 1:
                raise ValueError("Round count must be greater than 0")
        except ValueError as err:
            print(err)
            continue
        else:
            break

    return length, symbols, round_count
