"""
ФУНКЦИИ В PYTHON
==================
Функция — именованный блок кода, который выполняет определённую задачу.
Может принимать входные данные (аргументы), выполнять операции и возвращать результат.

Преимущества:
- Структурирование кода
- Читаемость
- Многократное использование
- Избегание дублирования (DRY — Don't Repeat Yourself)
"""

import operator


# ============================================
# 1. ОБЪЯВЛЕНИЕ И ВЫЗОВ ФУНКЦИИ
# ============================================

def greet(name):
    """Эта функция приветствует пользователя"""
    print(f"Привет, {name}!")


# Вызов функции:
greet("Анна")  # Привет, Анна!


# ============================================
# 2. ЗАГЛУШКА ФУНКЦИИ (PLACEHOLDER)
# ============================================

# Если функция ещё не реализована — используйте raise NotImplementedError
# вместо pass (более информативно):

def connect():
    """Функция подключения к БД (ещё не реализована)"""
    raise NotImplementedError("Функция connect() не содержит кода")


# connect()  # NotImplementedError: Функция connect() не содержит кода


# ============================================
# 3. АРГУМЕНТЫ ПО УМОЛЧАНИЮ
# ============================================

def power(base, exponent=2):
    """Возведение в степень (по умолчанию — квадрат)"""
    return base ** exponent


print(power(3))      # 9 (3 во 2 степени)
print(power(3, 3))   # 27 (3 в 3 степени)


# ============================================
# 4. ПЕРЕМЕННОЕ КОЛИЧЕСТВО АРГУМЕНТОВ
# ============================================

# *args — позиционные аргументы (кортеж):
def sum_all(*args):
    """Сумма всех переданных чисел"""
    return sum(args)


print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())               # 0


