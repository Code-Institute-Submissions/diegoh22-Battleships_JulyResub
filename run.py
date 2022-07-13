from random import randint


#print("Welcome to Battleship, Please follow the rules and enjoy of today game")
#print('Ideas are ideas, check the Ships en Sunk them')
#p1 = str(input("Enter your nickname : "))
#Board for holding ship locations
PLAYER_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
       
# By writing this as a function, we don't have
#  to repeat it later. It's less code, it makes
# the rest easier to read, and if we improve this, we have to do it only once!
def ask_user_for_board_position():
    column = input("column (A to H):")
    while column not in "ABCDEFGH":
        print("That column is wrong! It should be A, B, C, D, E, F or H")
        column = input("column (A to H):")

    row = input("row (1 to 7):")
    while row not in "1234567":
        print("That row is wrong! it should be 1, 2, 3, 4, 5, 6 or 7")
        row = input("row (1 to 7):")

    # The code calling this function will receive the values
    #  listed in the return statement below
    # and it can assign it to variables
    return int(row) - 1, letters_to_numbers[column]


def print_board(board):
    # Show the board, one row at a time
    print("  A B C D E F G H")
    print(" +-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" +-+-+-+-+-+-+-+")
        row_number = row_number + 1


# We want 5 battleships, so we use a for loop to ask for a ship 5 times!
for n in range(5):
    print("Where do you want ship ", n + 1, "?")
    row_number, column_number = ask_user_for_board_position()

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")

    board[row_number][column_number] = 'X'
    print_board(board)

    # computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(PLAYER_GUESS_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(PLAYER_BOARD)
        row, column = get_ship_location()
        if PLAYER_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif PLAYER_GUESS_BOARD[row][column] == "X":
            print("Hit")
            PLAYER_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            PLAYER_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(PLAYER_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")