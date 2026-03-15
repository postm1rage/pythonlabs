one = 5
two = 4
three = 0


def to_roman(num):
    roman_nums = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    result = ""
    for value, symbol in roman_nums.items():
        while num >= value:
            result += symbol
            num -= value
    return result


def roman():
    global three
    three = one + two
    print(f"{to_roman(one)} + {to_roman(two)} = {to_roman(three)}")


roman()
