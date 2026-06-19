# Callback-функція — це функція, яку передають як аргумент іншій функції.
# Передача функції без дужок означає передачу самої функції.
# Якщо написати дужки (), функція виконається відразу.
# Callback робить код більш гнучким.

grades = []


def add_grade():
    try:
        grade = int(input("Введіть оцінку (1-12): "))

        if 1 <= grade <= 12:
            grades.append(grade)
            print("Оцінку додано.")
        else:
            print("Оцінка повинна бути від 1 до 12.")

    except ValueError:
        print("Потрібно ввести число.")


def show_grades(data):
    print("Оцінки:", data)


def average_grade(data):
    print("Середній бал:", round(sum(data) / len(data), 2))


def highest_grade(data):
    print("Найвища оцінка:", max(data))


def lowest_grade(data):
    print("Найнижча оцінка:", min(data))


def count_grades(data):
    print("Кількість оцінок:", len(data))


def process_grades(data, callback):
    callback(data)


while True:
    print("\nМеню")
    print("1 - Додати оцінку")
    print("2 - Показати всі оцінки")
    print("3 - Показати середній бал")
    print("4 - Показати найвищу оцінку")
    print("5 - Показати найнижчу оцінку")
    print("6 - Показати кількість оцінок")
    print("7 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_grade()

    elif choice == "2":
        if grades:
            process_grades(grades, show_grades)
        else:
            print("Список оцінок порожній.")

    elif choice == "3":
        if grades:
            process_grades(grades, average_grade)
        else:
            print("Список оцінок порожній.")

    elif choice == "4":
        if grades:
            process_grades(grades, highest_grade)
        else:
            print("Список оцінок порожній.")

    elif choice == "5":
        if grades:
            process_grades(grades, lowest_grade)
        else:
            print("Список оцінок порожній.")

    elif choice == "6":
        if grades:
            process_grades(grades, count_grades)
        else:
            print("Список оцінок порожній.")

    elif choice == "7":
        print("Роботу завершено.")
        break

    else:
        print("Невірний вибір.")