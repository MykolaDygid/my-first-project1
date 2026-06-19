items = ["яблуко", "банан", "груша", "банан", "ківі"]

# Видалення за значенням
items.remove("банан")
print("Після remove:", items)

# Видалення останнього елемента
last_item = items.pop()
print("Видалено елемент:", last_item)
print("Список зараз:", items)

# Видалення першого елемента
del items[0]
print("Після del:", items)

# Очищення списку
items.clear()
print("Після clear:", items)