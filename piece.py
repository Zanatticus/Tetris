class Piece:
     def __init__(self, piece_type):
          s = self
          s.piece_type = piece_type
          #s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
          #s.piece_colors = {"I":"cyan", "J":"pink", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
          s.last_held = 0
          
          if piece_type == "I":
               s.color = "cyan"
               s.coordinates = [[1,3], [1,4], [1,5], [1,6]]
               s.queue_coordinates = [[0,0], [0,1], [0,2], [0,3]]
               s.pivot = 2 # 3rd coordinate [1, 5]
               s.position = 0
          if piece_type == "J":
               s.color = "pink"
               s.coordinates = [[0,3], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,0], [1,0], [1,1], [1,2]]
               s.pivot = 2 # 3rd coordinate [1, 4]
               s.position = None
          if piece_type == "L":
               s.color = "orange"
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,2], [1,0], [1,1], [1,2]]
               s.pivot = 2 # 3rd coordinate [1, 4]
               s.position = None
          if piece_type == "O":
               s.color = "yellow"
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [0,2], [1,1], [1,2]]
               s.pivot = None
               s.position = None
          if piece_type == "S":
               s.color = "red"
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
               s.queue_coordinates = [[0,1], [0,2], [1,0], [1,1]]
               s.pivot = 3 # 4th coordinate [1, 4]
               s.position = None
          if piece_type == "T":
               s.color = "magenta"
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [1,0], [1,1], [1,2]]
               s.pivot = 2 # 3rd coordinate [1, 4]
               s.position = None
          if piece_type == "Z":
               s.color = "green"
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]
               s.queue_coordinates = [[0,0], [0,1], [1,1], [1,2]] 
               s.pivot = 2 # 3rd coordinate [1, 4]
               s.position = None

     def reset_coordinates(self):
          s = self
          if s.piece_type == "I":
               s.coordinates = [[1,3], [1,4], [1,5], [1,6]]
               s.position = 0
          if s.piece_type == "J":
               s.coordinates = [[0,3], [1,3], [1,4], [1,5]]
          if s.piece_type == "L":
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
          if s.piece_type == "O":
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
          if s.piece_type == "S":
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
          if s.piece_type == "T":
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
          if s.piece_type == "Z":
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]

     def shift_piece(self, direction):
          s = self
          if direction == "left":
               direction = -1
          elif direction == "right":
               direction = 1
          for [row, col] in s.coordinates:
               col = col + direction

     def drop_piece(self):
          s = self
          for [row, col] in s.coordinates:
               row = row + 1
               
     def rotate_piece(piece, direction, pivot, position = None):
          rotated_piece = []
          pivot_row, pivot_col = piece[pivot]
          row_modifier = 0
          column_modifier = 0
          piece_type = "I"
          
          if direction == "clockwise":
               direction = 1
               if piece_type == "I":
                    if position == 0:
                         row_modifier = 1 
                    if position == 1:
                         column_modifier = -1
                    if position == 2:
                         row_modifier = -1 
                    if position == 3:
                         column_modifier = 1
          elif direction == "counter-clockwise":
               direction = -1
               if piece_type == "I":
                    if position == 0:
                         column_modifier = -1
                    if position == 1:
                         row_modifier = 1
                    if position == 2:
                         column_modifier = 1 
                    if position == 3:
                         row_modifier = -1
          
          for [row, col] in piece:
               # Calculate the new coordinates after rotation around the pivot point
               new_row = pivot_row + (col - pivot_col) * direction
               new_col = pivot_col - (row - pivot_row) * direction   
               rotated_piece.append([new_row + row_modifier, new_col + column_modifier])
          return rotated_piece