# temperature.py
# Конвертація температур
print("КОНВЕРТЕР ТЕМПЕРАТУРИ")
print("=" * 35)
# Температура в градусах Цельсія
celsius = 25  # Початкове значення
# Конвертація в Фаренгейти
fahrenheit = celsius * 9 / 5 + 32  # Формула C → F
# Зворотна конвертація в Цельсії
celsius_back = (fahrenheit - 32) * 5 / 9  # Формула F → C
# Вивід результатів
print(f"{celsius} °C = {fahrenheit} °F")       # Пряма конвертація
print(f"{fahrenheit} °F = {celsius_back} °C")  # Зворотна конвертація
print("=" * 35)