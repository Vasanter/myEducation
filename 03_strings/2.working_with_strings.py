"""
РАБОТА СО СТРОКАМИ: КОНКАТЕНАЦИЯ, ФОРМАТИРОВАНИЕ, F-СТРОКИ
============================================================
"""

# ============================================
# 1. СЛОЖЕНИЕ СТРОК (КОНКАТЕНАЦИЯ)
# ============================================

# Конкатенация строк через +
print('Hello ' + 'World!')  # Hello World!
print('My name is ' + 'John')  # My name is John

# Конкатенация с приведением типов:
name = "Alice"
age = 25
print(name + " is " + str(age) + " years old")  # нужно str() для чисел

# Умножение строк (повторение):
print("Ha" * 3)  # HaHaHa
print("-" * 30)  # ------------------------------

# Конкатенация с присваиванием:
message = "Hello"
message += " World"
message += "!"
print(message)  # Hello World!


# ============================================
# 2. МЕТОД FORMAT (УСТАРЕВШИЙ СПОСОБ)
# ============================================

name = "John"
age = 25

# Позиционные аргументы:
print('Вас зовут {} и вам {}!'.format(name, age))
print('Вас зовут {0} и вам {1}!'.format(name, age))

# Именованные аргументы:
print('Вас зовут {n} и вам {a}!'.format(n=name, a=age))

# Форматирование чисел в format:
pi = 3.14159
print('Число Пи: {:.2f}'.format(pi))  # 3.14
print('Проценты: {:.1%}'.format(0.25))  # 25.0%


# ============================================
# 3. F-СТРОКИ (СОВРЕМЕННЫЙ СПОСОБ, Python 3.6+)
# ============================================

name = "Alice"
surname = "Smith"

# Простое использование:
print(f"Приветствую тебя, {name} {surname}!")

# Вычисления внутри f-строк:
print(f"Результат: {2 * 37}")  # Результат: 74

# Отладка с = (Python 3.8+):
print(f"Результат: {2 * 37 = }")  # Результат: 2 * 37 = 74

# Вызов функций и методов:
text = "Hello"
print(f"Длина строки: {len(text)}")  # Длина строки: 5
print(f"Верхний регистр: {text.upper()}")  # HELLO

# Многострочные f-строки:
first = "John"
last = "Doe"
print(f"""
Имя: {first}
Фамилия: {last}
Полное имя: {first} {last}
""")


# ============================================
# 4. ФОРМАТИРОВАНИЕ ЧИСЕЛ В F-СТРОКАХ
# ============================================

# Разделители тысяч:
n = 100000000
print(f"С запятой: {n:,}")  # 100,000,000
print(f"С подчёркиванием: {n:_}")  # 100_000_000

# Округление:
x = 146.56789
print(f"Два знака: {x:.2f}")  # 146.57
print(f"Один знак: {x:.1f}")  # 146.6
print(f"Без дробной части: {x:.0f}")  # 147

# Комбинация разделителя и округления:
big = 14656789.12924
print(f"Форматированное: {big:,.2f}")  # 14,656,789.13

# Проценты:
ratio = 0.875
print(f"Процент: {ratio:.1%}")  # 87.5%

# Экспоненциальная запись:
number = 123456789
print(f"Экспонента: {number:e}")  # 1.234568e+08

# Двоичная, восьмеричная, шестнадцатеричная:
num = 255
print(f"Двоичная: {num:b}")  # 11111111
print(f"Восьмеричная: {num:o}")  # 377
print(f"Шестнадцатеричная: {num:x}")  # ff
print(f"Шестнадцатеричная (верхний): {num:X}")  # FF


# ============================================
# 5. ВЫРАВНИВАНИЕ В F-СТРОКАХ
# ============================================

name = 'Python'

# Выравнивание вправо (ширина 20):
print(f"|{name:>20}|")  # |              Python|

# Выравнивание влево:
print(f"|{name:<20}|")  # |Python              |

# По центру:
print(f"|{name:^20}|")  # |       Python       |

# С заполнителем:
print(f"|{name:*>20}|")  # |**************Python|
print(f"|{name:*<20}|")  # |Python**************|
print(f"|{name:*^20}|")  # |*******Python*******|

# Практический пример (таблица):
users = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print(f"{'Имя':<10} | {'Возраст':>5}")
print("-" * 20)
for user_name, user_age in users:
    print(f"{user_name:<10} | {user_age:>5}")


