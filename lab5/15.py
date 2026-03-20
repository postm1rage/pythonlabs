import sys
from functools import reduce

print(reduce(lambda a, b: a if a < b else b, [line.strip() for line in sys.stdin]))
