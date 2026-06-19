# Перевірка голосної букви

letter = input("Введіть букву: ").lower()

vowels = "aeiouауоіеияю"

if letter in vowels:
    print("Це голосна буква")
else:
    print("Це не голосна буква")