# **kwargs — именованные аргументы (словарь):
def print_info(**kwargs):
    """Вывод информации о пользователе"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Анна", age=25)
# name: Анна
# age: 25


# Комбинация *args и **kwargs:
def mixed_func(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


mixed_func(1, 2, 3, 4, 5, name="Alice", age=30)
# a = 1, b = 2
# args = (3, 4, 5)
# kwargs = {'name': 'Alice', 'age': 30}


# ============================================
# 5. ВОЗВРАТ НЕСКОЛЬКИХ ЗНАЧЕНИЙ
# ============================================

def min_max(numbers):
    """Возвращает минимум и максимум (кортеж)"""
    return min(numbers), max(numbers)


minimum, maximum = min_max([12, 3, 11, 5, 2, 16, 11, 10, 8, 4, 9])
print(f"Наименьшее число => {minimum}")   # 2
print(f"Наибольшее число => {maximum}")   # 16


# ============================================
# 6. ПРОСТЫЕ ПРИМЕРЫ
# ============================================

# ПРИМЕР 1: Проверка чётности
def check_parity(number):
    """Проверка числа на чётность"""
    if number % 2 == 0:
        return f'Число {number} - чётное!'
    return f'Число {number} - нечётное!'


print(check_parity(int(input("Enter a number: "))))


# ПРИМЕР 2: Подсчёт среднего значения
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]


def find_average(numbers):
    """Находит среднее значение списка"""
    return sum(numbers) / len(numbers)


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)

print(average_1, average_2, sep=' / ')  # 3.0 / 8.0


# ПРИМЕР 3: Подсчёт гласных букв в строке
def count_vowels(string):
    """Подсчёт гласных букв (русские + английские)"""
    vowels = 'аяуюоеёэиыАЯУЮОЕЁЭИЫaeiouyAEIOUY'
    return sum(1 for char in string if char in vowels)


print(count_vowels("Привет Антон!"))  # 4


# ПРИМЕР 4: Приветствие с несколькими аргументами
def welcome_message(name, age, location):
    """Приветствие пользователя"""
    print(f"Shalom, {name}. You are {age} and from {location}!")


welcome_message('Valdo', 37, 'Belgium')
welcome_message('Ted', 30, 'Turkey')


# ============================================
# 7. ПРОБЛЕМА ПОЗИЦИОННЫХ АРГУМЕНТОВ
# ============================================

# ❌ ПЛОХОЙ ПРИМЕР: перепутали параметры (день - месяц)
def format_date_bad(day, month):
    return f"The date is {day} of {month}."


print(format_date_bad(15, "October"))    # The date is 15 of October.
print(format_date_bad("January", 1))     # The date is January of 1. — ОШИБКА!


# ✅ РЕШЕНИЕ: keyword-only аргументы через *
def format_date(*, day: int, month: str) -> str:
    """
    Форматирование даты.

    * — все параметры после * должны передаваться только по имени.
    : int, : str — аннотации типов (type hints).
    -> str — тип возвращаемого значения.
    """
    return f"The date is {day} of {month}."


print(format_date(day=15, month="October"))  # The date is 15 of October.
# print(format_date("January", 1))  # TypeError: takes 0 positional arguments


# ============================================
# 8. KEYWORD-ONLY И POSITIONAL-ONLY АРГУМЕНТЫ
# ============================================

# Пример с keyword-only аргументами:
def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    """Приветствие с настраиваемым обращением"""
    return f"{greeting}, {name}!"


print(custom_greeting(name="John"))                      # Hello, John!
print(custom_greeting(name="John", greeting="Good morning"))  # Good morning, John!


# Пример с positional-only аргументами (Python 3.8+):
def divide(a, b, /):
    """
    / — все параметры ДО / должны передаваться только позиционно.
    """
    return a / b


print(divide(10, 2))       # 5.0
# print(divide(a=10, b=2))  # TypeError: got some positional-only arguments passed as keyword arguments


# ============================================
# 9. АННОТАЦИИ ТИПОВ (TYPE HINTS)
# ============================================

def add(a: int, b: int) -> int:
    """Сложение двух чисел"""
    return a + b


def greet_person(name: str, age: int = 18) -> str:
    """Приветствие с возвратом строки"""
    return f"Привет, {name}! Тебе {age} лет."


# Аннотации не обязательны, но полезны:
# - Улучшают читаемость
# - Помогают IDE (автодополнение, проверка типов)
# - Можно проверить через mypy


# ============================================
# 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# ПРИМЕР 5: Конвертер валют
def to_euro(amount):
    """Конвертация рублей в евро"""
    rate = 92.09
    return amount / rate


def to_usd(amount):
    """Конвертация рублей в доллары"""
    rate = 78.23
    return amount / rate


print("Конвертер валют\n"
      "1 — пара: RUB -> EURO\n"
      "2 — пара: RUB -> USD")

money = float(input("Введите сумму: "))
choice = int(input("Выберите пару: "))

if choice == 1:
    print("При пересчёте в евро:", round(to_euro(money), 2))
elif choice == 2:
    print("При пересчёте в доллары:", round(to_usd(money), 2))
else:
    print("Такой пары нет!")


# ПРИМЕР 6: Калькулятор (улучшенный)
def calc(a, b, operation):
    """
    Калькулятор с поддержкой нескольких операций.

    Использует модуль operator для чистого кода без eval().
    """
    operations = {
        '+': (operator.add, '+'),
        '-': (operator.sub, '-'),
        '*': (operator.mul, '*'),
        '/': (operator.truediv, '/'),
        '**': (operator.pow, '**'),
        '//': (operator.floordiv, '//'),
        '%': (operator.mod, '%'),
    }

    if operation not in operations:
        return f'Операция => {operation} — не поддерживается!'

    if operation in ('/', '//', '%') and b == 0:
        return 'Ошибка: Деление на ноль!'

    func, symbol = operations[operation]
    return f'{a} {symbol} {b} = {func(a, b)}'


# Тесты:
print(calc(2, 3, '**'))   # 2 ** 3 = 8
print(calc(10, 3, '/'))   # 10 / 3 = 3.3333333333333335
print(calc(10, 0, '/'))   # Ошибка: Деление на ноль!
print(calc(10, 3, '//'))  # 10 // 3 = 3
print(calc(10, 3, '%'))   # 10 % 3 = 1


# ============================================
# 11. ДОКУМЕНТИРОВАНИЕ ФУНКЦИЙ
# ============================================

def calculate_area(length: float, width: float) -> float:
    """
    Вычисляет площадь прямоугольника.

    Args:
        length: Длина прямоугольника (положительное число).
        width: Ширина прямоугольника (положительное число).

    Returns:
        Площадь прямоугольника.

    Raises:
        ValueError: Если length или width отрицательные.

    Examples:
        >>> calculate_area(5, 3)
        15
        >>> calculate_area(-1, 3)
        ValueError: Длина и ширина должны быть положительными
    """
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными")
    return length * width


print(calculate_area(5, 3))  # 15


# ============================================
# 12. ШПАРГАЛКА
# ============================================

"""
┌─────────────────────────────────────────────────────────┐
│  ФУНКЦИИ В PYTHON — ШПАРГАЛКА                           │
├─────────────────────────────────────────────────────────┤
│  ОБЪЯВЛЕНИЕ:                                            │
│  def func_name(params):                                 │
│      '''docstring'''                                    │
│      body                                               │
│      return value                                       │
├─────────────────────────────────────────────────────────┤
│  АРГУМЕНТЫ:                                             │
│  def f(a, b):              — позиционные                │
│  def f(a, b=10):           — по умолчанию               │
│  def f(*args):             — переменное кол-во          │
│  def f(**kwargs):          — именованные                │
│  def f(*, a, b):           — keyword-only               │
│  def f(a, b, /):           — positional-only (3.8+)     │
├─────────────────────────────────────────────────────────┤
│  ВОЗВРАТ:                                               │
│  return value              — одно значение              │
│  return a, b               — кортеж                     │
│  return                    — None                       │
├─────────────────────────────────────────────────────────┤
│  АННОТАЦИИ ТИПОВ:                                       │
│  def f(a: int, b: str) -> bool:                         │
└─────────────────────────────────────────────────────────┘
"""


# ============================================
# 13. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Изменяемые аргументы по умолчанию
def bad_append(item, lst=[]):  # список создаётся ОДИН раз при определении!
    lst.append(item)
    return lst


print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] — не [2]!
print(bad_append(3))  # [1, 2, 3]


# ✅ Решение: использовать None
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(good_append(1))  # [1]
print(good_append(2))  # [2]
print(good_append(3))  # [3]


# ❌ Ошибка 2: Забыли return
def add_bad(a, b):
    a + b  # результат вычислен, но не возвращён!


result = add_bad(2, 3)
print(result)  # None


# ✅ Решение:
def add_good(a, b):
    return a + b


print(add_good(2, 3))  # 5


# ❌ Ошибка 3: Изменение порядка аргументов
def format_date_bad(day, month):
    return f"{day} of {month}"


# print(format_date_bad("October", 15))  # October of 15 — семантически неверно!

# ✅ Решение: keyword-only аргументы
def format_date_good(*, day: int, month: str):
    return f"{day} of {month}"


print(format_date_good(day=15, month="October"))  # 15 of October