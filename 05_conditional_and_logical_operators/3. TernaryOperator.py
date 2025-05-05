# Тернарный оператор в Python - это специальная конструкция, позволяющая записывать условное выражение в одну строку.
# Часто используется для выбора одного из двух значений.
# Не может содержать elif т.е. всегда состоит из основной конструкции if-else
# else также обязательно должно быть в отличие от не тернарного условного оператора.


# ПРИМЕР ПРЕОБРАЗОВАНИЯ 1:
a, b = 3, -1

if a > b:
    print(a)
else:
    print(b)

res = a if a > b else b  # переменной res присваиваем значение переменной a, если a > b; иначе присваиваем значение b
print(res)  # 3

# ... можно добавлять условия:
res = a + 2 if a > b else b - 4
print(res)  # 5

# ... использовать функции:
res = abs(a) if a < b else abs(b)
print(res)  # 1


# ПРИМЕР ПРЕОБРАЗОВАНИЯ 2:
# num = int(input("Enter a number: "))
# if num < 20:
#     number = num
# else:
#     number = 100
# print(number)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# вышеописанный код можно сократить следующим образом:
# num = int(input("Enter a number: "))
# number = num if num < 20 else 100
# print(number)


# Определение максимального значения:
# a = 12
# b = 7
# maximum = a if a > b else b
# print(maximum)  # 12

# Проверка чётности числа:
# a = int(input("Enter a number: "))
# result = "четное" if a % 2 == 0 else "нечетное"
# print(result)  # нечетное


# Преобразование строки в верхний регистр по условию:
# s = 'python'
# _type = 'upper'
# res = s.upper() if _type == 'upper' else s
# print(res)  # PYTHON
