def swap(first, second):
    first[:], second[:] = second[:], first[:]


first = [1, 2, 3]
second = [4, 5, 6]

first_content = first[:]
second_content = second[:]

swap(first, second)

print(first, second_content, first == second_content)  # [4, 5, 6] [4, 5, 6] True
print(second, first_content, second == first_content)  # [1, 2, 3] [1, 2, 3] True
