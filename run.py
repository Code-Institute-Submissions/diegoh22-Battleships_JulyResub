from random import randint

class board:

   def __init__(self, size, num_ships, name, player=False):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player = player
        self.ships = []
        self.guesses = []
        self.populate()


    def view_board(self):
        
        view_board(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))   

    def add_ship(self):
        """
        Populates the board with ships
        """
        board = [["." for x in range(self.size)] for y in range(self.size)]
        self.board = board
        for _ in range(self.num_ships):
            x, y = random_coordinate(self.size)
            while (x, y) in self.ships:
                x, y = random_coordinate(self.size)
            self.ships.append((x, y))
            if self.player:
                self.board[x][y] = "@" 

    def guess(self, x, y):
       
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return True
        else:
            return False  
    
    def already_guessed(self, x, y):
    
        if (x, y) in self.guesses:
            return True
        return False
