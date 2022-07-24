from random import randint


def rand_coordinate(board_size):

    x = randint(0, board_size - 1)
    y = randint(0, board_size - 1)
    return(x, y)

def valid_coordinates(x, y, board_size):

    if 0 <= x < board_size and 0 <= y < board_size:
        return True

    return False  


class Board:

    def __init__(self, size, turn, num_ships, name, player):
        self.size = size
        self.num_ships = num_ships
        self.turn = turn
        self.player = player
        self.name = name
        self.ships = []
        self.populate = []



