# leap_year.py
# Перевірка високосного року

year = int(input("Ведіть рік: "))

if (year % 2 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - Висококосний рік.")
else:
    print(f"{year} - Не висококосний рік.")