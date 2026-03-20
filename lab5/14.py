import sys

text = sys.stdin.read()
words = text.split()

first = {}
result = []

for i, w in enumerate(words):
    if w and w[0].isupper():
        if w not in first:
            first[w] = i
        result.append((first[w], w))

result.sort(key=lambda x: x[1])

for idx, word in result:
    print(f"{idx} - {word}")