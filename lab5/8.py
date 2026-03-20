def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            row.append(str(operation(i, j)))
        print("\t".join(row))


print("таблица 9x9:")
print_operation_table(lambda x, y: x * y)

print("\nтаблица 5x9:")
print_operation_table(lambda x, y: x * y, 5)
