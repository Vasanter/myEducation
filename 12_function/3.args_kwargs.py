"""
*ARGS И **KWARGS В PYTHON
============================
Специальные параметры, позволяющие функциям принимать переменное
количество аргументов. Используются для создания гибких функций.

- *args   — собирает ПОЗИЦИОННЫЕ аргументы в кортеж (tuple)
- **kwargs — собирает ИМЕНОВАННЫЕ аргументы в словарь (dict)

⚠️ Названия args и kwargs — условные. Важны символы * и **.
   Можно писать *numbers, **options — работает так же.
"""

# ============================================
# 1. *ARGS — ПОЗИЦИОННЫЕ АРГУМЕНТЫ
# ============================================

def add_all(*args):
    """
    Складывает все переданные числа.

    *args собирает все позиционные аргументы в кортеж.
    """
    summary = 0
    for num in args:
        summary += num
    return summary


print(add_all(1, 2, 3))          # 6
print(add_all(1, 2, 3, 4, 5))    # 15
print(add_all())                 # 0 (пустой кортеж)
print(add_all(10))               # 10


# Тип внутри функции — кортеж:
def show_args_type(*args):
    print(type(args))  # <class 'tuple'>
    print(args)


show_args_type(1, 2, 3)  # (1, 2, 3)


# ============================================
# 2. РАСПАКОВКА СПИСКА В *ARGS
# ============================================

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

# * перед списком распаковывает его в отдельные аргументы:
print(add_all(*values))                  # 15
print(add_all(*values, *other_values))   # 55

# Без * список передаётся как ОДИН аргумент — ошибка:
# print(add_all(values))  # TypeError: unsupported operand type(s) for +=: 'int' and 'list'


# ============================================
# 3. **KWARGS — ИМЕНОВАННЫЕ АРГУМЕНТЫ
# ============================================

def introduce(**kwargs):
    """
    Выводит все переданные именованные аргументы.

    **kwargs собирает все keyword-аргументы в словарь.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


introduce(name="John", age=30, city="New York")
# name: John
# age: 30
# city: New York


# Тип внутри функции — словарь:
def show_kwargs_type(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)


show_kwargs_type(a=1, b=2)  # {'a': 1, 'b': 2}


# ============================================
# 4. РАСПАКОВКА СЛОВАРЯ В **KWARGS
# ============================================

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

# ** перед словарём распаковывает его в именованные аргументы:
introduce(**person)
# city: New York
# age: 30
# name: John


# ============================================
# 5. КОМБИНАЦИЯ ВСЕХ ТИПОВ АРГУМЕНТОВ
# ============================================

def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    """
    Порядок параметров ВАЖЕН:
    1. Позиционные (x, y)
    2. *args
    3. Keyword-only (value)
    4. **kwargs
    """
    print(f"x = {x}, y = {y}")
    print(f"args = {args}")
    print(f"value = {value}")
    print(f"kwargs = {kwargs}")


address = {
    "city": "Moscow",
    "street": "Red place",
    "house": 12,
}

func_with_all_arguments(
    *[3, 4, 5, 6, 7, 8, 9],  # x=3, y=4, args=(5,6,7,8,9)
    **address                 # kwargs = address
)
# x = 3, y = 4
# args = (5, 6, 7, 8, 9)
# value = 6
# kwargs = {'city': 'Moscow', 'street': 'Red place', 'house': 12}


# ============================================
# 6. ПРАКТИЧЕСКИЙ ПРИМЕР: JOIN_TEXT
# ============================================

def join_text(*strings, sep: str = ' ') -> str:
    """
    Объединяет строки с указанным разделителем.

    Args:
        *strings: произвольное количество строк
        sep: разделитель (keyword-only, по умолчанию пробел)

    Returns:
        Объединённая строка
    """
    return sep.join(strings)


def main() -> None:
    print(join_text('A', 'B', 'C', 'D', sep=' - '))  # A - B - C - D
    print(join_text('ABC', sep=' '))                 # ABC
    print(join_text('A', 'B', 'C', sep=' / '))       # A / B / C
    print(join_text('A', 'B', 'C'))                  # A B C


if __name__ == '__main__':
    main()


# ============================================
# 7. ИМЕНОВАНИЕ АРГУМЕНТОВ
# ============================================

# Названия могут быть любыми — важны только символы * и **:

def sum_numbers(*numbers):        # вместо *args
    return sum(numbers)


def create_user(**data):          # вместо **kwargs
    return data


print(sum_numbers(1, 2, 3))               # 6
print(create_user(name="Alice", age=30))  # {'name': 'Alice', 'age': 30}


# ============================================
# 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Функция логирования с произвольными данными:
def log_message(level, *messages, **context):
    """Логирование сообщений с контекстом"""
    prefix = f"[{level.upper()}]"
    text = " ".join(str(m) for m in messages)
    print(f"{prefix} {text}")
    if context:
        print(f"  Контекст: {context}")


log_message("info", "Пользователь", "вошёл", user_id=42, ip="127.0.0.1")
# [INFO] Пользователь вошёл
#   Контекст: {'user_id': 42, 'ip': '127.0.0.1'}


# 2. Универсальный сумматор:
def total(*numbers, start=0):
    """Сумма чисел с возможностью задать начальное значение"""
    return start + sum(numbers)


print(total(1, 2, 3))            # 6
print(total(1, 2, 3, start=10))  # 16


# 3. Создание словаря из именованных аргументов:
def make_dict(**kwargs):
    """Создаёт словарь из именованных аргументов"""
    return kwargs


config = make_dict(host="localhost", port=5432, debug=True)
print(config)  # {'host': 'localhost', 'port': 5432, 'debug': True}


# 4. Декоратор с аргументами (продвинутый пример):
def repeat(times=1):
    """Декоратор для повторного вызова функции"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")  # Hello, Alice! (3 раза)


