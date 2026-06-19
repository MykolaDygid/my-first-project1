# Отримуємо текст від користувача
text = input("Введіть речення: ")

# --- Методи регістру ---
print("\nРезультати зміни регістру:")
print("UPPER:", text.upper())          # Усі літери великі
print("lower:", text.lower())          # Усі літери маленькі
print("Capitalize:", text.capitalize())  # Перша літера велика
print("Title:", text.title())          # Кожне слово з великої

# --- Очищення пробілів ---
clean_text = text.strip()  # Видаляє пробіли з початку і кінця

print("\nОчищення тексту:")
print("До очищення довжина:", len(text))
print("Після очищення довжина:", len(clean_text))

# --- Заміна слів ---
spam_text = "Це spam повідомлення про spam"

# Замінюємо слово spam на ***
censored = spam_text.replace("spam", "***")

print("\nЦензура:")
print("Було:", spam_text)
print("Стало:", censored)