n = int(input())

current = 1
row_length = 1

while current <= n:
    for i in range(row_length):
        if current <= n:
            print(current, end=' ')
            current += 1
    print()
    row_length += 1