def ask_password(login, password, success, failure):
    login, password = login.lower(), password.lower()
    vowels = set("aeiouy")

    vowels_count = sum(1 for ch in password if ch in vowels)

    login_cons = [ch for ch in login if ch not in vowels]
    pass_cons = [ch for ch in password if ch not in vowels]

    if vowels_count == 3 and login_cons == pass_cons:
        success(login)
    else:
        if vowels_count != 3 and login_cons != pass_cons:
            error = "Everything is wrong"
        elif vowels_count != 3:
            error = "Wrong number of vowels"
        else:
            error = "Wrong consonants"
        failure(login, error)


def main(login, password):
    ask_password(
        login,
        password,
        lambda l: print(f"Привет, {l}!"),
        lambda l, e: print(
            f"Кто-то пытался притвориться пользователем {l}, но в пароле допустил ошибку: {e.upper()}."
        ),
    )
