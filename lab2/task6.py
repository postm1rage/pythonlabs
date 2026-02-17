s = input()
answer = ''
current = 1
for letter in s:
    answer = answer + letter * current
    current += 1

print(answer)