"""
ВСТРОЕННЫЕ ФУНКЦИИ PYTHON ДЛЯ РАБОТЫ С ДАННЫМИ
================================================
Python предоставляет множество встроенных функций, которые не требуют
импорта и доступны в любом месте программы.
"""

# ============================================
# 1. ПРЕОБРАЗОВАНИЕ ТИПОВ
# ============================================

# int() — преобразование в целое число
my_float = 1.9999
my_int = int(my_float)  # отбрасывает дробную часть (не округляет!)
print(my_int)  # 1

# float() — преобразование в число с плавающей точкой
my_int = 1
my_float = float(my_int)
print(my_float)  # 1.0

# str() — преобразование в строку
print(str(42))  # '42'
print(str(3.14))  # '3.14'

# bool() — преобразование в логическое значение
nonsense = True
print(int(nonsense))  # 1
print(float(nonsense))  # 1.0
print(str(nonsense))  # 'True'

# Что считается False:
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(None))  # False

# Из строки в число:
print(int("123"))  # 123
print(float("3.14"))  # 3.14


# ============================================
# 2. МАТЕМАТИЧЕСКИЕ ФУНКЦИИ
# ============================================

# abs() — модуль числа
print(abs(-5))  # 5
print(abs(5))  # 5
print(abs(-3.14))  # 3.14

# pow() — возведение в степень
print(pow(2, 3))  # 8
print(pow(2, 3, 5))  # 3 (2^3 % 5)
print(2 ** 3)  # 8 (оператор ** делает то же самое)

# round() — округление
print(round(1.9999))  # 2
print(round(2.5))  # 2 (банковское округление к чётному!)
print(round(3.5))  # 4
print(round(3.14159, 2))  # 3.14

# min(), max(), sum() — минимум, максимум, сумма
nums = [4, 2, 9, 5]
print(min(nums))  # 2
print(max(nums))  # 9
print(sum(nums))  # 20

# С несколькими аргументами:
print(min(4, 2, 9, 5))  # 2
print(max(4, 2, 9, 5))  # 9

# sum() с начальным значением:
print(sum(nums, 100))  # 120 (20 + 100)


# ============================================
# 3. РАБОТА С КОЛЛЕКЦИЯМИ
# ============================================

# len() — длина объекта
print(len("Python"))  # 6
print(len([1, 25, 39]))  # 3
print(len({"a": 1, "b": 2}))  # 2

# sorted() — сортировка (возвращает новый список)
print(sorted([3, 1, 4]))  # [1, 3, 4]
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1]
print(sorted("hello", reverse=True))  # ['o', 'l', 'l', 'e', 'h']

# Сортировка по ключу:
words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))  # ['apple', 'banana', 'cherry']

# zip() — объединение коллекций
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30)]

# Распаковка zip:
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Обратный zip:
pairs = [('Alice', 25), ('Bob', 30)]
names, ages = zip(*pairs)
print(names)  # ('Alice', 'Bob')
print(ages)  # (25, 30)

# enumerate() — нумерация элементов
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# С начальным индексом:
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")


# ============================================
# 4. ПРОВЕРКА УСЛОВИЙ
# ============================================

# all() — True, если все элементы истинны
nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))  # True (все чётные)
print(all([True, True, False]))  # False

# any() — True, если хотя бы один элемент истинен
print(any(n > 5 for n in nums))  # True (есть числа > 5)
print(any([False, False, True]))  # True
print(any([False, False, False]))  # False

# isinstance() — проверка типа
x = 10
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False
print(isinstance("hello", str))  # True

# Проверка нескольких типов:
print(isinstance(x, (int, float)))  # True


# ============================================
# 5. ДРУГИЕ ПОЛЕЗНЫЕ ФУНКЦИИ
# ============================================

# range() — генерация последовательности
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# reversed() — обратный порядок
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# help() — документация
# help(print)  # покажет документацию для print()

# dir() — все методы и атрибуты объекта
# print(dir(str))  # все методы строки

# eval() — выполнение строки как кода (ОСТОРОЖНО!)
example = '5 + 2 * 8 ** 2'
print(eval(example))  # 133
# ВНИМАНИЕ: eval() небезопасен при работе с пользовательским вводом!

# Безопасная альтернатива:
import ast
print(ast.literal_eval("[1, 2, 3]"))  # [1, 2, 3]


# ============================================
# 6. РАБОТА С ЧИСЛАМИ И МОДУЛЬ MATH
# ============================================

import math

# Константы:
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

# Функции:
print(math.sqrt(16))  # 4.0
print(math.ceil(1.1))  # 2 (вверх)
print(math.floor(1.9))  # 1 (вниз)
print(math.factorial(5))  # 120
print(math.gcd(12, 18))  # 6

# Форматирование чисел:
print(f'{math.pi:.2f}')  # 3.14
large_number = 123456789
print(f'{large_number:,}')  # 123,456,789
print(f'{large_number:_}')  # 123_456_789


# ============================================
# 7. ФУНКЦИИ ДЛЯ РАБОТЫ С ИТЕРАТОРАМИ
# ============================================

# map() — применение функции к каждому элементу
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# С обычной функцией:
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter() — фильтрация элементов
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# С обычной функцией:
def is_positive(x):
    return x > 0

positives = list(filter(is_positive, [-2, -1, 0, 1, 2]))
print(positives)  # [1, 2]

# Комбинация map и filter:
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16]


# ============================================
# 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Статистика списка:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Сумма: {sum(data)}")
print(f"Минимум: {min(data)}")
print(f"Максимум: {max(data)}")
print(f"Среднее: {sum(data) / len(data):.2f}")
print(f"Длина: {len(data)}")

# 2. Проверка пароля:
def is_strong_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return len(password) >= 8 and all([has_upper, has_lower, has_digit, has_special])

print(is_strong_password("Pass123!"))  # True
print(is_strong_password("weak"))  # False

# 3. Индексация сотрудников:
employees = ["Alice", "Bob", "Charlie"]
salaries = [50000, 60000, 70000]

for i, (name, salary) in enumerate(zip(employees, salaries), start=1):
    print(f"{i}. {name}: {salary} руб.")

# 4. Группировка данных:
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# 5. Поиск самого длинного слова:
words = ["cat", "elephant", "dog", "hippopotamus"]
longest = max(words, key=len)
print(f"Самое длинное слово: {longest}")  # hippopotamus

# 6. Сортировка словаря по значению:
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]


# ============================================
# 9. ШПАРГАЛКА
# ============================================

"""
┌─────────────────────────────────────────────────────┐
│  ВСТРОЕННЫЕ ФУНКЦИИ PYTHON — ШПАРГАЛКА              │
├─────────────────────────────────────────────────────┤
│  ПРЕОБРАЗОВАНИЕ ТИПОВ:                              │
│  int(), float(), str(), bool()                      │
├─────────────────────────────────────────────────────┤
│  МАТЕМАТИКА:                                        │
│  abs(), pow(), round(), min(), max(), sum()         │
├─────────────────────────────────────────────────────┤
│  КОЛЛЕКЦИИ:                                         │
│  len(), sorted(), zip(), enumerate(), reversed()    │
├─────────────────────────────────────────────────────┤
│  ПРОВЕРКА:                                          │
│  all(), any(), isinstance()                         │
├─────────────────────────────────────────────────────┤
│  ИТЕРАТОРЫ:                                         │
│  map(), filter(), range()                           │
├─────────────────────────────────────────────────────┤
│  ОТЛАДКА:                                           │
│  help(), dir(), type(), id()                        │
└─────────────────────────────────────────────────────┘
"""