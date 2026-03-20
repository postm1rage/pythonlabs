import time


def check_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Введите пароль:")
            user_password = input()
            if user_password == correct_password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None

        return wrapper

    return decorator


@check_password("12345")
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    time.sleep(1)
    print(f"Готовим бургер с {typeOfMeat}")
    time.sleep(1)
    if withOnion:
        print("Добавляем лук")
        time.sleep(1)
    if withTomato:
        print("Добавляем помидор")
        time.sleep(1)
    print("Готово!")


make_burger("говядиной", True)
