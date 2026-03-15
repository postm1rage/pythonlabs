def bracket_check(string):
    stack = []
    pairs = {"(": ")", '"': '"'}

    for char in string:
        if char in pairs:
            if char == '"':
                if stack and stack[-1] == '"':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        elif char in pairs.values():
            if not stack:
                print("NO")
                return
            last = stack.pop()
            if pairs.get(last) != char:
                print("NO")
                return

    if not stack:
        print("YES")
    else:
        print("NO")


# Тесты
tests = [
    "",  # YES
    "()",  # YES
    '""',  # YES
    '("")',  # YES
    '(")(")',  # NO
    '"()"',  # YES
    '("()")',  # YES
    '(")',  # NO
    '((("")))',  # YES
    '("")("")',  # YES
]

for test in tests:
    print(f"{test} -> ", end="")
    bracket_check(test)
