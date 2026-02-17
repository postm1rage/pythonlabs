path = input()
draw_char = path[0]
moves = path[1:]

grid = [[' ' for _ in range(100)] for _ in range(100)]
row, col = 0, 0
grid[row][col] = draw_char

min_row, max_row = 0, 0
min_col, max_col = 0, 0

for move in moves:
    if move == '<':
        col -= 1
    elif move == '>':
        col += 1
    elif move == 'V':
        row += 1
    
    grid[row][col] = draw_char
    min_row = min(min_row, row)
    max_row = max(max_row, row)
    min_col = min(min_col, col)
    max_col = max(max_col, col)

for r in range(min_row, max_row + 1):
    line = ''.join(grid[r][c] for c in range(min_col, max_col + 1))
    print(line)