# Безпечний калькулятор з обробкою винятків.
# Блок try використовується для коду, в якому може виникнути помилка.
# Блок except перехоплює винятки та не дозволяє програмі аварійно завершитися.
# ValueError виникає, коли користувач вводить текст замість числа.
# ZeroDivisionError виникає при спробі поділити число на 0.
# Блок else виконується, якщо в блоці try не виникло жодної помилки.
# Блок finally виконується завжди, незалежно від того, була помилка чи ні.
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Помилка: невідома математична операція.")
except ValueError:
    print("Помилка: потрібно вводити тільки числа.")
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")
else:
    if operation in ["+", "-", "*", "/"]:
        print(f"Результат: {result}")
        print("Операція виконана успішно.")
finally:
    print("Роботу калькулятора завершено.")