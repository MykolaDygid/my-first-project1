rows = 5
print("Звичайна піраміда:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\nЦентрована піраміда:")
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # пробіли зліва
    for j in range(1, i + 1):
        print(j, end=" ")
    print()