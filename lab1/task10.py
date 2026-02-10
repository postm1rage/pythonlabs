def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    num1 = int(input())
    operation = input()

    if operation == "x":
        print(num1)
        break

    if operation == '!':
        if num1 >= 0:
            result = factorial(num1)
            print(result)
        continue

    num2 = int(input())

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print(num1 // num2)
    elif operation == '%':
        if num2 != 0:
            print(num1 % num2)