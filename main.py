from board import *
from tkinter import *
from PIL import ImageTk

root = Tk()

# Creates the window size and color which the game will be played on

image = ImageTk.PhotoImage(file = "C:\Users\zinga\Tetris\Tetris.png")
#photo_image = PhotoImage(file="background_tetris.png")
game_screen = Canvas(root, width=1000, height=1500, bg = "gray", highlightthickness=0)

game_screen.create_image(0, 0, anchor="nw", image=image)

game_screen.pack(expand=YES, fill= BOTH)

# Create a Board object and display it to start the game
myBoard = Board(game_screen, root)
myBoard.display_board()
# Perpetually move pieces down one square every second

# Allows for mouse clicks and keyboard inputs and focuses these inputs onto game_screen
game_screen.bind("<Key>", myBoard.keyboard_buttons)
game_screen.focus_set()

root.title("Tetris")
root.mainloop()
