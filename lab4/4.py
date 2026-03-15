import math


def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return math.sqrt(a**2 + b**2)


print(distance(0, 0, 3, 0))  
print(distance(1, 1, 1, 5)) 
print(distance(0, 0, 3, 4)) 