import math

# В программировании числа классифицируются прежде всего на целые (integer, тип int в Python) и вещественные -
# (тип float) с плавающей запятой.
# Целые числа (int) в Python представляются без десятичной точки. Они могут быть положительными или отрицательными.
# В Python нет ограничений на длину целых чисел, то есть целые числа могут быть очень большими.

# Вещественные числа поддерживают те же операции, что и целые.
# Однако (из-за представления чисел в компьютере) вещественные числа неточны, и это может привести к ошибкам:
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)  # 0.8999999999999999


# Чтобы определить тип переменной, можно использовать встроенную функцию type():
name = "Ivan"       # строка "Ivan"
print(type(name))   # <class 'str'>

n = 5               # целое число
print(type(n))      # <class 'int'>

r = 5.0             # вещественное число
print(type(r))      # <class 'float'>


"""СЛОЖЕНИЕ"""
# x = 10
# y = 5
# summary = x + y
# print(summary)  # 15


"""ВЫЧИТАНИЕ"""
# x = 10.5
# y = 5.5
# summary = x - y
# print(summary)  # 5.0


"""УМНОЖЕНИЕ"""
# x = 10
# y = 5
# z = x * y
# print(z)  # 50


"""ДЕЛЕНИЕ"""
# x = 10
# y = 5
# z = x / y
# print(z)  # 2.0


# x = 10
# y = 0
# z = x / y
# print(z)  # ZeroDivisionError: division by zero - на ноль делить нельзя!


"""ВОЗВЕДЕНИЕ В СТЕПЕНЬ"""
# x = 2
# print(x ** 3)  # 8


"""ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ"""
# x = 9
# y = 4
# print(x // y)  # 2 - целочисленное деление


"""ОСТАТОК ОТ ДЕЛЕНИЯ"""
# x = 9
# y = 4
# print(x % y)  # 1 - остаток


"""ВОЗВЕДЕНИЕ В СТЕПЕНЬ"""
# big_number = 10 ** 1000
# print(big_number)  # very big number


"""ПРЕОБРАЗОВАНИЕ ТИПА ДАННЫХ"""
# my_int = 1
# my_float = float(my_int)  # преобразуем int в float
# print(my_float)  # 1.0


# my_float = 1.9999
# my_int = int(my_float)  # преобразуем float в int
# print(my_int)  # 1


# nonsense = True
# print(int(nonsense))  # 1
# print(float(nonsense))  # 1.0
# print(str(nonsense))  # True | <class 'str'>


"""ПРИМЕРЫ ОКРУГЛЕНИЯ И РАЗДЕЛЕНИЯ ЧИСЕЛ"""
# my_float = 1.9999
# my_int = round(my_float)
# print(my_int)  # 2


# my_float = 1.4999
# my_int = round(my_float)
# print(my_int)  # 1


# print(math.pi)  # 3.141592653589793
# print(f'{math.pi:.2f}')  # 3.14


# large_number = 123456789
# print(f'{large_number:,}')  # 123,456,789
