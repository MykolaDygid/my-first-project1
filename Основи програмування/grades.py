# grades.py
# Система оцінювання

score = int(input("Введіть кількість балів (0-100): "))

if 90 <= score <= 100:
    print("Оцінка: Відмінно")
elif 75 <= score <= 89:
    print("Оцінка: Добре")
elif 60 <= score <= 74:
    print("Оцінка: Задовільно")
elif 0 <= score < 60:
    print("Оцінка: Незадовільно")
else:
    print("Некоректне значення!")