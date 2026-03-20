def square_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a**2
        a, b = b, a + b


print(*square_fibonacci(7))
