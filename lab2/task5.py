prev = input()
while True:
    current = input()
    if current[0].lower() != prev[-1].lower():
        print(current)
        break
    prev = current