while True:
    password = input()
    confirm = input()
    
    if len(password) < 8:
        print("Короткий!")
        continue
    
    if "123" in password:
        print("Простой!")
        continue
    
    if password != confirm:
        print("Различаются.")
        continue 
    
    print("OK")
    break