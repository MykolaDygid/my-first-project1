# Система знижок

price = float(input("Введіть суму покупки: "))
age = int(input("Введіть ваш вік: "))
student = input("Ви студент? (так/ні): ")
vip = input("VIP клієнт? (так/ні): ")
day = input("День тижня: ")
birthday = input("Сьогодні ваш день народження? (так/ні): ")

discount = 0

# 50%
if vip == "так":
    discount = 50
elif student == "так" and price > 500 and day in ["субота", "неділя"]:
    discount = 50

# 30%
elif student == "так" or age < 18 or age > 60:
    discount = 30

# 15%
elif day in ["субота", "неділя"]:
    discount = 15

# день народження
if birthday == "так":
    discount = discount * 2
    if discount > 70:
        discount = 70

final_price = price - (price * discount / 100)

print("Початкова ціна:", price)
print("Знижка:", discount, "%")
print("Фінальна ціна:", final_price)