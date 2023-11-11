from board import *
from tkinter import *
#from tkinter import Canvas, PhotoImage, Tk

root = Tk()

# Creates the window size and color which the game will be played on
root.geometry("850x1500")

#image = ImageTk.PhotoImage(file = "C:\Users\zinga\Tetris\Tetris.png")
game_screen = Canvas(root, bg = 'grey')
game_screen.pack(expand=YES, fill=BOTH)

root.wm_attributes('-transparentcolor', "grey")

# Create a Board object and display it to start the game
myBoard = Board(game_screen, root)
myBoard.display_board()

# Allows for mouse clicks and keyboard inputs and focuses these inputs onto game_screen
game_screen.bind("<Key>", myBoard.keyboard_buttons)
game_screen.focus_set()

root.title("Tetris")
root.mainloop()
