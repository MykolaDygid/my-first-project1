from datetime import datetime, date
# Звичайний формат дати (15.06.2026) не завжди є зручним для користувача.
# Локалізація дозволяє відображати дату зрозумілою мовою.
# timedelta — це об'єкт, який представляє різницю між двома датами або часом.
# Використовується для обчислення кількості днів, годин, хвилин між подіями.
months = {
    1: "січня",
    2: "лютого",
    3: "березня",
    4: "квітня",
    5: "травня",
    6: "червня",
    7: "липня",
    8: "серпня",
    9: "вересня",
    10: "жовтня",
    11: "листопада",
    12: "грудня"
}
now = datetime.now()
print(
    f"Сьогодні: {now.day} {months[now.month]} {now.year} року"
)
print(f"Поточний час: {now.strftime('%H:%M')}")
# Різниця дат
user_date = input(
    "\nВведіть дату народження або події (ДД.ММ.РРРР): "
)
event_date = datetime.strptime(user_date, "%d.%m.%Y").date()
today = date.today()
difference = event_date - today
if difference.days > 0:
    print(f"До події залишилося {difference.days} днів.")
elif difference.days < 0:
    print(f"Від події минуло {abs(difference.days)} днів.")
else:
    print("Подія відбувається сьогодні!")