from piece import Piece
import random
from tkinter import *
from ctk_scoreboard import ScoreboardApp
import darkdetect
import customtkinter
import csv

class Board:
    """
    Board class handles all the displaying of the board to the screen and everything else associated with the board.
    """
    gravity_count = 0
    def __init__(s, root, game_screen, scoreboard_screen):
        """
        Initializes a 10x20 Tetris board
        """
        s.root = root
        s.game_screen = game_screen
        
        s.scoreboard_screen = scoreboard_screen
        s.csv_filepath = "scoreboard.csv"
        s.score_dict = {}
        with open(s.csv_filepath, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            # Assuming the first row contains column headers
            headers = next(csv_reader, None)
            for row in csv_reader:
                if row:  # Skip empty rows
                    name = row[0]
                    score = float(row[1])  # Assuming scores are numeric, adjust if needed
                    s.score_dict[name] = score
            s.score_dict = dict(sorted(s.score_dict.items(), key=lambda item: item[1], reverse=True))
        s.create_widgets()
        
        system_color_mode = darkdetect.theme()
        if system_color_mode == 'Dark':
            s.fill_color = 'black'
            s.outline_color = 'white'
        else:
            s.fill_color = 'white'
            s.outline_color = 'black'
            
        s.game_over = 0
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
        s.gravity_timer = 1000
        s.root.after(0, s.gravity())

    def reset(s):
        s.points = 0
        s.game_over = 0
        s.holder = []
        s.board_array = [[None] * s.columns for i in range(s.rows)]
        s.queue_array = [[None] * s.queue_columns for i in range(s.queue_rows)]
        s.holder_array = [[None] * s.holder_columns for i in range(s.holder_rows)]
        s.piece_queue = [s.get_random_piece() for i in range(7)]    
        s.current_piece = s.get_random_piece()
        s.update_queue_array()
        s.spawn_piece()
        s.root.after(0, s.gravity())
        
    def display_board(s):
        """
        Displays the board, scoreboard, etc.
        :return: None
        """
        s.game_screen.delete("all")
        if s.game_over == 1:
            return
        unit = 50
        s.game_screen.create_text(unit * 14, unit * 17.5, text=f"SCORE:", fill=s.outline_color, font=40)
        s.game_screen.create_text(unit * 14, unit * 18, text=f"{s.points}", fill=s.outline_color, font=40, anchor="center")
        
        for row in range(s.rows):
            for col in range(s.columns): 
                # Board array squares
                if s.board_array[row][col] == None:
                    color = s.fill_color
                else:
                    color = s.piece_colors[s.board_array[row][col]] 
                s.game_screen.create_rectangle(1 + unit * (col + 1), 1 + unit * (row + 1), -1 + unit * (col + 2), -1 + unit * (row + 2), fill=color, outline=color)
     
        # Create horizontal border lines
        for r in range(21):
            s.game_screen.create_line(unit, unit * (r + 1), unit * 11, unit * (r + 1), fill=s.outline_color, width = 2)
        # Create vertical border lines
        for c in range(11):    
            s.game_screen.create_line(unit * (c + 1), unit, unit * (c + 1), unit * 21, fill=s.outline_color, width = 2)    
        
        # Piece queue
        for row in range(s.queue_rows):
            for col in range(s.queue_columns): 
                if s.queue_array[row][col] == None:
                    color = s.fill_color
                else:
                    color = s.piece_colors[s.queue_array[row][col]]
                s.game_screen.create_rectangle(1 + unit * (col + 12), 1 + unit * (row + 2), -1 + unit * (col + 13), -1 + unit * (row + 3), fill=color, outline=color)
        
        # Create 'NEXT' Text:
        s.game_screen.create_text(unit * 14, unit * 1.5, text="NEXT", fill=s.outline_color, font=40)
        
        # Create horizontal border lines for piece queue
        for r in range(12):
            s.game_screen.create_line(unit * 12, unit * (r + 2), unit * 16, unit * (r + 2), fill=s.outline_color, width = 2)
        # Create vertical border lines for piece queue
        for c in range(5):    
            s.game_screen.create_line(unit * (c + 12), unit * 2, unit * (c + 12), unit * 13, fill=s.outline_color, width = 2)    
        
        # Holder
        for row in range(s.holder_rows):
            for col in range(s.holder_columns): 
                if s.holder_array[row][col] == None:
                    color = s.fill_color
                else:
                    color = s.piece_colors[s.holder_array[row][col]]
                s.game_screen.create_rectangle(1 + unit * (col + 12), 1 + unit * (row + 14), -1 + unit * (col + 13), -1 + unit * (row + 15), fill=color, outline=color)

        # Create 'HOLD' Text:
        s.game_screen.create_text(unit * 14, unit * 13.5, text="HOLD", fill=s.outline_color, font=40)

        # Create horizontal border lines for holder
        for r in range(3):
            s.game_screen.create_line(unit * 12, unit * (r + 14), unit * 16, unit * (r + 14), fill=s.outline_color, width = 2)
        # Create vertical border lines for holder
        for c in range(5):    
            s.game_screen.create_line(unit* (c + 12), unit * 14, unit * (c + 12), unit * 16, fill=s.outline_color, width = 2)
    
    def hold_piece(s):
        if s.holder == []:
            for [row, col] in s.current_piece.coordinates:
                s.board_array[row][col] = None
            s.current_piece.reset_piece()
            s.holder.append(s.current_piece)
            s.update_holder_array()
            s.get_next_piece()
        else:
            if s.holder[0].held == 1:
                return
            for [row, col] in s.current_piece.coordinates:
                s.board_array[row][col] = None
            s.current_piece.reset_piece()
            s.holder.append(s.current_piece)
            s.current_piece = s.holder.pop(0)
            s.update_holder_array()
            s.spawn_piece()

    def update_holder_array(s):
        s.holder_array = [[None] * s.holder_columns for i in range(s.holder_rows)]
        for [row, col] in s.holder[0].queue_coordinates:
            s.holder_array[row][col] = s.holder[0].piece_type
       
    def update_queue_array(s):
        counter = 0
        s.queue_array = [[None] * s.queue_columns for i in range(s.queue_rows)]
        for piece in s.piece_queue:
            if counter == 4:
                return
            for [row, col] in piece.queue_coordinates:
                s.queue_array[row + 3*counter][col] = piece.piece_type
            counter += 1        
    
    def get_next_piece(s):
        s.current_piece = s.piece_queue.pop(0)
        s.spawn_piece()
        s.piece_queue.append(s.get_random_piece())
        s.update_queue_array()
        
    def get_random_piece(s):
        random_int = random.randint(0, 1000) % 7
        random_piece = s.piece_list[random_int]
        return Piece(random_piece)

    def spawn_piece(s):
        for [row, col] in s.current_piece.coordinates:
            if s.board_array[row][col] != None:
                s.end_game()
                return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        s.display_board()
        
    def end_game(s):
        s.game_over = 1
        s.game_screen.delete("all")
        s.game_screen.pack_forget()
        s.scoreboard_screen.pack(expand=1, fill='both')
        s.scoreboard_screen.focus_set()
        s.scoreboard_screen.bind("<Key>", s.scoreboard_keyboard_buttons)
        s.scoreboard_screen.bind("<Button-1>", s.click_event)

        if s.points != 0:
            s.create_score_submission()
        #ScoreboardApp(s.root, s.scoreboard_screen, s.game_screen, s.points)
        #s.game_screen.focus_set()
        #TODO PROFANITY FILTER
    
    
    def create_widgets(s):
        # Game Over text
        s.scoreboard_label1 = customtkinter.CTkLabel(s.scoreboard_screen, text="GAME OVER!", font=("Helvetica", 45))
        s.scoreboard_label1.pack(pady=10)
        # Restart/Quit text
        s.scoreboard_label2 = customtkinter.CTkLabel(s.scoreboard_screen, text="Press 'R' to restart or 'ESC' to quit!", font=("Helvetica", 30))
        s.scoreboard_label2.pack(pady=10)
        # Label for displaying the scoreboard
        s.scoreboard_label3 = customtkinter.CTkLabel(s.scoreboard_screen, text="Scoreboard", font=("Helvetica", 30))
        s.scoreboard_label3.pack(pady=10)
        
        # Listbox to display scores
        s.score_frame = customtkinter.CTkScrollableFrame(s.scoreboard_screen, width=200, height=400)
        s.score_frame.pack()
        
        for name in s.score_dict:
            txt = f"{name}: {int(s.score_dict.get(name))}"
            s.score_entry = customtkinter.CTkLabel(s.score_frame, text=txt)
            s.score_entry.pack()
    
    def click_event(s, event):
        x,y = s.scoreboard_screen.winfo_pointerxy()                   # get the mouse position on screen
        widget = s.scoreboard_screen.winfo_containing(x,y)            # identify the widget at this location
        if (widget == ".text_widget") == False:                       # if the mouse is not over the text widget
            s.scoreboard_screen.focus_set()                           # focus on root
            
    def create_score_submission(s):
        # Entry fields for name and score
        s.name_label = customtkinter.CTkLabel(s.scoreboard_screen, text="Name:")
        s.name_label.pack()
        s.name_entry = customtkinter.CTkEntry(s.scoreboard_screen)
        s.name_entry.pack()
        
        # Add score button
        s.add_score_button = customtkinter.CTkButton(s.scoreboard_screen, text="Add Score", command=s.add_score)
        s.add_score_button.pack(pady=10)

    def add_score(s):
        name = s.name_entry.get().upper()
        score = s.points
        
        if name and score:
            name = name[:10]
            existing_score = s.score_dict.get(name)
            
            if existing_score != None:    
                if score <= s.score_dict.get(name):
                    print("Can only override a score with same name if the new score is higher")
                    return
            
            s.score_dict[name] = score
            txt = f"{name}: {s.score_dict.get(name)}"
            
            # Sort the score dict
            s.score_dict = dict(sorted(s.score_dict.items(), key=lambda item: item[1], reverse=True))
            
            # Clear existing contents of the CSV file
            with open(s.csv_filepath, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows([])  # Writing an empty list to clear the file

            # Write the dictionary to the CSV file
            with open(s.csv_filepath, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Write header
                csv_writer.writerow(['NAME', 'SCORE'])

                # Write data
                for name, score in s.score_dict.items():
                    csv_writer.writerow([name, score])
                    
            s.score_entry = customtkinter.CTkLabel(s.score_frame, text=txt)
            s.score_entry.pack()
            
            # Clear the entry fields
            s.add_score_button.destroy()
            s.name_entry.destroy()
            s.name_label.destroy()
    
    
    
    
    
    
    
    
    
    
    
    
    def rotate_piece(s, direction):
        if s.current_piece.piece_type == "O":
            return
        rotated_piece_coordinates = s.current_piece.create_rotated_piece(direction)
        if s.valid_rotation(rotated_piece_coordinates) == False:
            return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = None
        s.current_piece.coordinates = rotated_piece_coordinates
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        if s.current_piece.position != None:
            s.current_piece.position = (s.current_piece.position + 1) % 4
        s.display_board()
    
    def valid_rotation(s, rotated_piece):
        for [row, col] in rotated_piece:
            if [row, col] in s.current_piece.coordinates:
                continue
            if row > 19 or row < 0:
                return False
            if col > 9 or col < 0:
                return False
            if s.board_array[row][col] != None:
                return False
        return True
        
    def shift(s, direction):
        if s.valid_shift(direction) == False:
            return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = None
        s.current_piece.shift_piece(direction)
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        s.display_board()
        
    def soft_drop(s):
        if s.valid_shift("down") == False:
            s.place()
            return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = None
        s.current_piece.drop_piece()
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        s.display_board()
    
    def hard_drop(s):
        if s.valid_shift("down") == False:
            s.place()
            return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = None
        s.current_piece.drop_piece()
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        s.hard_drop()
        s.display_board()  
        
    def gravity(s):
        if s.game_over == 1:
            return
        if s.valid_shift("down") == False:
            s.place()
            s.display_board()
            s.root.after(s.gravity_timer, s.gravity)
            return
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = None
        s.current_piece.drop_piece()
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        s.display_board()
        s.root.after(s.gravity_timer, s.gravity) 
    
    def valid_shift(s, type_of_movement):
        for [row, col] in s.current_piece.coordinates:
            if type_of_movement == "down":
                if row + 1 > 19:
                    return False
                if s.board_array[row + 1][col] != None and [row + 1, col] not in s.current_piece.coordinates:
                    return False
                
            elif type_of_movement == "left":
                if col - 1 < 0:
                    return False
                if s.board_array[row][col - 1] != None and [row, col - 1] not in s.current_piece.coordinates:
                    return False
                
            elif type_of_movement == "right":
                if col + 1 > 9:
                    return False
                if s.board_array[row][col + 1] != None and [row, col + 1] not in s.current_piece.coordinates:
                    return False
        return True

    def place(s):
        clear_points = [0, 100, 300, 500, 800]
        for [row, col] in s.current_piece.coordinates:
            s.board_array[row][col] = s.current_piece.piece_type
        number_of_clears = s.clear_line()
        if number_of_clears:
            s.points += clear_points[number_of_clears]
            s.gravity_timer -= int(clear_points[number_of_clears] / 50)
        del s.current_piece
        if s.holder != []:
            s.holder[0].held = 0
        s.get_next_piece()
        
    def clear_line(s):
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
            
    def keyboard_buttons(s, event):
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
        button_pressed = event.keysym
        if button_pressed.lower() == "r":
            s.play_new_game()
        elif button_pressed.lower() == "escape":
            s.root.destroy()
        if s.game_over == 0:    
            if button_pressed.lower() == "q":
                s.rotate_piece("counter-clockwise")
            elif button_pressed.lower() == "e":
                s.rotate_piece("clockwise")
            elif button_pressed.lower() == "a":
                s.shift("left")
            elif button_pressed.lower() == "d":
                s.shift("right")
            elif button_pressed.lower() == "h":
                s.hold_piece()
            elif button_pressed.lower() == "w":
                s.hard_drop()   
            elif button_pressed.lower() == "s":
                s.soft_drop()            
    
    def scoreboard_keyboard_buttons(s, event):
        button_pressed = event.keysym
        if button_pressed.lower() == "r":
            try:
                s.add_score_button.destroy()
                s.name_entry.destroy()
                s.name_label.destroy()
            except:
                pass
            s.play_new_game()
        elif button_pressed.lower() == "escape":
            s.root.destroy()
    
    def play_new_game(s):
        """
        Restarts the game.
        :return: None
        """
        if s.game_over == 1:
            #s.scoreboard_screen.destroy()
            s.scoreboard_screen.pack_forget()
            s.game_screen.delete("all")
            s.reset()
            s.display_board()
            s.game_screen.pack(expand=1, fill='both')
            s.game_screen.focus_set()
        