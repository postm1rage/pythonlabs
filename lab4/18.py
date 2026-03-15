def from_string_to_list(string, container):
    container.extend([int(x) for x in string.split()])


my_list = [1, 2, 3]
from_string_to_list("4 5 6", my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6]

from_string_to_list("10 20 30", my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6, 10, 20, 30]
