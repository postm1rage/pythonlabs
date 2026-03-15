def tic_tac_toe(field):
    lines = []

    # строки
    for row in field:
        lines.append("".join(row))

    # столбцы
    for col in range(3):
        lines.append(field[0][col] + field[1][col] + field[2][col])

    # диагонали
    lines.append(field[0][0] + field[1][1] + field[2][2])
    lines.append(field[0][2] + field[1][1] + field[2][0])

    if "xxx" in lines:
        print("x win")
    elif "000" in lines:
        print("0 win")
    else:
        print("draw")


field = [["x", "x", "x"], ["0", "x", "0"], ["-", "0", "-"]]
tic_tac_toe(field)  # x win
print()

field = [["0", "x", "x"], ["0", "x", "-"], ["0", "-", "x"]]
tic_tac_toe(field)  # 0 win
print()

field = [["x", "0", "0"], ["x", "0", "x"], ["0", "x", "x"]]
tic_tac_toe(field)  # 0 win
print()
