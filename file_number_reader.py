# FileNotFoundError виникає, якщо файл не існує,
# був видалений або вказано неправильний шлях.
# Дані з текстового файлу читаються як рядок (str),
# тому їх потрібно перетворювати на число.
# Конструкція with open() автоматично закриває файл
# після завершення роботи з ним.
try:
    with open("number.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()
    number = float(content)
    print(f"Число з файлу: {number}")
    print(f"Число * 2 = {number * 2}")
    print(f"100 / число = {100 / number}")
except FileNotFoundError:
    print("Помилка: файл number.txt не знайдено.")
except ValueError:
    print("Помилка: у файлі має бути записане число.")
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")
finally:
    print("Роботу з файлом завершено.")