# Тернарный оператор в Python - это специальная конструкция, позволяющая записывать условное выражение в одну строку.
# Он часто используется для выбора одного из двух значений в зависимости от условия, и является компактной альтернативой
# конструкции if-else.

# ПРИМЕР ПРЕОБРАЗОВАНИЯ:
# a = int(input("Enter a number: "))
# if a < 20:
#     number = a
# else:
#     number = 100
# print(number)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# вышеописанный код можно сократить следующим образом:
# a = int(input("Enter a number: "))
# number = a if a < 20 else 100
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
