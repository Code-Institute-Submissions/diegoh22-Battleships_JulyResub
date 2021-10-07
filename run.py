import curses

# set up window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], '#')

# Game Logic
score = 0

ESC = 27
key = curses.KEY_RIGHT


while key != ESC:
    win.addstr(0, 2, 'Score' + str(score) + '')
    win.timeout(160 - (len(snake)) // 5 + len(snake)//10 % 120)
    event = win.getch()


curses.endwin()
print(f"Final Score = {score}")
