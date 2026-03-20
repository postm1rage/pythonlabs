numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    25,
    49,
    543,
    2345,
    23,
    42,
    14,
    51,
    25,
    18,
    27,
    90,
    999,
    909,
    36,
    45,
    81,
]

result1 = list(filter(lambda x: x < 5, numbers))
print("1)", result1)

result2 = list(map(lambda x: x / 2, numbers))
print("2)", result2)

result3 = list(map(lambda x: x / 2, (list(filter(lambda x: x > 17, numbers)))))
print("3)", result3)

result4 = sum(list(map(lambda x: x * x, list(filter(lambda x: x % 9 == 0, numbers)))))
print("4)", result4)
