list1 = [1, 3, 5, 7, 9]
list2 = [3, 4, 5, 6, 7]
print(sorted(set(list1) & set(list2), key=int))