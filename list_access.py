# Індекс списку — це порядковий номер елемента.
# У Python індексація починається з 0.
# IndexError виникає, якщо звернутися до індексу,
# якого немає в списку.
# Конструкція try-except дозволяє програмі продовжити
# роботу та показати зрозуміле повідомлення про помилку.
students = ["Анна", "Максим", "Олег", "Ірина", "Софія"]
print("Список студентів:")
for index, student in enumerate(students):
    print(f"{index}: {student}")
try:
    user_index = int(input("Введіть індекс студента: "))
    selected_student = students[user_index]
except ValueError:
    print("Помилка: індекс має бути числом.")
except IndexError:
    print("Помилка: студента з таким індексом немає.")
else:
    print(f"Обраний студент: {selected_student}")
    print("Пошук виконано успішно.")
finally:
    print("Перевірку списку завершено.")
