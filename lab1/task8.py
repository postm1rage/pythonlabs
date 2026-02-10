heights = []
while True:
    s = input()
    if s == "!":
        break
    s = int(s)
    if s in range(150, 191):
        heights.append(s)

print(len(heights))
print(*heights, sep = ', ')