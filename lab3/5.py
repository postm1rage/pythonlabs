n = int(input())
words = set()

for i in range(n):
    line = input().split()
    for word in line:
        words.add(word)

print(len(words))