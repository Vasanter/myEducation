"""
ТИПЫ ДАННЫХ В PYTHON
=====================
Python имеет динамическую типизацию, но каждый объект принадлежит определённому типу.
Типы делятся на изменяемые (mutable) и неизменяемые (immutable).
"""

# ============================================
# ИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ (MUTABLE)
# ============================================
# Можно изменять содержимое после создания

"""СПИСКИ - list"""
# Упорядоченная, изменяемая коллекция объектов разных типов.
# Поддерживает индексацию, срезы, добавление и удаление элементов.
var_list = ['Ok', 1.275, ['Australia'], 100500, {1, 2, 3}]
print(var_list, type(var_list))  # ['Ok', 1.275, ['Australia'], 100500, {1, 2, 3}] <class 'list'>

# Основные операции со списками:
var_list.append('new')  # добавить элемент
var_list.remove(100500)  # удалить элемент
var_list[0] = 'Changed'  # изменить элемент
print(var_list, '\n' + '-' * 50)

"""СЛОВАРИ - dict"""
# Изменяемая коллекция пар «ключ-значение».
# Ключи словаря должны быть уникальными и неизменяемыми (строки, числа, кортежи).
var_dict = {1: 'mango', 2: 'banana', 3: 'apple'}
print(var_dict, type(var_dict))  # {1: 'mango', 2: 'banana', 3: 'apple'} <class 'dict'>

# Основные операции:
var_dict[4] = 'orange'  # добавить пару
var_dict[1] = 'kiwi'  # изменить значение
del var_dict[2]  # удалить пару
print(var_dict['kiwi'] if 'kiwi' in var_dict.values() else 'no kiwi')
print('-' * 50)

"""МНОЖЕСТВА - set"""
# Неупорядоченная коллекция уникальных элементов.
# Поддерживает математические операции над множествами.
var_set = {1, 2, 3, 4, 5}
print(var_set, type(var_set))  # {1, 2, 3, 4, 5} <class 'set'>

# Операции с множествами:
var_set.add(6)  # добавить элемент
var_set.remove(1)  # удалить элемент
set2 = {4, 5, 6, 7}
print("Объединение:", var_set | set2)  # {2, 3, 4, 5, 6, 7}
print("Пересечение:", var_set & set2)  # {4, 5, 6}
print("Разность:", var_set - set2)  # {2, 3}
print('-' * 50)

# ============================================
# НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ (IMMUTABLE)
# ============================================
# Нельзя изменить после создания (при "изменении" создаётся новый объект)

"""ЧИСЛА - int, float, complex"""

# INT — целые числа
# В Python нет ограничений на размер целых чисел
var_int = 100
print(var_int, type(var_int))  # 100 <class 'int'>

# Операции с int:
print(2 ** 10)  # 1024 — возведение в степень
print(17 // 5)  # 3 — целочисленное деление
print(17 % 5)  # 2 — остаток от деления
print(abs(-42))  # 42 — модуль числа
print(bin(42))  # '0b101010' — двоичное представление
print(hex(42))  # '0x2a' — шестнадцатеричное представление
print('-' * 50)

# FLOAT — числа с плавающей точкой
var_float = 1.275
print(var_float, type(var_float))  # 1.275 <class 'float'>

# Проблема точности float:
print(0.1 + 0.2)  # 0.30000000000000004 (не 0.3!)
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)  # 0.8999999999999999

# Решение проблемы точности:
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.2'))  # 0.3 — точное вычисление

# Округление:
print(round(2.675, 2))  # 2.67 (из-за особенностей float)
print(round(Decimal('2.675'), 2))  # 2.68 (правильно)
print('-' * 50)

# COMPLEX — комплексные числа
# Состоят из реальной и мнимой части (a + bj)
num1 = complex(2, 3)
print(num1, type(num1))  # (2+3j) <class 'complex'>

# Операции с комплексными числами:
num2 = 1 + 2j
print("Сложение:", num1 + num2)  # (3+5j)
print("Умножение:", num1 * num2)  # (-4+7j)
print("Реальная часть:", num1.real)  # 2.0
print("Мнимая часть:", num1.imag)  # 3.0
print("Модуль:", abs(num1))  # 3.605551275463989
print('-' * 50)

"""СТРОКИ - str"""
# Неизменяемая упорядоченная последовательность символов
variable = "Hello, world!"
print(variable, type(variable))  # Hello, world! <class 'str'>

