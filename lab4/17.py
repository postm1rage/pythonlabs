def mirror(arr):
    arr.extend(arr[::-1]) # reverse() ничего не возвращает

my_list = [1, 2, 3]
mirror(my_list)
print(*my_list)
