login = input()
mail = input()

if "@" in login:
    print("Invalid login")
if "@" not in mail:
    print("Invalid mail")
