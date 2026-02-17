words = input().split()
indices = list(map(int, input().split()))

result = []
for index in indices:
    result.append(words[index - 1])

result[0] = result[0].capitalize()
print(' '.join(result))