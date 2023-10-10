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
          if piece_type == "J":
               s.color = "pink"
               s.coordinates = [[0,3], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,0], [1,0], [1,1], [1,2]]
          if piece_type == "L":
               s.color = "orange"
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,2], [1,0], [1,1], [1,2]]
          if piece_type == "O":
               s.color = "yellow"
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [0,2], [1,1], [1,2]]
          if piece_type == "S":
               s.color = "red"
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
               s.queue_coordinates = [[0,1], [0,2], [1,0], [1,1]]
          if piece_type == "T":
               s.color = "magenta"
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
               s.queue_coordinates = [[0,1], [1,0], [1,1], [1,2]]
          if piece_type == "Z":
               s.color = "green"
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]
               s.queue_coordinates = [[0,0], [0,1], [1,1], [1,2]]  

     def reset_coordinates(self):
          s = self
          if s.piece_type == "I":
               s.coordinates = [[1,3], [1,4], [1,5], [1,6]]
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
