# Перевірка надійності пароля

password = input("Введіть пароль: ")

length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if length and has_digit and has_upper:
    print("Пароль безпечний")
else:
    print("Пароль слабкий")
    print("Умови: мінімум 8 символів, велика літера та цифра")