numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(odd)
print(even)

# ошибка была в том, что odd = even = [] создаёт один массив,
# а нам надо два, для четных и нечетных чисел
