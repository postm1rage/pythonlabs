alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def alphabet_generator(n):
    n += 1
    for i in range(0, n - 1):
        yield alphabet[i]


print(*alphabet_generator(10))

n = 10
alphabet_gen = (alphabet[i] for i in range(n))
print(*alphabet_gen)
