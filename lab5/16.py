from math import gcd
from functools import reduce
import sys

print(reduce(gcd, map(int, sys.stdin.read().split())))
