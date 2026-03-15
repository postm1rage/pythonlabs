def defratalize(fractal):
    fractal[:] = [x for x in fractal if x is not fractal]


fractal = [2, 5]
fractal.append(fractal)
print(fractal)

fractal.append(3)
fractal.append(fractal)
fractal.append(9)

defratalize(fractal)
print(fractal)
