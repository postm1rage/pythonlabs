def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None

    if len(coefficients) == 1:
        a, b, c = 0, 0, coefficients[0]
    elif len(coefficients) == 2:
        a, b, c = 0, coefficients[0], coefficients[1]
    else:
        a, b, c = coefficients

    if a == 0 and b == 0 and c == 0:
        return ["all"]
    if a == 0 and b == 0:
        return []
    if a == 0:
        return [-c / b]

    d = b**2 - 4 * a * c
    if d < 0:
        return []
    if d == 0:
        return [-b / (2 * a)]

    sqrt_d = d**0.5
    return [(-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a)]


print(sorted(solve(1, 2, 1)))
print(sorted(solve(1, -3, 2)))
print(solve(0, 2, 1))
print(solve(0, 0, 5))
print(solve(0, 0, 0))
print(solve(1, 2, 5))
print(solve())
print(solve(1, 2, 3, 4))
