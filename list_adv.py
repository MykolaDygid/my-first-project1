# Оцінки
grades = [78, 95, 62, 88, 70]

# Пошук індексу
index = grades.index(88)
print("Індекс оцінки 88:", index)

# Сортування за спаданням
grades.sort(reverse=True)
print("Відсортований список:", grades)


#Проблема копіювання
list1 = [1, 2, 3]
list2 = list1  # це не копія, а посилання

list2.append(4)

print("list1:", list1)
print("list2:", list2)

# Обидва списки змінилися, тому що вони посилаються на один і той самий об'єкт у пам'яті.


# ✅ Правильна копія
list3 = [5, 6, 7]
list4 = list3.copy()

list4.append(8)

print("list3:", list3)
print("list4:", list4)

# Тепер зміни торкаються тільки копії.