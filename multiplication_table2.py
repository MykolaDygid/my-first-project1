# Таблиця множення для введеного числа
num = int(input("Введіть число: "))
print(f"\nТаблиця множення для {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
print("\nПіфагорова таблиця:")
# Повна таблиця множення 1–10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")  # форматування для рівних колонок
    print()  # перехід на новий рядок