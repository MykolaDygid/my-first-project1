# Функція-валідатор перевіряє правильність даних.
# Вона часто повертає True або False.
# Великі задачі краще розбивати на кілька маленьких функцій,
# тому що код стає простішим для читання та тестування.


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_min_length(password):
    return len(password) >= 8


def validate_password(password):
    if password == "":
        return False, "Пароль порожній"

    if not has_min_length(password):
        return False, "Пароль занадто короткий"

    if not has_digit(password):
        return False, "Пароль не містить цифру"

    if not has_uppercase(password):
        return False, "Пароль не містить велику літеру"

    return True, "Пароль надійний"


password = input("Введіть пароль: ")

is_valid, message = validate_password(password)

if is_valid:
    print("Пароль надійний")
else:
    print("Пароль слабкий")
    print("Причина:", message)