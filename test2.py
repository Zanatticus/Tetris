import math
columns = 6
rows = 8
a = [[0] * columns for i in range(rows)]
b = [[0] * columns for i in range(rows)]
c = [[0] * columns for i in range(rows)]
d = [[0] * columns for i in range(rows)]
e = [[0] * columns for i in range(rows)]

I_Piece = [[4, 2], [4, 3], [4, 4], [4, 5]] # None pivot
J_Piece = [[3, 4], [4, 2], [4, 3], [4, 4]] # 2 pivot
L_Piece = [[3, 2], [4, 2], [4, 3], [4, 4]] # 3 pivot
S_Piece = [[3, 3], [3, 4], [4, 3], [4, 4]] # 4 pivot
T_Piece = [[3, 2], [4, 1], [4, 2], [4, 3]] # 3 pivot
Z_Piece = [[3, 2], [3, 3], [4, 3], [4, 4]] # 3 pivot


def rotate_piece(piece_coords, direction):
    # Calculate the center of the piece
    x_center = sum(x for x, y in piece_coords) / len(piece_coords)
    y_center = sum(y for x, y in piece_coords) / len(piece_coords)

    # Determine direction of rotation
    if direction == "clockwise":
        direction = 1
    if direction == "counter-clockwise":
        direction = -1
        
    # Rotate each block of the piece
    rotated_piece = []
    for x, y in piece_coords:
        # Translate block to origin
        x -= x_center
        y -= y_center
        
        # Rotate block
        x_new = y * (direction)
        y_new = -x * (direction)

        # Translate block back to center
        x_new += x_center
        y_new += y_center
        
        # Append block to rotated piece
        rotated_piece.append((round(x_new), round(y_new)))
    return rotated_piece

def rotate_long_piece(piece_coords, direction, position):
    # Calculate the center of the piece
    x_center = math.ceil(sum(x for x, y in piece_coords) / len(piece_coords))
    y_center = math.ceil(sum(y for x, y in piece_coords) / len(piece_coords))
    
    # Determine direction of rotation
    if direction == "clockwise":
        direction = 1
    else:
        direction = -1
        
    # Rotate each block of the piece
    rotated_piece = []
    for x, y in piece_coords:
        # Translate block to origin
        x -= x_center
        y -= y_center

        # Rotate block
        x_new = y * (direction)
        y_new = -x * (direction)
        
        # Translate block back to center
        x_new += x_center
        y_new += y_center
        
        # Append block to rotated piece
        if direction == "clockwise":
            if position == 0: # Flat top
                rotated_piece.append((x_new + 1, y_new))
            if position == 1: # Right upright
                rotated_piece.append((x_new, y_new - 1))
            if position == 2 : # Flat bottom
                rotated_piece.append((x_new, y_new - 1))
            if position == 3: # Left upright
                rotated_piece.append((x_new - 1, y_new))
        else:
            if position == 0: # Flat top
                rotated_piece.append((x_new, y_new - 1))
            if position == 1: # Right upright
                rotated_piece.append((x_new, y_new + 1))
            if position == 2 : # Flat bottom
                rotated_piece.append((x_new - 1, y_new))
            if position == 3: # Left upright
                rotated_piece.append((x_new - 1, y_new))
            
        # if position == 0: # Flat top
        #     rotated_piece.append((math.floor(x_new) + 1, math.ceil(y_new)))
        # if position == 1: # Right upright
        #     rotated_piece.append((math.ceil(x_new), math.floor(y_new)))
        # if position == 2 : # Flat bottom
        #     rotated_piece.append((math.floor(x_new), math.floor(y_new)))
        # if position == 3: # Left upright
        #     rotated_piece.append((math.floor(x_new), math.ceil(y_new)))
    return rotated_piece


direction1 = "clockwise"
direction2 = "counter-clockwise"
current_piece = L_Piece

for [row, col] in current_piece:
    a[row][col] = 1
rotated_piece = rotate_piece(current_piece, direction1)
for [row, col] in rotated_piece:
    b[row][col] = 2
rotated_piece = rotate_piece(rotated_piece, direction1)
for [row, col] in rotated_piece:
    c[row][col] = 3
rotated_piece = rotate_piece(rotated_piece, direction1)
for [row, col] in rotated_piece:
    d[row][col] = 4
rotated_piece = rotate_piece(rotated_piece, direction1)
for [row, col] in rotated_piece:
    e[row][col] = 5

for row in a:
    print(row)    
print()
for row in b:
    print(row)
print()
for row in c:
    print(row)    
print()
for row in d:
    print(row)
print()
for row in e:
    print(row)
print()   
