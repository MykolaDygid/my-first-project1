cart = []

# Додаємо товари
cart.append("хліб")
cart.append("молоко")
cart.append("сир")

print("Після додавання:", cart)

# Вставка на позицію 1
cart.insert(1, "яйця")
print("Після вставки:", cart)

# Другий список
extra_items = ["масло", "цукор"]

# Об'єднання списків
cart.extend(extra_items)
print("Після об'єднання:", cart)

# append() додав би весь список як один елемент:
# cart.append(extra_items) → ["хліб", ..., ["масло", "цукор"]]
# extend() додає кожен елемент окремо.