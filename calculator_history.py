# Глобальна змінна доступна в усьому файлі.
# Локальна змінна існує лише всередині функції.
# Не варто зловживати глобальними змінними.
# Історію зручно зберігати у списку.
# Код з функціями легше читати та підтримувати.

history = []


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def add_to_history(record):
    history.append(record)


def show_history():
    if not history:
        print("Історія операцій порожня")
        return

    print("\nІсторія операцій:")
    for item in history:
        print(item)


while True:
    print("\nМеню")
    print("1 - Додати")
    print("2 - Відняти")
    print("3 - Помножити")
    print("4 - Поділити")
    print("5 - Показати історію")
    print("6 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "5":
        show_history()
        continue

    if choice == "6":
        print("Роботу завершено.")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Перше число: "))
        b = float(input("Друге число: "))

        if choice == "1":
            result = add(a, b)
            record = f"{a} + {b} = {result}"

        elif choice == "2":
            result = subtract(a, b)
            record = f"{a} - {b} = {result}"

        elif choice == "3":
            result = multiply(a, b)
            record = f"{a} * {b} = {result}"

        else:
            result = divide(a, b)

            if result is None:
                print("Помилка: ділення на нуль!")
                continue

            record = f"{a} / {b} = {result}"

        print("Результат:", result)
        add_to_history(record)

    else:
        print("Невірний вибір!")