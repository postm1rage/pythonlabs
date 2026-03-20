correct_password = "12345"


def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль:\n")
        if password == correct_password:
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None

    return wrapper


@check_password
def iscorrect():
    return True


check_password(iscorrect())
