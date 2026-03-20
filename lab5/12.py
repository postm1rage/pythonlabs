def distance(x, y):
    return (x * x + y * y) ** 0.5


coords_list = [[3, 4], [2, 25], [3, 2], [0, 6], [5, 5], [4, 3], [0, 0], [-3, -5]]


sorted_coords = sorted(
    coords_list, key=lambda point: (distance(point[0], point[1]), point[0], point[1])
)

for coord in sorted_coords:
    print(coord)
