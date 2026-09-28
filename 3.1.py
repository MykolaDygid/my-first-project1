import numpy as np

# Створюємо оцінки та рахуємо середнє в один рядок для кожного з 100 студентів
grades = np.random.randint(0, 101, size=(100, 3))
averages = grades.mean(axis=1)

# Виводимо результати
for i, (student_grades, avg) in enumerate(zip(grades, averages), 1):
    print(f"Студент {i:02d}: {student_grades} -> Середній бал: {avg:.2f}")
