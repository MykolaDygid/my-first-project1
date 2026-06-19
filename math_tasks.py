import math
# Для точних математичних обчислень краще використовувати модуль math,
# оскільки його константи та функції мають значно більшу точність,
# ніж самостійно задані наближені значення (наприклад pi = 3.14).
# Функції math.sin() та math.cos() приймають аргументи у радіанах,
# тому градуси потрібно переводити через math.radians().
# Коло
radius = float(input("Введіть радіус кола: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Площа кола: {round(area, 2)}")
print(f"Довжина кола: {round(circumference, 2)}")
# Тригонометрія
angle_deg = float(input("\nВведіть кут у градусах: "))
angle_rad = math.radians(angle_deg)
print(f"Синус: {round(math.sin(angle_rad), 4)}")
print(f"Косинус: {round(math.cos(angle_rad), 4)}")
# Корінь і факторіал
number = int(input("\nВведіть ціле число: "))
if number >= 0:
    print(f"Квадратний корінь: {math.sqrt(number)}")
    print(f"Факторіал: {math.factorial(number)}")
else:
    print("Для від'ємних чисел факторіал і квадратний корінь не обчислюються.")