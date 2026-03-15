numbers = [int(x) for x in input().split()]
print(*['*' * n for n in numbers], sep='\n')