s = input()
n = len(s)

k = (n + 1) // 2

result = s[k:] + s[:k]
print(result)