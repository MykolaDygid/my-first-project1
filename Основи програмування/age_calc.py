# age_calc.py
# Калькулятор віку в місяцях та днях

name = input("Введіть ваше ім'я: ")
years = int(input("Скільки вам років: "))

months = years * 12
days = years * 365

print("\n=== Картка користувача ===")
print(f"Ім'я: {name}")
print(f"Вік у роках: {years}")
print(f"Вік у місяцях: {months}")
print(f"Вік у днях: {days}")
print("==========================")