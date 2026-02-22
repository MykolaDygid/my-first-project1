# currency.py
# Конвертер гривні в долари

uan = float(input("Ведіть суму в гривнях: "))
rade = float(input("Ведіть суму в доларах: "))

usd = uan / rade

print(f"{uan} грн = {usd: .2f} $")