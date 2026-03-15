my_list = [1, 2, 3, 4, 5, 6, 25, 38, 41, 7, 8, 9, 10, 90]

# 1, 2, 3
result1 = [x for x in my_list if x < 5]
result2 = [x / 2 for x in my_list]
result3 = [x * 2 for x in my_list if x > 17]

print("1) ", result1)
print("2) ", result2)
print("3) ", result3)

# 4
n = int(input("4) введите число: "))
result4 = [x**2 for x in range(n + 1)]
print(result4)

# 5
print("5) введите числа:")
numbers = [int(x) for x in input().split()]
squares = [x**2 for x in numbers]
print("квадраты:", *squares)

# 6
print("6) Введите числа через пробел:")
print(*[x for x in [int(i) for i in input().split()] if x % 2 != 0 and x % 10 != 9])

"""
то же самое, что и
input_string = input()
string_list = input_string.split()
numbers = [int(i) for i in string_list]

result = []
for x in numbers:
    if x % 2 != 0:
        square = x**2
        if square % 10 != 9:
            result.append(square)
"""
