from random import randint


def random_coordinate(grid_size):
    
    x = randint(0, grid_size - 1)
    y = randint(0, grid_size - 1)
    return (x, y)


def valid_coordinates(x, y, grid_size):
   
    if 0 <= x < grid_size and 0 <= y < grid_size:
        return True

    return False


class Board:
    
    def __init__(self, size, num_ships, name, player=False):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player = player
        self.ships = []
        self.guesses = []
        self.populate()
        
    def print(self):
        
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))

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

    def last_guess(self):
        
        return self.guesses[-1]

    def populate(self):
       
        board = [["." for x in range(self.size)] for y in range(self.size)]
        self.board = board
        for _ in range(self.num_ships):
            x, y = random_coordinate(self.size)
            while (x, y) in self.ships:
                x, y = random_coordinate(self.size)
            self.ships.append((x, y))
            if self.player:
                self.board[x][y] = "@"


class Game:
   
    def __init__(self, size, num_ships):
        self.size = size
        self.num_ships = num_ships
        self.scores = {"computer": 0, "player": 0}
        
    def start(self):
        
        self.show_info()
        tmp_board = Board(self.size, self.num_ships, "Computer", player=False)
        self.computer_board = tmp_board
        player_name = input("Please enter your name:\n")
        print("-" * 45)
        tmp_board = Board(self.size, self.num_ships, player_name, player=True)
        self.player_board = tmp_board

        self.play()

    def play(self):
        tunrs = 10
        while True:
            self.print_boards()
            
            # player guess
            x, y = self.make_guess()
            while not self.valid_guess(x, y):
                x, y = self.make_guess()
            player_hit = self.computer_board.guess(x, y)

            # computer guess
            x, y = random_coordinate(self.size)
            while self.player_board.already_guessed(x, y):
                x, y = random_coordinate(self.size)
            computer_hit = self.player_board.guess(x, y)

            # end of round
            self.round_tally(player_hit, computer_hit)
            
            if tunrs <= 1:
                print("GAME OVER YOUR ARE OUT OF TUNRS")
                break
            print("You have" + str(tunrs) + "turns remaining")
            tunrs -= 1
             
    def make_guess(self):
       
        while True:
            try:
                print("-" * 45)
                x = input("Guess a row:\n")
                x = int(x)
                y = input("Guess a column:\n")
                y = int(y)
                break
            except ValueError:
                print("Row and column must be numbers")

        return (x, y)

    def print_boards(self):
        
        self.player_board.print()
        self.computer_board.print()

    def valid_guess(self, x, y):
       
        if not valid_coordinates(x, y, self.size):
            print(f"Row and column must be between 0 and {self.size - 1}")
            return False
        if self.computer_board.already_guessed(x, y):
            print("You cannot guess the same coordinates more than once.")
            return False

        return True

    def game_over(self):
       
        if self.scores["player"] >= self.num_ships or \
           self.scores["computer"] >= self.num_ships:
            return True
        return False

    def round_tally(self, player_hit, computer_hit):
        """
        Output the scores after each round
        """
        print("-" * 45)
        print(f"{self.player_board.name} guessed " +
              f"{self.computer_board.last_guess()}")
        if player_hit:
            self.scores["player"] += 1
            print("That was a hit!")
        else:
            print("That was a miss!")
        print(f"Computer guessed {self.player_board.last_guess()}")
        if computer_hit:
            self.scores["computer"] += 1
            print("That was a hit!")
        else:
            print("That was a miss!")
        print("\nAfter this round, the scores are:")
        print(f"{self.player_board.name}:" +
              f"{self.scores['player']} . Computer:{self.scores['computer']}")
        print("-" * 45)
            
    def show_info(self):
        
        print("-" * 45)
        print(" Welcome to the great battle of BATTLESHIPS!!")
        print(f" Board Size: {self.size}. Number of ships: {self.num_ships}.")
        print(" You have 10 tunrs to the sunk 5 ships")
        print(" Top left corner is row: 0, col: 0")
        print("-" * 45)

# Ask the user what grid size to use, validate the size, then start a new game


game = Game(size=10, num_ships=5,)
game.start()