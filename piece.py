class Piece:
     def __init__(s, piece_type):
          s.piece_type = piece_type
          s.last_held = 1
          s.position = None
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
          if piece_type == "L":
               s.color = "orange"
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,2], [1,0], [1,1], [1,2]]
               s.pivot = 2 # 3rd coordinate [1, 4]
          if piece_type == "O":
               s.color = "FFD700"
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [0,2], [1,1], [1,2]]
               s.pivot = None
          if piece_type == "S":
               s.color = "red"
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
               s.queue_coordinates = [[0,1], [0,2], [1,0], [1,1]]
               s.pivot = 3 # 4th coordinate [1, 4]
          if piece_type == "T":
               s.color = "magenta"
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [1,0], [1,1], [1,2]]
               s.pivot = 2 # 3rd coordinate [1, 4]
          if piece_type == "Z":
               s.color = "green"
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]
               s.queue_coordinates = [[0,0], [0,1], [1,1], [1,2]] 
               s.pivot = 2 # 3rd coordinate [1, 4]

     def reset_piece(s):
          if s.piece_type == "I":
               s.coordinates = [[1,3], [1,4], [1,5], [1,6]]
               s.position = 0
               s.held = 1
          if s.piece_type == "J":
               s.coordinates = [[0,3], [1,3], [1,4], [1,5]]
               s.held = 1
          if s.piece_type == "L":
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
               s.held = 1
          if s.piece_type == "O":
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
               s.held = 1
          if s.piece_type == "S":
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
               s.held = 1
          if s.piece_type == "T":
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
               s.held = 1
          if s.piece_type == "Z":
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]
               s.held = 1

     def shift_piece(s, direction):
          if direction == "left":
               direction = -1
          elif direction == "right":
               direction = 1
          for square in s.coordinates:
               square[1] = square[1] + direction

     def drop_piece(s):
          for square in s.coordinates:
               square[0] = square[0] + 1
               
     def create_rotated_piece(s, direction):
          rotated_piece = []
          pivot_row, pivot_col = s.coordinates[s.pivot]
          row_modifier = 0
          column_modifier = 0
          piece_type = "I"
          
          if direction == "clockwise":
               direction = 1
               if piece_type == "I":
                    if s.position == 0:
                         row_modifier = 1 
                    if s.position == 1:
                         column_modifier = -1
                    if s.position == 2:
                         row_modifier = -1 
                    if s.position == 3:
                         column_modifier = 1
          elif direction == "counter-clockwise":
               direction = -1
               if piece_type == "I":
                    if s.position == 0:
                         column_modifier = -1
                    if s.position == 1:
                         row_modifier = 1
                    if s.position == 2:
                         column_modifier = 1 
                    if s.position == 3:
                         row_modifier = -1
          
          for [row, col] in s.coordinates:
               # Calculate the new coordinates after rotation around the pivot point
               new_row = pivot_row + (col - pivot_col) * direction
               new_col = pivot_col - (row - pivot_row) * direction   
               rotated_piece.append([new_row + row_modifier, new_col + column_modifier])
          return rotated_piece
     
     def rotate_piece(s, rotated_piece):
          s = rotated_piece
