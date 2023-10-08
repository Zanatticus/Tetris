from piece import Piece
import random


class Board:
    """
    Board class handles all the displaying of the board to the screen and everything else associated with the board.
    """
    def __init__(self, game_screen, root):
        """
        Initializes a 10x20 Tetris board
        """
        s = self
        s.game_screen = game_screen
        s.root = root
        
        s.row = 0
        s.column = 0
        s.holder = []
        s.board_array = []
        s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
        s.piece_colors = {"I":"cyan", "J":"pink", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
        
        s.piece_queue = []
        for i in range(7):
            s.piece_queue.append(s.get_random_piece())
        s.current_piece = s.get_random_piece()
        
        for i in range(10):
            s.board_array.append([])
            for j in range(20):
                s.board_array[i].append("I")


    def display_board(self):
        """
        Displays the board, scoreboard, whose move it is, etc.
        :return: None
        """
        s = self
        s.game_screen.delete("all")
        
        for x in range(10):
            for y in range(20):
                s.row = x
                s.column = y
                # Board array squares
                if s.board_array[x][y] in s.piece_list:
                    color = s.piece_colors[s.board_array[x][y]]
                    s.game_screen.create_rectangle(54 + 50 * x, 54 + 50 * y, 96 + 50 * x, 96 + 50 * y, fill=color,
                                                 outline=color)
                # Board array lines
                s.game_screen.create_line(50 * (x + 1), 50 * (y + 1), 50 * 9, 50 * (y + 1))
                s.game_screen.create_line(50 * (x + 1), 50 * (y + 1), 50 * (x + 1), 50 * 9)
        # Board array boundaries
        s.game_screen.create_line(50, 50 * 9, 50 * 9, 50 * 9)
        s.game_screen.create_line(50 * 9, 50, 50 * 9, 50 * 9)      
        
        # Piece queue
        s.game_screen.create_rectangle(700, 100, 1000, 500, fill="black",
                                                 outline="grey")

        # Holder
        s.game_screen.create_rectangle(700, 600, 1000, 850, fill="black",
                                                 outline="grey")

    def get_next_piece(self):
        s = self
        s.current_piece = s.piece_queue.pop(0)
        s.piece_queue.append(s.get_random_piece())

    def get_random_piece(self):
        s = self
        random_piece = s.piece_list[random.randint(0, 6)]
        return Piece(random_piece)



    def rotate(self, direction):
        s = self

    def shift(self, direction):
        s = self
        if s.valid_movement(direction) == False:
            return
        if direction == "left":
            direction = -1
        elif direction == "right":
            direction = 1    
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[0] = square[0] + direction
            s.board_array[square[0]][square[1]] = s.current_piece.color
            
    def soft_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.color
        
    def hard_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.color
        s.hard_drop()
            
    def gravity(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.color
        s.game_screen.after(1, s.gravity)

    def valid_movement(self, type_of_movement):
        if type_of_movement == "down":
            pass
        elif type_of_movement == "left":
            pass
        elif type_of_movement == "right":
            pass
        elif type_of_movement == "rotate":
            pass

    def place(self):
        s = self
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = s.current_piece.color
        s.clear_line()

    def clear_line(self):
        s = self
        last_row = s.board_array[-1]
        clear_counter = 0
        for square in last_row:
            if square == None:
                return clear_counter
        s.board_array = [None] * 10 + s.board_array[:-1]
        clear_counter = 1
        return clear_counter + s.clear_line()  
        
    def hold(self):
        s = self
        if s.holder == []:
            s.holder.append(s.current_piece)
            s.get_next_piece()
            return   
        held_piece = s.holder.pop[0]
        s.current_piece = held_piece
        return held_piece            
            
      
            
            
    def keyboard_buttons(self, event):
        """
        Handles keyboard input to either:
            a) restart
            b) quit
            c) move
            d) rotate
            e) hold
            f) hard drop
            g) soft drop
        :param event: keyboard input
        :return: None
        """
        s = self
        button_pressed = event.keysym
        if button_pressed.lower() == "r":
            s.play_new_game()
        elif button_pressed.lower() == "q":
            s.root.destroy()
        elif button_pressed.lower() == "j":
            s.rotate("counter_clockwise")
        elif button_pressed.lower() == "l":
            s.rotate("clockwise")
        elif button_pressed.lower() == "a":
            s.shift("left")
        elif button_pressed.lower() == "d":
            s.shift("right")
        elif button_pressed.lower() == "i":
            s.hold_piece()
        elif button_pressed.lower() == "w":
            s.hard_drop()   
        elif button_pressed.lower() == "s":
            s.soft_drop()            
    
    def play_new_game(self):
        """
        Restarts the game.
        :return: None
        """
        s = self
        s.logistics.play_new_game()
        s.game_screen.delete("all")
        s.__init__(s.game_screen, s.root)
        s.display_board()
