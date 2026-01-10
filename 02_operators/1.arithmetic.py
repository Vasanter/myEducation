import math

"""АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ"""
'''Сложение'''
# x = 10
# y = 5
# summary = x + y
# print(summary)  # 15


# summ = True + False  # True является единицей, False - нулем
# print(summ, type(summ))  # 1 <class 'int'>


'''Вычитание'''
# x = 10.5
# y = 5.5
# summary = x - y
# print(summary)  # 5.0


# summ = False - True + 1.5
# print(summ, type(summ))  # 0.5 <class 'float'>


'''Умножение'''
# x = 10
# y = 5
# z = x * y
# print(z)  # 50


'''Деление'''
# x = 10
# y = 5
# z = x / y
# print(z)  # 2.0


# x = 10
# y = 0
# z = x / y
# print(z)  # ZeroDivisionError: division by zero - на ноль делить нельзя!


'''Возведение в степень'''
# x = 2
# print(x ** 3)  # 8


'''Целочисленное деление'''
# x = 9
# y = 4
# print(x // y)  # 2 - целочисленное деление


'''Остаток от деления'''
# x = 9
# y = 4
# print(x % y)  # 1 - в остатке


'''Возведение в степень'''
# big_number = 10 ** 1000
# print(big_number)  # очень большое число


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
# my_int = round(my_float)  # функция round() используется для округления чисел
# print(my_int)  # 2


# my_float = 1.4999
# my_int = round(my_float)
# print(my_int)  # 1


# print(math.pi)  # 3.141592653589793
# print(f'{math.pi:.2f}')  # 3.14


# large_number = 123456789
# print(f'{large_number:,}')  # 123,456,789
