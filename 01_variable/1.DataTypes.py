"""ИЗМЕНЯЕМЫЕ типы данных"""
# ... для определения типа переменной или объекта используется функция type

"""СПИСКИ - list"""
# Списки используются для хранения упорядоченных коллекций элементов произвольных типов:
var_list = ['Ok', 1.275, ['Australia'], 100500, {1, 2, 3}]
print(var_list, type(var_list), '\n- - - - -')  # Output: ['Ok', 1.275, ['Australia'], 100500, {1, 2, 3}]
# <class 'list'> - список

"""СЛОВАРИ - dict"""
# Это тип данных, представляющий собой коллекцию из уникального ключа и связанного с ним значения:
var_dict = {1: 'mango', 2: 'banana', 3: 'apple'}
print(var_dict, type(var_dict), '\n- - - - -')  # Output: {1: 'mango', 2: 'banana', 3: 'apple'} <class 'dict'> - словарь

"""МНОЖЕСТВА - set"""
# Это изменяемая структура данных, предназначенная для хранения уникальных и неупорядоченных элементов
var_set = {1, 2, 3, 4, 5}
print(var_set, type(var_set), '\n- - - - -')  # Output: {1, 2, 3, 4, 5} <class 'set'> - множества

"""НЕИЗМЕНЯЕМЫЕ типы данных"""
# В программировании числа классифицируются прежде всего на целые (тип int, т.е. integer) и вещественные -
# (тип float) с плавающей запятой.
# Целые числа (int) в Python представляются без десятичной точки. Они могут быть положительными или отрицательными.
# В Python нет ограничений на длину целых чисел, то есть целые числа могут быть очень большими.

# Вещественные числа поддерживают те же операции, что и целые.
# Однако (из-за представления чисел в компьютере) вещественные числа неточны, и это может привести к ошибкам:
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)  # 0.8999999999999999

"""ЧИСЛА - int, float, complex"""
var_int = 100
print(var_int, type(var_int), '\n- - - - -')  # 100 <class 'int'> - целое число

var_float = 1.275
print(var_float, type(var_float), '\n- - - - -')  # <class 'float'> - число с плавающей точкой (вещественное)

# Функция complex() используется для создания комплексного числа. Комплексное число состоит из двух частей: реальной и
# мнимой части, обозначаемых в виде a + bj, где a - это реальная часть, b - мнимая часть, а j - мнимая единица.
# Создание комплексного числа 2+3j:
num1 = complex(2, 3)
print(num1, type(num1), '\n- - - - -')  # (2+3j) <class 'complex'>

"""СТРОКИ - str"""
variable = "Hello, world!"
print(variable, type(variable), '\n- - - - -')  # Hello, world! <class 'str'>

"""КОРТЕЖИ - tuple"""
# Кортежи по сути это неизменяемые списки
var_tuple = ('Ok', 1.275, ['Australia'], 100500, {1, 2, 3})
print(var_tuple, type(var_tuple), '\n- - - - -')  # ('Ok', 1.275, ['Australia'], 100500, {1, 2, 3})
# <class 'tuple'>


"""Неизменяемое множество - frozenset"""
my_list = [1, 2, 3, 4, 5]
print(my_list, type(frozenset(my_list)), '\n- - - - -')  # [1, 2, 3, 4, 5] <class 'frozenset'>

# БУЛЕВЫЙ тип данных (bool) — это примитивный тип данных, который принимает два значения — True (истина) и False (ложь)
x = 10
y = 10
print(x == y)  # Outputs: True
print(type(x == y), '\n- - - - -')  # <class 'bool'>  # Outputs: True

x = 9
y = 10
print(x == y)  # Outputs: False
print(type(x == y))  # <class 'bool'>
