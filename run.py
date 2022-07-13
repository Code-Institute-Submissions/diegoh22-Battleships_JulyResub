from random import randint

scores = {"computer": 0, "player": 0}


class Board:

    def __init__(self, size num_ships, name, type):
        self.size = size
        self.board = [["." for x in range (size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type
        self.guesses = []
        self.ships = []

    def print (self):
        for row in self.board:
            print("".joing(row))

    def guess(self, x, y):
        self.guesses.append((x,y))
        self.board[x] [y] = "X"

        if (x, y) in self.ships:
            self.board[x] [y] = "*"
            return "Hit"
        else:
            return "Miss"   

    def add_ship(self, x, y, type="computer"):
        if len(self.ship) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.shipd.append((x, y))
            if self.type == "player":
                self.board[x] [y] = "@"  

def valid_coordinates(x, y, board):
    pass

def populate_board(board):
    pass

def make_guess(board):
    pass

def play_game(computer_board, player_board):
    pass

def new_game():
    pass









new_game()