class Piece:
     def __init__(self, piece_type):
          s = self
          #s.piece_list = ["I", "J", "L", "O", "S", "T", "Z"]
          #s.piece_colors = {"I":"cyan", "J":"pink", "L":"orange", "O":"yellow", "S":"red", "T":"magenta", "Z":"green"}
          if piece_type == "I":
               s.color = "cyan"
               s.coordinates = [[0,3], [0,4], [0,5], [0,6]]
               
          if piece_type == "J":
               s.color = "pink"
               s.coordinates = [[0,3], [1,3], [1,4], [1,5]]
               
          if piece_type == "L":
               s.color = "orange"
               s.coordinates = [[0,5], [1,3], [1,4], [1,5]]
               
          if piece_type == "O":
               s.color = "yellow"
               s.coordinates = [[0,4], [0,5], [1,4], [1,5]]
               
          if piece_type == "S":
               s.color = "red"
               s.coordinates = [[0,4], [0,5], [1,3], [1,4]]
               
          if piece_type == "T":
               s.color = "magenta"
               s.coordinates = [[0,4], [1,3], [1,4], [1,5]]
               
          if piece_type == "Z":
               s.color = "green"
               s.coordinates = [[0,3], [0,4], [1,4], [1,5]]
               

     