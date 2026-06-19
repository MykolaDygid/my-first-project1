# return повертає значення з функції.
# print лише виводить інформацію на екран.
# Для різних дій краще створювати окремі функції,
# тому що код стає зрозумілішим і легше підтримується.

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

choice = input("Оберіть дію: ")

if choice == "1":
    celsius = float(input("Введіть температуру у °C: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {result:.2f}°F")

elif choice == "2":
    fahrenheit = float(input("Введіть температуру у °F: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {result:.2f}°C")

else:
    print("Помилка: неправильний вибір операції.")