import random
import string
# Модуль random використовується для генерації псевдовипадкових чисел.
# Вони не є абсолютно випадковими, оскільки створюються математичним алгоритмом.
# random.randint(a, b) повертає випадкове число в заданому діапазоні.
# random.choice(sequence) повертає випадковий елемент із послідовності.
# Генератор паролів
length = random.randint(8, 12)
symbols = string.ascii_letters + string.digits + "!@#$%"
password = "".join(random.choice(symbols) for _ in range(length))
print(f"Згенерований пароль: {password}")
# Гра "Вгадай число"
secret_number = random.randint(1, 100)
attempts = 0
print("\nГра 'Вгадай число'")
print("Я загадав число від 1 до 100.")
while True:
    guess = int(input("Ваш варіант: "))
    attempts += 1
    if guess < secret_number:
        print("Більше")
    elif guess > secret_number:
        print("Менше")
    else:
        print(f"Вітаю! Ви вгадали число за {attempts} спроби.")
        break