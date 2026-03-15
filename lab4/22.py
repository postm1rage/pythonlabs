def fractal_print(obj):
    print("[", end="")

    for i, item in enumerate(obj):
        if item is obj:
            print("[", end="")
            for j, sub in enumerate(obj):
                if sub is obj:
                    print("[...]", end="")
                else:
                    print(repr(sub), end="")
                if j < len(obj) - 1:
                    print(", ", end="")
            print("]", end="")
        else:
            print(repr(item), end="")

        if i < len(obj) - 1:
            print(", ", end="")

    print("]")


fractal_print([1, "два", 3])  # [1, 'два', 3]

f = [3]
f.append(f)
fractal_print(f)  # [3, [3, [...]]]

f = [1, "x"]
f.append(f)
f.append(5)
fractal_print(f)  # [1, 'x', [1, 'x', [...], 5], 5]
