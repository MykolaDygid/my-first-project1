# advanced_calc.py
# Завдання із зірочкою
print("ADVANCED CALCULATIONS")
print("=" * 40)
# Корені чисел
sqrt_144 = 144 ** 0.5  # Квадратний корінь
cbrt_27 = 27 ** (1/3)  # Кубічний корінь
print("144 =", sqrt_144)   # Вивід квадратного кореня
print("27 =", cbrt_27)     # Вивід кубічного кореня
print("-" * 40)
# Діагональ прямокутника
width = 12   # Ширина
height = 5   # Висота
diagonal = (width**2 + height**2) ** 0.5  # Теорема Піфагора
print("Діагональ прямокутника:", diagonal)
print("-" * 40)
# Калькулятор знижок
price1 = 120  # Ціна першого товару
price2 = 80   # Ціна другого товару
price3 = 100  # Ціна третього товару
total_price = price1 + price2 + price3  # Загальна сума
discount = 0.25                          # Знижка 25%
discount_amount = total_price * discount  # Сума економії
final_price = total_price - discount_amount  # Фінальна ціна
print("Загальна сума:", total_price)
print("Економія:", discount_amount)
print("До сплати:", final_price)
print("=" * 40)