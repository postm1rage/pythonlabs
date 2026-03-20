input = list(input().split(" "))

sorted = sorted(input, key=lambda x: x.lower())
print(*sorted)
