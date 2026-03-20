def arithmetic_operation(operation):
    if operation == "+":
        return lambda x, y: x + y
    elif operation == "-":
        return lambda x, y: x - y
    elif operation == "*":
        return lambda x, y: x * y
    elif operation == "/":
        return lambda x, y: x / y


operations = "+-*/"
for op in operations:
    operation = arithmetic_operation(op)
    print(operation(70, 7))
