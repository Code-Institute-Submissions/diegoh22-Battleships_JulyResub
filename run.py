from random import randint

scores = {"computer": 0, "player": 0}


class Board:

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"   

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"  

def random_point(size):

    return randint(0, size - 1)             

def valid_coordinates(x, y, board):
    pass

def populate_board(board):
    pass

def make_guess(board):
    pass

def play_game(computer_board, player_board):
    pass

def new_game():
    size = 7
    num_ships = 5
    scores["computer"] = 0
    scores["palyer"] = 0
    print("_" * 40)
    print("WELCOME TO BATTLESHIPS")
    print(f" Board size: {size}. Number of ships: {num_ships}")
    print(" Top Left Corner is Row 0, col: 0")
    print("_" * 40)
    player_name = input("Enter your name: ")
    print("-" * 40)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)    


new_game()
