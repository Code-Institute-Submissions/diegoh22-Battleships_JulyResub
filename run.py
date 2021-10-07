
from random import randint

board = []

# Create 7 x 7 board

for x in range(7):
    board.append(["O"] * 7)


# Function to display current board status

def print_board(board):
    for row in board:
        print(" ").join(row)


print("Let's play Battleship!")
print_board(board)

# Functions to randomly select ship coordinates


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


# Get random coordinates for ship 1

ship1_row = random_row(board)
ship1_col = random_col(board)

# Get random coordinates for ship 2;
# try again up to 10 times if they are the same as ship 1

for i in range(10):
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    if ship2_row != ship1_row and ship2_col != ship1_col:
        break

# Cheat by printing positions (for testing, I swear!)

print("ship1: " + str(ship1_row) + " " + str(ship1_col)
print("ship2: " + str(ship2_row) + " " + str(ship2_col)




# set initial "win" status as false; these
# keep track of which of the two ships have been found

ship1_won = False
ship2_won = False

for turn in range(10):

    # Get user guesses

    print "Turn #" + str(turn + 1)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))


    # Check to see if user guesses match ship 1 and
    # check to see if ship 1 hasn't already been found

    if {(guess_row == ship1_row and guess_col ==
         ship1_col and ship1_won == False)}:
        print("Congratulations! One ship down!")
        ship1_won = True

        # Set board space to "B" to show correct guess

        board[guess_row][guess_col] = "B"

        # Declare game over if both ships have been found

        if ship1_won == True and ship2_won == True:
            print "Congratulations! You sunk both battleships!"
            break

    elif {(guess_row == ship2_row and guess_col ==
           ship2_col and ship2_won = False)}:
        print "Congratulations! One ship down!"
        ship2_won = True
        board[guess_row][guess_col] = "B"
        if ship1_won = True and ship2_won = True:
            print "Congratulations! You sunk both battleships!"
            break

    else:
        if turn == 5:
            print "Game Over"

        elif {(guess_row < 0 or guess_row > len(board[0])-1) or
              (guess_col < 0 or guess_col > len(board[0])-1)}:
            print "Oops, that's not even in the ocean."

        elif{(board[guess_row][guess_col] == "X") or
             (board[guess_row][guess_col] == "B")}:
            print "Sorry! You fired in the same spot!"

        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

    turn += 1
    print
    print_board(board)
    print