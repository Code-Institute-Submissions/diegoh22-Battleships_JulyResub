

from random import randint
import os
'''

Game startin fucntion

'''
p1 = str(input("Lest play Enter your nickname : "))
os.system('clear')
board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)

'''

Pick the randon row and col

'''


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

'''

Guess the ships and  end game fuction

'''
for turn in range(5):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print(turn + 1)
        print_board(board)
        if turn > 4:
            print("Game Over")
            print("the real ship location is")

'''

Gamen over call

'''
if ship_col:
    print("You missed my battleship Game Over")

else:
    print("All the ships are sunk. You win!")
print(ship_col)
