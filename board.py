from piece import Piece
import random
import time

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
        
        s.columns = 10
        s.rows = 20
        s.holder = []
        s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
        s.piece_colors = {"I":"cyan", "J":"purple", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
        s.board_array = [[None] * s.columns for i in range(s.rows)]
        s.board_array[3][7] = "Z"
        for row in s.board_array:
            print(row)
        s.piece_queue = [s.get_random_piece() for i in range(7)]    
        s.current_piece = s.get_random_piece()

        s.spawn_piece()

    def display_board(self):
        """
        Displays the board, scoreboard, whose move it is, etc.
        :return: None
        """
        s = self
        s.game_screen.delete("all")
        
        for row in range(s.rows):
            for col in range(s.columns): 
                # Board array squares
                print(f"row = {row}")
                print(f"col = {col}")
                print(s.board_array[row][col])
                if s.board_array[row][col] == None:
                    color = "black"
                else:
                    color = s.piece_colors[s.board_array[row][col]]
                    
                s.game_screen.create_rectangle(54 + 50 * col, 54 + 50 * row, 96 + 50 * col, 96 + 50 * row, fill=color,
                                                 outline=color)
                # Board array lines
                s.game_screen.create_line(50 * (col + 1), 50 * (row + 1), 50 * 9, 50 * (row + 1))
                s.game_screen.create_line(50 * (col + 1), 50 * (row + 1), 50 * (col + 1), 50 * 9)
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
        s.spawn_piece()
        s.piece_queue.append(s.get_random_piece())

    def get_random_piece(self):
        s = self
        random_int = random.randint(0, 6)
        random_piece = s.piece_list[random_int]
        return Piece(random_piece)

    def spawn_piece(self):
        s = self
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        s.display_board()
        
    def rotate(self, direction):
        s = self
        s.display_board()
        
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
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        s.display_board()
            
    def soft_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        s.display_board()
        
    def hard_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        s.hard_drop()
        s.display_board()
            
    def gravity(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            square[1] = square[1] + 1
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        print("test")
        time.sleep(1)
        s.gravity()
        s.display_board()
        
    def valid_movement(self, type_of_movement):
        if type_of_movement == "down":
            return True
        elif type_of_movement == "left":
            return True
        elif type_of_movement == "right":
            return True
        elif type_of_movement == "rotate":
            return True

    def place(self):
        s = self
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
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
