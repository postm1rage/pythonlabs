def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)


fib = [1, 1]
continue_fibonacci_sequence(fib, 22000)
print(fib)  # [1, 1, 2, 3, 5, 8, 13]
