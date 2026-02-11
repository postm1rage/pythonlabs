n = int(input())
a, b, c, d = n // 1000, n // 100 % 10, n // 10 % 10, n % 10

if a > b: a, b = b, a
if c > d: c, d = d, c
if a > c: a, c = c, a
if b > d: b, d = d, b
if b > c: b, c = c, b

if a != 0:
    res = a * 1000 + b * 100 + c * 10 + d
elif b != 0:
    res = b * 1000 + a * 100 + c * 10 + d
elif c != 0:
    res = c * 1000 + a * 100 + b * 10 + d
else:
    res = d * 1000 + a * 100 + b * 10 + c

print(res)