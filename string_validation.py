# --- Робота з email ---
email = "user@example.com"

print("Аналіз email:")

# Позиція символа @
print("Позиція @:", email.find("@"))

# Кількість літер 'e'
print("Кількість 'e':", email.count("e"))

# Перевірки
print("Починається з 'user':", email.startswith("user"))
print("Закінчується на '.com':", email.endswith(".com"))


# --- Перевірка типу рядка ---
user_input = input("\nВведіть будь-який рядок: ")

if user_input.isdigit():
    print("Це число")
elif user_input.isalpha():
    print("Це слово")
elif user_input.isalnum():
    print("Буквено-цифрова комбінація")
else:
    print("Змішаний вміст (символи/пробіли)")