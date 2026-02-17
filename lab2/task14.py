coords = []
for _ in range(8):
    x, y = map(int, input().split())
    coords.append((x, y))

result = "NO"

for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            result = "YES"
            break
    if result == "YES":
        break

print(result)