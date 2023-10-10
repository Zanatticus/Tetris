from piece import Piece
import random
import time

class Board:
    """
    Board class handles all the displaying of the board to the screen and everything else associated with the board.
    """
    gravity_count = 0
    def __init__(self, game_screen, root):
        """
        Initializes a 10x20 Tetris board
        """
        s = self
        s.game_screen = game_screen
        s.root = root
        
        s.points = 0
        s.rows = 20
        s.columns = 10
        s.queue_rows = 11
        s.queue_columns = 4
        s.holder_rows = 2
        s.holder_columns = 4
        s.holder = []
        s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
        s.piece_colors = {"I":"cyan", "J":"purple", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
        s.board_array = [[None] * s.columns for i in range(s.rows)]
        s.queue_array = [[None] * s.queue_columns for i in range(s.queue_rows)]
        s.holder_array = [[None] * s.holder_columns for i in range(s.holder_rows)]
        s.piece_queue = [s.get_random_piece() for i in range(7)]    
        s.current_piece = s.get_random_piece()
        s.update_queue_array()
        s.spawn_piece()
        s.game_over = 0
        
    def reset(self):
        s = self
        s.points = 0
        s.rows = 20
        s.columns = 10
        s.queue_rows = 11
        s.queue_columns = 4
        s.holder_rows = 2
        s.holder_columns = 4
        s.holder = []
        s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
        s.piece_colors = {"I":"cyan", "J":"purple", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
        s.board_array = [[None] * s.columns for i in range(s.rows)]
        s.queue_array = [[None] * s.queue_columns for i in range(s.queue_rows)]
        s.holder_array = [[None] * s.holder_columns for i in range(s.holder_rows)]
        s.piece_queue = [s.get_random_piece() for i in range(7)]    
        s.current_piece = s.get_random_piece()
        s.update_queue_array()
        s.spawn_piece()
        s.game_over = 0

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
                if s.board_array[row][col] == None:
                    color = "black"
                else:
                    color = s.piece_colors[s.board_array[row][col]]
                    
                s.game_screen.create_rectangle(54 + 50 * col, 54 + 50 * row, 96 + 50 * col, 96 + 50 * row, fill=color, outline=color)
                # Board array lines
                s.game_screen.create_line(50 * (col + 1), 50 * (row + 1), 50 * 9, 50 * (row + 1))
                s.game_screen.create_line(50 * (col + 1), 50 * (row + 1), 50 * (col + 1), 50 * 9)
        # Board array boundaries
        s.game_screen.create_line(50, 50 * 9, 50 * 9, 50 * 9)
        s.game_screen.create_line(50 * 9, 50, 50 * 9, 50 * 9)      
        
        # Piece queue
        #s.game_screen.create_rectangle(700, 100, 1000, 500, fill="black", outline="grey")
        for row in range(s.queue_rows):
            for col in range(s.queue_columns): 
                if s.queue_array[row][col] == None:
                    color = "black"
                else:
                    color = s.piece_colors[s.queue_array[row][col]]
                s.game_screen.create_rectangle(700 + 50 * col, 100 + 50 * row, 742 + 50 * col, 142 + 50 * row, fill=color, outline=color)

        # Holder
        #s.game_screen.create_rectangle(700, 600, 1000, 850, fill="black", outline="grey")
        for row in range(s.holder_rows):
            for col in range(s.holder_columns): 
                if s.holder_array[row][col] == None:
                    color = "black"
                else:
                    color = s.piece_colors[s.holder_array[row][col]]
                s.game_screen.create_rectangle(700 + 50 * col, 700 + 50 * row, 742 + 50 * col, 742 + 50 * row, fill=color, outline=color)
    
    def hold_piece(self):
        s = self
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
            s.current_piece.reset_coordinates()
        if s.holder != []:
            held_piece = s.holder.pop(0)
            s.holder.append(s.current_piece)
            s.current_piece = held_piece
        if s.holder == []:
            s.holder.append(s.current_piece)    
            s.get_next_piece()  
        s.update_holder_array()
        s.spawn_piece()
               
    def update_holder_array(self):
        s = self
        s.holder_array = [[None] * s.holder_columns for i in range(s.holder_rows)]
        for square in s.holder[0].queue_coordinates:
            s.holder_array[square[0]][square[1]] = s.holder[0].piece_type
       
    def update_queue_array(self):
        s = self
        counter = 0
        s.queue_array = [[None] * s.queue_columns for i in range(s.queue_rows)]
        for piece in s.piece_queue:
            if counter == 4:
                return
            for square in piece.queue_coordinates:
                s.queue_array[square[0] + 3*counter][square[1]] = piece.piece_type
            counter += 1        
    
    def get_next_piece(self):
        s = self
        s.current_piece = s.piece_queue.pop(0)
        s.spawn_piece()
        s.piece_queue.append(s.get_random_piece())
        s.update_queue_array()
        
    def get_random_piece(self):
        s = self
        random_int = random.randint(0, 6)
        random_piece = s.piece_list[random_int]
        return Piece(random_piece)

    def spawn_piece(self):
        s = self
        for square in s.current_piece.coordinates:
            if s.board_array[square[0]][square[1]] != None:
                s.end_game()
                return
        for square in s.current_piece.coordinates:
                s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        s.display_board()
        
    def end_game(self):
        s = self
        s.game_screen.delete("all")
        s.game_screen.create_text(250, 470, text="GAME OVER! Press 'R' to restart or 'Q' to quit.",
                                         fill="black",
                                         font=40)
        s.game_over = 1
    
    def rotate_right(self):
        s = self
        if s.valid_movement("rotate_right") == False:
            return
        
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
        rotated_piece = []
        pivot_row, pivot_col = s.current_piece.pivot
        for [row, col] in s.current_piece:
            # Calculate the new coordinates after rotation around the pivot point
            new_row = pivot_row + (col - pivot_col)
            new_col = pivot_col - (row - pivot_row)
            rotated_piece.append([new_row, new_col])
        s.current_piece.coordinates = rotated_piece
        s.display_board()
        
    def rotate_left(self):
        s = self
        if s.valid_movement("rotate_left") == False:
            return
        
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = None
        rotated_piece = []
        pivot_row, pivot_col = s.current_piece.pivot
        for [row, col] in s.current_piece:
            # Calculate the new coordinates after rotation around the pivot point
            new_row = pivot_row - (col - pivot_col)
            new_col = pivot_col + (row - pivot_row)
            rotated_piece.append([new_row, new_col])
        s.current_piece.coordinates = rotated_piece
        s.display_board()
        
    def shift(self, direction):
        s = self
        if s.valid_movement(direction) == False:
            return
        piece_type = s.current_piece.piece_type
        if direction == "left":
            direction = -1
            piece_type = s.current_piece.piece_type
            for square in s.current_piece.coordinates:
                s.board_array[square[0]][square[1]] = None
                square[1] = square[1] + direction
                s.board_array[square[0]][square[1]] = piece_type
        elif direction == "right":
            direction = 1    
            piece_type = s.current_piece.piece_type
            for square in reversed(s.current_piece.coordinates):
                s.board_array[square[0]][square[1]] = None
                square[1] = square[1] + direction
                s.board_array[square[0]][square[1]] = piece_type
        s.display_board()
            
    def soft_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        piece_type = s.current_piece.piece_type
        for square in reversed(s.current_piece.coordinates):
            s.board_array[square[0]][square[1]] = None
            square[0] = square[0] + 1
            s.board_array[square[0]][square[1]] = piece_type
        s.display_board()
        
    def hard_drop(self):
        s = self
        if s.valid_movement("down") == False:
            s.place()
            return
        piece_type = s.current_piece.piece_type
        for square in reversed(s.current_piece.coordinates):
            s.board_array[square[0]][square[1]] = None
            square[0] = square[0] + 1
            s.board_array[square[0]][square[1]] = piece_type
        s.hard_drop()
        s.display_board()
            
    def gravity(self):
        s = self
        if s.game_over == 1:
            s.root.after(1000, s.gravity)
            return
        if s.valid_movement("down") == False:
            s.place()
            return
        piece_type = s.current_piece.piece_type
        for square in reversed(s.current_piece.coordinates):
            s.board_array[square[0]][square[1]] = None
            square[0] = square[0] + 1
            s.board_array[square[0]][square[1]] = piece_type
        s.display_board()
        s.root.after(1000, s.gravity)     
    
    
    # TODO ROTATION
    def valid_movement(self, type_of_movement):
        s = self
        current_coords = s.current_piece.coordinates
        for square in current_coords:
            row = square[0]
            col = square[1]
            if type_of_movement == "down":
                if row + 1 > 19:
                    return False
                if s.board_array[row + 1][col] != None and [row + 1, col] not in current_coords:
                    return False
                
            elif type_of_movement == "left":
                if col - 1 < 0:
                    return False
                if s.board_array[row][col - 1] != None and [row, col - 1] not in current_coords:
                    return False
                
            elif type_of_movement == "right":
                if col + 1 > 9:
                    return False
                if s.board_array[row][col + 1] != None and [row, col + 1] not in current_coords:
                    return False
                
            elif type_of_movement == "rotate_left":
                return True
            elif type_of_movement == "rotate_right":
                return True
        return True



    def place(self):
        s = self
        clear_points = [0, 100, 300, 500, 800]
        for square in s.current_piece.coordinates:
            s.board_array[square[0]][square[1]] = s.current_piece.piece_type
        number_of_clears = s.clear_line()
        if number_of_clears:
            s.points += clear_points[number_of_clears]
            print(s.points)
        del s.current_piece
        s.get_next_piece()
        
    def clear_line(self):
        s = self
        clear_counter = 0
        for row in s.board_array:
            square_counter = 0
            for square in row:
                if square == None:
                    break
                square_counter += 1
            if square_counter == 10:
                s.board_array.remove(row)
                s.board_array.insert(0, [None] * 10)
                clear_counter += 1        
        if clear_counter == 0:
            return 0
        else:
            return clear_counter + s.clear_line()
            
    def keyboard_buttons(self, event):
        """
        Handles keyboard input to either:
            a) restart
            b) quit
            c) rotate
            d) shift
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
            s.rotate_left()
        elif button_pressed.lower() == "l":
            s.rotate_right()
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
        s.game_screen.delete("all")
        s.reset()
        s.gravity()
        s.display_board()
