#секретне число
secret_number = 7

# Нескінченний цикл
while True:
    # Отримуємо число від користувача
    guess = int(input("Вгадай число від 1 до 10: "))
    
    # Перевірка
    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        
        # break — зупиняє цикл
        break
    else:
        print("Спробуй ще раз!")