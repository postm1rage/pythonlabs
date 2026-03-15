def transpose(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose(matrix)

for line in matrix:
    print(*line)
