input = list(map(int, (input().split(" "))))

sorted = sorted(input, key=lambda x: abs(x))
print(*sorted)