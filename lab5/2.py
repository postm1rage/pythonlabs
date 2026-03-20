def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact


for n in range(10):
    print(*factorials(n))