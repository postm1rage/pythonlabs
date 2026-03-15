def partial_sums(*args):
    return [sum(args[:i]) for i in range(len(args) + 1)]


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))
print(partial_sums())
print(partial_sums(5, 5, 5, 5, 5))
print(partial_sums(10, -5, 3, -1))
