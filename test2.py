
a = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]
b = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]

def rotate_right(piece, pivot, position):
    rotated_piece = []
    pivot_row, pivot_col = pivot
    if position == 0:
        row_modifier = -1
        column_modifier = 2
        for [row, col] in piece:
            [new_row, new_col] = [row + row_modifier, col + column_modifier]
            row_modifier + 1
            column_modifier - 1
    if position == 1:
        row_modifier = 2
        column_modifier = 1
        for [row, col] in piece:
            [new_row, new_col] = [row + row_modifier, col + column_modifier]
            row_modifier + 1
            column_modifier - 1
    if position == 2:
        row_modifier = -2
        column_modifier = 1
        for [row, col] in piece:
            [new_row, new_col] = [row + row_modifier, col + column_modifier]
            row_modifier + 1
            column_modifier - 1
    if position == 3:
        row_modifier = -1
        column_modifier = 2
        for [row, col] in piece:
            [new_row, new_col] = [row + row_modifier, col + column_modifier]
            row_modifier + 1
            column_modifier - 1
        
    
    for [row, col] in piece:
        [new_row, new_col] = [row + row_modifier, col + column_modifier]
        row_modifier + 1
        column_modifier - 1
    
    
    
    
    for [row, col] in piece:
        # Calculate the new coordinates after rotation around the pivot point
        new_row = pivot_row + (col - pivot_col)
        new_col = pivot_col - (row - pivot_row)
        rotated_piece.append([new_row, new_col])
    return rotated_piece

def rotate_left(piece, pivot):
    rotated_piece = []
    pivot_row, pivot_col = pivot

    for [row, col] in piece:
        # Calculate the new coordinates after rotation around the pivot point
        new_row = pivot_row - (col - pivot_col)
        new_col = pivot_col + (row - pivot_row)
        rotated_piece.append([new_row, new_col])
    return rotated_piece

# Specify the pivot point for rotation
pivot_point1 = [4, 4]
pivot_point2 = [5, 2]
T_Piece = [[3, 4], [4, 3], [4, 4], [4, 5]]
I_Piece = [[6, 0], [6, 1], [6, 2], [6, 3]]
# Rotate the Tetris piece around the pivot point
rotated_T = rotate_right(rotate_right(T_Piece, pivot_point1), pivot_point1)
#rotated_I = rotate_right(I_Piece, pivot_point2)
rotated_T2 = rotate_left(T_Piece, pivot_point1)

    
for square in rotated_T2:
    b[square[0]][square[1]] = 2


for row in a:
    print(row)    
print()
for row in b:
    print(row)