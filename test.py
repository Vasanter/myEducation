print("Таблица умножения:")
print("-" * 155)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="    \t")
    print()  # переход на новую строку