# ============================================
# 6. ФОРМАТИРОВАНИЕ ДАТЫ И ВРЕМЕНИ
# ============================================

import datetime

today = datetime.datetime.today()

# Различные форматы даты:
print(f"Текущее время: {today:%H:%M:%S}")  # 12:57:57
print(f"Дата: {today:%d-%m-%Y}")  # 05-12-2024
print(f"Дата и время: {today:%d.%m.%Y %H:%M}")  # 05.12.2024 12:57
print(f"Год: {today:%Y}")  # 2024
print(f"Месяц: {today:%B}")  # December
print(f"День недели: {today:%A}")  # Thursday


# ============================================
# 7. F-СТРОКИ С УСЛОВИЯМИ И ЦИКЛАМИ
# ============================================

# Условные выражения:
age = 20
print(f"Статус: {'совершеннолетний' if age >= 18 else 'несовершеннолетний'}")

# Генераторы списков:
numbers = [1, 2, 3, 4, 5]
print(f"Квадраты: {[x**2 for x in numbers]}")

# Словари:
person = {"name": "Alice", "age": 30}
print(f"Имя: {person['name']}, Возраст: {person['age']}")

# Лямбда-функции:
print(f"Сумма: {(lambda x, y: x + y)(5, 3)}")


# ============================================
# 8. СПЕЦИАЛЬНЫЕ МЕТОДЫ СТРОК
# ============================================

# str.format_map() — форматирование из словаря:
data = {"name": "Alice", "age": 25}
print("{name} is {age} years old".format_map(data))


# str.maketrans() и str.translate() — замена символов:
# Простая замена (гласные на цифры):
trans_table = str.maketrans("aeiou", "12345")
text = "hello world"
print(text.translate(trans_table))  # h2ll4 w4rld

# Удаление символов:
delete_table = str.maketrans("", "", "aeiou")
print(text.translate(delete_table))  # hll wrld

# Замена через словарь:
trans_dict = {
    ord('a'): 'A',  # заменить 'a' на 'A'
    ord('e'): 'E',  # заменить 'e' на 'E'
    ord('o'): None  # удалить 'o'
}
dict_table = str.maketrans(trans_dict)
print("hello world".translate(dict_table))  # hEll w rld


# ============================================
# 9. СЫРЫЕ СТРОКИ (RAW STRINGS)
# ============================================

# Обычная строка (нужно экранировать):
print("C:\\Users\\Name\\Documents")  # C:\Users\Name\Documents

# Сырая строка (экранирование не работает):
print(r"C:\Users\Name\Documents")  # C:\Users\Name\Documents

# Проблема с кавычками в сырых строках:
print(r"Как пройти в \"библиотеку?\"")  # Как пройти в \"библиотеку?\"

# Комбинация сырой и f-строки:
file_name = "pic.jpeg"
path = rf"C:\Users\Name\Desktop\Python Project\{file_name}"
print(path)  # C:\Users\Name\Desktop\Python Project\pic.jpeg

# Практическое применение (регулярные выражения):
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # паттерн для поиска SSN
text = "SSN: 123-45-6789"
match = re.search(pattern, text)
print(f"Найдено: {match.group()}" if match else "Не найдено")


# ============================================
# 10. СРАВНЕНИЕ СПОСОБОВ ФОРМАТИРОВАНИЯ
# ============================================

name = "Alice"
age = 25
city = "New York"

# Конкатенация (не рекомендуется):
result1 = "Имя: " + name + ", возраст: " + str(age)

# Метод format (устаревший):
result2 = "Имя: {}, возраст: {}".format(name, age)

# F-строка (рекомендуется):
result3 = f"Имя: {name}, возраст: {age}"

print(f"\n{result1}\n{result2}\n{result3}")

# Производительность:
import timeit

concat_time = timeit.timeit(lambda: "Имя: " + name + ", возраст: " + str(age), number=1000000)
format_time = timeit.timeit(lambda: "Имя: {}, возраст: {}".format(name, age), number=1000000)
fstring_time = timeit.timeit(lambda: f"Имя: {name}, возраст: {age}", number=1000000)

print(f"\nВремя выполнения (1 млн операций):")
print(f"Конкатенация: {concat_time:.4f} сек")
print(f"format(): {format_time:.4f} сек")
print(f"f-строка: {fstring_time:.4f} сек (самая быстрая)")