# ============================================
# 9. ВАЖНО ЗНАТЬ
# ============================================

"""
✅ ПОРЯДОК ПАРАМЕТРОВ В ФУНКЦИИ:

    def func(pos1, pos2, *args, kw1=default, **kwargs):
         ↑      ↑       ↑       ↑              ↑
         │      │       │       │              └─ именованные
         │      │       │       └─ keyword-only
         │      │       └─ позиционные переменные
         │      └─ обычные позиционные
         └─ обычные позиционные

✅ ЧТО СОБИРАЕТ:
    *args   → tuple  (позиционные)
    **kwargs → dict  (именованные)

✅ РАСПАКОВКА ПРИ ВЫЗОВЕ:
    func(*[1, 2, 3])       → func(1, 2, 3)
    func(**{"a": 1})        → func(a=1)

✅ ИМЕНОВАНИЕ:
    args / kwargs — условные имена.
    Важны символы * и **.

❌ ЧАСТЫЕ ОШИБКИ:
    - Забыли * при распаковке списка
    - Забыли ** при распаковке словаря
    - Неверный порядок параметров
    - Использование args/kwargs без * или **
"""


# ============================================
# 10. ШПАРГАЛКА
# ============================================

"""
┌────────────────────────────────────────────────────────┐
│  *ARGS И **KWARGS — ШПАРГАЛКА                          │
├────────────────────────────────────────────────────────┤
│  ОБЪЯВЛЕНИЕ:                                           │
│  def f(*args):                — позиционные в tuple    │
│  def f(**kwargs):             — именованные в dict     │
│  def f(*args, **kwargs):      — оба типа               │
│  def f(a, b, *args):          — позиционные + args     │
│  def f(*args, key=1):         — args + keyword-only    │
├────────────────────────────────────────────────────────┤
│  ВЫЗОВ С РАСПАКОВКОЙ:                                  │
│  f(*[1, 2, 3])                — список → позиционные   │
│  f(**{"a": 1, "b": 2})        — словарь → именованные  │
│  f(*[1, 2], **{"a": 3})       — комбинация             │
├────────────────────────────────────────────────────────┤
│  ВНУТРИ ФУНКЦИИ:                                       │
│  args — это tuple                                      │
│  kwargs — это dict                                     │
│  Можно перебирать: for x in args, for k, v in kwargs   │
├────────────────────────────────────────────────────────┤
│  ПОРЯДОК ПАРАМЕТРОВ:                                   │
│  pos → *args → keyword-only → **kwargs                 │
└────────────────────────────────────────────────────────┘
"""


# ============================================
# 11. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Забыли * при распаковке списка
def add_all(*args):
    return sum(args)


values = [1, 2, 3]
# print(add_all(values))   # TypeError: unsupported operand type(s)
print(add_all(*values))     # 6

# ❌ Ошибка 2: Забыли ** при распаковке словаря
def greet(name, age):
    print(f"{name}, {age}")


person = {"name": "Alice", "age": 30}
# greet(person)             # TypeError: missing 1 required positional argument
greet(**person)             # Alice, 30

# ❌ Ошибка 3: Неверный порядок параметров
# def bad_func(*args, x, y):  # x, y — keyword-only, нельзя передать позиционно
#     pass

def good_func(x, y, *args):
    pass

# ❌ Ошибка 4: args и kwargs без * или **
# def bad_func(args, kwargs):  # это обычные параметры!
#     pass