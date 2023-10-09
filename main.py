from board import *
from tkinter import *
import time

root = Tk()
# Creates the window size and color which the game will be played on
game_screen = Canvas(root, width=1500, height=1500, background="grey", highlightthickness=0)
game_screen.pack()

# Create a Board object and display it to start the game
myBoard = Board(game_screen, root)
myBoard.display_board()
# Perpetually move pieces down one square every second

# Allows for mouse clicks and keyboard inputs and focuses these inputs onto game_screen
game_screen.bind("<Key>", myBoard.keyboard_buttons)
game_screen.focus_set()

root.title("Tetris")
root.after(0, myBoard.gravity())
root.mainloop()