import pandas as pd, numpy as np

# 1-2. Генеруємо дані відразу в таблицю та рахуємо середній бал
df = pd.DataFrame({
    'Ім’я': [f"Студент {i+1}" for i in range(100)], 'Вік': np.random.randint(17, 23, 100),
    'Оцінка з математики': np.random.randint(0, 101, 100), 'Оцінка з програмування': np.random.randint(0, 101, 100)
})
df['Середній бал'] = df[['Оцінка з математики', 'Оцінка з програмування']].mean(axis=1)

# 3-6. Додаємо статус, виводимо статистику та зберігаємо у CSV
df['Status'] = np.where(df['Середній бал'] >= 75, 'Здали', 'Не здали')

print(f"Бал > 80: {len(df[df['Середній бал'] > 80])}\n{df['Status'].value_counts()}")
df.to_csv('students_results.csv', index=False, encoding='utf-8-sig')
