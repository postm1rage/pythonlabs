def same_by(characteristic, objects):
    if not objects:
        return True

    first_value = characteristic(objects[0])

    for obj in objects[1:]:
        if characteristic(obj) != first_value:
            return False

    return True


# true
values = list(range(0, 101, 2))  # 0 2 4 6 ... 100
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")

# false
values = list(range(1, 11))  # 0 1 2 3 ... 10
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")