# Разные способы создания строк:
s1 = 'Одинарные кавычки'
s2 = "Двойные кавычки"
s3 = '''Тройные кавычки
для многострочного текста'''
s4 = "Строка с 'кавычками' внутри"
s5 = 'Строка с "кавычками" внутри'
s6 = r"Сырая строка \n не интерпретируется"
s7 = f"F-строка: {variable}"  # форматирование

# Неизменяемость строк:
text = "hello"
# text[0] = "H"  # TypeError: 'str' object does not support item assignment
text = "H" + text[1:]  # Правильный способ — создание новой строки
print('-' * 50)

"""КОРТЕЖИ - tuple"""
# Упорядоченная, неизменяемая коллекция (неизменяемый список)
var_tuple = ('Ok', 1.275, ['Australia'], 100500, {1, 2, 3})
print(var_tuple, type(var_tuple))  # ('Ok', 1.275, ['Australia'], 100500, {1, 2, 3}) <class 'tuple'>

# Особенности кортежей:
single_element = (1,)  # кортеж с одним элементом (запятая обязательна!)
not_tuple = (1)  # это просто число, не кортеж
print(type(single_element))  # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# Вложенные изменяемые объекты в кортеже можно изменять:
var_tuple[2].append('New')  # список внутри кортежа можно изменить
print(var_tuple)

# Упаковка и распаковка:
a, b, c = 1, 2, 3  # упаковка
coordinates = (10, 20)
x, y = coordinates  # распаковка
print(f"x={x}, y={y}")
print('-' * 50)

"""НЕИЗМЕНЯЕМОЕ МНОЖЕСТВО - frozenset"""
# Неизменяемый аналог set. Можно использовать как ключ словаря.
my_list = [1, 2, 3, 4, 5]
frozen = frozenset(my_list)
print(frozen, type(frozen))  # frozenset({1, 2, 3, 4, 5}) <class 'frozenset'>

# frozenset можно использовать как ключ словаря:
dict_with_frozenset = {frozenset([1, 2]): "value"}
print(dict_with_frozenset)

# Обычный set нельзя использовать как ключ:
# {set([1, 2]): "value"}  # TypeError: unhashable type: 'set'
print('-' * 50)

"""БУЛЕВЫЙ ТИП - bool"""
# Принимает два значения: True и False
x = 10
y = 10
print(x == y)  # True
print(type(x == y))  # <class 'bool'>

# Что является False в Python:
print("Ложные значения:")
print(bool(0))  # False — ноль
print(bool(0.0))  # False — ноль с плавающей точкой
print(bool(""))  # False — пустая строка
print(bool([]))  # False — пустой список
print(bool({}))  # False — пустой словарь
print(bool(set()))  # False — пустое множество
print(bool(None))  # False — None

# Всё остальное — True:
print("\nИстинные значения:")
print(bool(1))  # True — ненулевое число
print(bool(" "))  # True — непустая строка (даже пробел)
print(bool([0]))  # True — непустой список

# ============================================
# СРАВНЕНИЕ ТИПОВ ДАННЫХ
# ============================================

print("\n" + "=" * 50)
print("ИТОГОВАЯ ТАБЛИЦА ТИПОВ")
print("=" * 50)

types_examples = [
    ("int", 42, "Целое число"),
    ("float", 3.14, "Число с плавающей точкой"),
    ("complex", 2 + 3j, "Комплексное число"),
    ("str", "текст", "Строка"),
    ("list", [1, 2, 3], "Список (изменяемый)"),
    ("tuple", (1, 2, 3), "Кортеж (неизменяемый)"),
    ("dict", {"a": 1}, "Словарь (изменяемый)"),
    ("set", {1, 2, 3}, "Множество (изменяемое)"),
    ("frozenset", frozenset([1, 2]), "Неизменяемое множество"),
    ("bool", True, "Логический тип"),
    ("NoneType", None, "Отсутствие значения"),
]

for type_name, example, description in types_examples:
    print(f"{type_name:15} | {str(example):20} | {description}")

# ============================================
# ПРОВЕРКА ТИПОВ
# ============================================

# Функция isinstance() для проверки типа:
print(isinstance(42, int))  # True
print(isinstance("text", str))  # True
print(isinstance([1, 2], (list, tuple)))  # True (можно проверять несколько типов)

# Преобразование типов:
num_str = "123"
num_int = int(num_str)  # строка в число
num_float = float(num_str)  # строка в float
text = str(123)  # число в строку
list_from_string = list("abc")  # строка в список ['a', 'b', 'c']
tuple_from_list = tuple([1, 2, 3])  # список в кортеж
set_from_list = set([1, 2, 2, 3])  # список в множество {1, 2, 3}
