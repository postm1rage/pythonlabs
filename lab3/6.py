n = int(input())
surnames = {}

for _ in range(n):
    name = input().strip()
    surnames[name] = surnames.get(name, 0) + 1

count = 0
for v in surnames.values():
    if v > 1:
        count += v

print(count)