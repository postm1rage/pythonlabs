my_list = [3, 1, 4, 1, 5, 9]
print("было:", my_list)

# sort() меняет сам список
my_list.sort()
print("после sort():", my_list)  # список изменился

print("-" * 30)

# sorted() создает новый список
other_list = [3, 1, 4, 1, 5, 9]
print("было:", other_list)

new_list = sorted(other_list)
print("после sorted():", other_list)  # остался как был
print("новый список:", new_list)       # а это новый