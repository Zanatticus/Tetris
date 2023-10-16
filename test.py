import math
columns = 6
rows = 7
a = [[0] * columns for i in range(rows)]
b = [[0] * columns for i in range(rows)]
c = [[0] * columns for i in range(rows)]
d = [[0] * columns for i in range(rows)]
e = [[0] * columns for i in range(rows)]

I_Piece = [[4, 2], [4, 3], [4, 4], [4, 5]] # None pivot
J_Piece = [[3, 2], [4, 2], [4, 3], [4, 4]] # 2 pivot
L_Piece = [[3, 4], [4, 2], [4, 3], [4, 4]] # 2 pivot
S_Piece = [[3, 3], [3, 4], [4, 2], [4, 3]] # 3 pivot
T_Piece = [[3, 2], [4, 1], [4, 2], [4, 3]] # 2 pivot
Z_Piece = [[3, 2], [3, 3], [4, 3], [4, 4]] # 2 pivot

def rotate_piece(piece, direction, pivot):
    rotated_piece = []
    pivot_row, pivot_col = piece[pivot]
    if direction == "clockwise":
        direction = 1
    elif direction == "counter-clockwise":
        direction = -1

    for [row, col] in piece:
        # Calculate the new coordinates after rotation around the pivot point
        new_row = pivot_row + (col - pivot_col) * direction
        new_col = pivot_col - (row - pivot_row) * direction
        rotated_piece.append([new_row, new_col])
    return rotated_piece

direction1 = "clockwise"
direction2 = "counter-clockwise"
direction = direction2
current_piece = Z_Piece
pivot = 2

for [row, col] in current_piece:
    a[row][col] = 1
rotated_piece = rotate_piece(current_piece, direction, pivot)
for [row, col] in rotated_piece:
    b[row][col] = 2
rotated_piece = rotate_piece(rotated_piece, direction, pivot)
for [row, col] in rotated_piece:
    c[row][col] = 3
rotated_piece = rotate_piece(rotated_piece, direction, pivot)
for [row, col] in rotated_piece:
    d[row][col] = 4
rotated_piece = rotate_piece(rotated_piece, direction, pivot)
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
