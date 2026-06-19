# Словник товарів і цін
prices = {
    "Хліб": 35,
    "Молоко": 50,
    "Сир": 180,
    "Яблука": 45,
    "Шоколад": 60
}
print("Товари та ціни:")
for product, price in prices.items():
    print(f"{product}: {price} грн")
# Додавання нового товару
prices["Сік"] = 55
# Зміна ціни товару
prices["Молоко"] = 52
# Видалення товару
del prices["Яблука"]
# Пошук товару
product_name = input("\nВведіть назву товару: ")
if product_name in prices:
    print(f"Ціна товару {product_name}: {prices[product_name]} грн")
else:
    print("Товар не знайдено")
# Пошук найдорожчого товару
most_expensive = max(prices, key=prices.get)
print("\nНайдорожчий товар:")
print(f"{most_expensive} - {prices[most_expensive]} грн")
# Перевірка наявності ключа виконується оператором in.
# Наприклад:
# if product_name in prices:
# Це означає: перевірити, чи існує такий ключ у словнику.