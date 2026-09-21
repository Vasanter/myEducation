"""
ЛЯМБДА-ФУНКЦИИ (LAMBDA) В PYTHON
===================================
Лямбда-функция — это анонимная (безымянная) функция, которая
определяется в одной строке и может содержать только одно выражение.

Синтаксис:
    lambda параметры: выражение

Особенности:
- Нет имени (анонимная)
- Только одно выражение (не блок кода)
- Возвращает результат выражения автоматически (без return)
- Может быть использована там, где нужна простая функция
"""

# ============================================
# 1. ОБЫЧНАЯ ФУНКЦИЯ VS ЛЯМБДА
# ============================================

# Обычная функция:
def add(a, b):
    return a + b

print(add(2, 3))  # 5

# Эквивалент через lambda:
add_lambda = lambda a, b: a + b
print(add_lambda(2, 3))  # 5

# ?? Лямбда — это выражение, а не инструкция.
#    Можно использовать внутри других выражений.


# ============================================
# 2. ПРОСТЫЕ ПРИМЕРЫ
# ============================================

# Возведение в квадрат:
square = lambda x: x ** 2
print(square(5))  # 25

# Проверка чётности:
is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False

# Максимум из двух чисел:
maximum = lambda a, b: a if a > b else b
print(maximum(10, 7))  # 10

# Приветствие:
greet = lambda name: f"Привет, {name}!"
print(greet("Alice"))  # Привет, Alice!


# ============================================
# 3. ЛЯМБДА БЕЗ АРГУМЕНТОВ
# ============================================

# Лямбда может не принимать аргументов:
say_hello = lambda: "Hello, world!"
print(say_hello())  # Hello, world!

# Генерация случайного числа:
import random
random_number = lambda: random.randint(1, 100)
print(random_number())


# ============================================
# 4. ЛЯМБДА С НЕСКОЛЬКИМИ АРГУМЕНТАМИ
# ============================================

# Три аргумента:
sum_three = lambda a, b, c: a + b + c
print(sum_three(1, 2, 3))  # 6

# С аргументами по умолчанию:
power = lambda base, exp=2: base ** exp
print(power(3))     # 9
print(power(3, 3))  # 27

# С *args:
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4))  # 10

# С **kwargs:
show_info = lambda **kwargs: kwargs
print(show_info(name="Alice", age=30))  # {'name': 'Alice', 'age': 30}


# ============================================
# 5. ЛЯМБДА С УСЛОВИЯМИ (ТЕРНАРНЫЙ ОПЕРАТОР)
# ============================================

# Классификация числа:
classify = lambda x: "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль"
print(classify(5))   # положительное
print(classify(-3))  # отрицательное
print(classify(0))   # ноль

# Оценка:
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade(85))  # B


# ============================================
# 6. ЛЯМБДА С ВСТРОЕННЫМИ ФУНКЦИЯМИ
# ============================================

# --- SORTED() с ключом ---
# Сортировка по длине строки:
words = ["banana", "apple", "cherry", "kiwi"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(sorted_by_len)  # ['kiwi', 'apple', 'banana', 'cherry']

# Сортировка по последнему символу:
sorted_by_last = sorted(words, key=lambda w: w[-1])
print(sorted_by_last)  # ['banana', 'apple', 'kiwi', 'cherry']

# Сортировка словарей по значению:
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_students)


# --- MAP() — применение функции к каждому элементу ---
numbers = [1, 2, 3, 4, 5]

# Квадраты чисел:
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Преобразование в строки:
strings = list(map(lambda x: f"Число {x}", numbers))
print(strings)


# --- FILTER() — фильтрация элементов ---
# Только чётные:
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Только положительные:
mixed = [-3, -1, 0, 1, 2, 3]
positives = list(filter(lambda x: x > 0, mixed))
print(positives)  # [1, 2, 3]


# --- REDUCE() — свёртка последовательности ---
from functools import reduce

# Произведение всех чисел:
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)  # 120

# Максимум через reduce:
maximum = reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9, 4])
print(maximum)  # 9


# --- MAX() / MIN() с ключом ---
words = ["apple", "banana", "kiwi", "cherry"]
longest = max(words, key=lambda w: len(w))
print(longest)  # banana

shortest = min(words, key=lambda w: len(w))
print(shortest)  # kiwi


# ============================================
# 7. ЛЯМБДА В СПИСКОВЫХ ВКЛЮЧЕНИЯХ
# ============================================

# Список функций:
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Ошибка",
}

print(operations["add"](5, 3))       # 8
print(operations["multiply"](4, 7))  # 28
print(operations["divide"](10, 2))   # 5.0
print(operations["divide"](10, 0))   # Ошибка


# ============================================
# 8. ЛЯМБДА КАК АРГУМЕНТ ФУНКЦИИ
# ============================================

def apply_operation(a, b, operation):
    """Применяет операцию к двум числам"""
    return operation(a, b)


# Передаём лямбду как аргумент:
print(apply_operation(5, 3, lambda a, b: a + b))  # 8
print(apply_operation(5, 3, lambda a, b: a * b))  # 15
print(apply_operation(5, 3, lambda a, b: a ** b)) # 125


# ============================================
# 9. ЛЯМБДА В СЛОВАРЯХ
# ============================================

# Меню операций:
calculator = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Деление на ноль",
}

def calculate(a, b, op):
    if op in calculator:
        return calculator[op](a, b)
    return "Неизвестная операция"


print(calculate(10, 5, "+"))  # 15
print(calculate(10, 5, "-"))  # 5
print(calculate(10, 5, "*"))  # 50
print(calculate(10, 5, "/"))  # 2.0
print(calculate(10, 0, "/"))  # Деление на ноль


# ============================================
# 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Сортировка по нескольким критериям:
data = [
    ("Alice", 25, 50000),
    ("Bob", 30, 60000),
    ("Charlie", 25, 55000),
]

# Сортировка по возрасту, затем по зарплате:
sorted_data = sorted(data, key=lambda x: (x[1], x[2]))
print(sorted_data)
# [('Alice', 25, 50000), ('Charlie', 25, 55000), ('Bob', 30, 60000)]


# 2. Фильтрация словарей:
products = [
    {"name": "Ноутбук", "price": 80000, "in_stock": True},
    {"name": "Телефон", "price": 50000, "in_stock": False},
    {"name": "Наушники", "price": 5000, "in_stock": True},
]

# Товары в наличии дешевле 60000:
available = list(filter(
    lambda p: p["in_stock"] and p["price"] < 60000,
    products
))
print(available)  # [{'name': 'Наушники', ...}]


# 3. Цепочка преобразований:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Чётные числа ? квадраты ? сумма:
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)  # 220 (4 + 16 + 36 + 64 + 100)


# 4. Создание функций "на лету":
def make_multiplier(n):
    """Создаёт функцию умножения на n"""
    return lambda x: x * n


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# 5. Обработка данных из API:
users = [
    {"name": "alice", "age": 25, "email": "ALICE@mail.com"},
    {"name": "bob", "age": 17, "email": "BOB@mail.com"},
    {"name": "charlie", "age": 30, "email": "CHARLIE@mail.com"},
]

# Взрослые пользователи с email в нижнем регистре:
adults = list(map(
    lambda u: {"name": u["name"].title(), "email": u["email"].lower()},
    filter(lambda u: u["age"] >= 18, users)
))
print(adults)
# [{'name': 'Alice', 'email': 'alice@mail.com'},
#  {'name': 'Charlie', 'email': 'charlie@mail.com'}]


# ============================================
# 11. КОГДА ИСПОЛЬЗОВАТЬ ЛЯМБДА
# ============================================

"""
? ХОРОШО использовать:
- Для коротких одноразовых функций
- Как аргумент key в sorted(), max(), min()
- В map(), filter(), reduce()
- Для простых операций в словарях
- Когда функция нужна только один раз

? ПЛОХО использовать:
- Для сложной логики (лучше def)
- Когда нужна документация (docstring)
- Когда функция используется многократно
- Когда это ухудшает читаемость
- Для присваивания переменной (PEP 8 не рекомендует)

?? PEP 8: "Всегда используйте def вместо присваивания лямбды имени"
"""

# ? Плохо (PEP 8):
square = lambda x: x ** 2

# ? Хорошо:
def square(x):
    return x ** 2

# ? Лямбда уместна (одноразовое использование):
sorted([3, 1, 2], key=lambda x: -x)  # [3, 2, 1]


# ============================================
# 12. СРАВНЕНИЕ: LAMBDA VS DEF
# ============================================

"""
????????????????????????????????????????????????????????????????
?  Характеристика        ?  lambda          ?  def             ?
????????????????????????????????????????????????????????????????
?  Имя                   ?  Нет             ?  Есть            ?
?  Строк кода            ?  1 выражение     ?  Много           ?
?  Return                ?  Автоматически   ?  Явно            ?
?  Docstring             ?  Нет             ?  Да              ?
?  Аннотации типов       ?  Ограниченно     ?  Да              ?
?  Многострочность       ?  Нет             ?  Да              ?
?  Отладка               ?  Сложнее         ?  Легче           ?
?  Читаемость            ?  Для простого    ?  Для сложного    ?
????????????????????????????????????????????????????????????????
"""


# ============================================
# 13. ШПАРГАЛКА
# ============================================

"""
??????????????????????????????????????????????????????????
?  ЛЯМБДА-ФУНКЦИИ — ШПАРГАЛКА                            ?
??????????????????????????????????????????????????????????
?  СИНТАКСИС:                                            ?
?  lambda параметры: выражение                           ?
??????????????????????????????????????????????????????????
?  ПРИМЕРЫ:                                              ?
?  lambda: 42                    — без аргументов        ?
?  lambda x: x ** 2              — один аргумент         ?
?  lambda a, b: a + b            — два аргумента         ?
?  lambda *args: sum(args)       — переменное кол-во     ?
?  lambda **kw: kw               — именованные           ?
?  lambda x: x if x > 0 else 0   — с условием            ?
??????????????????????????????????????????????????????????
?  ГДЕ ИСПОЛЬЗУЕТСЯ:                                     ?
?  sorted(data, key=lambda x: ...)                       ?
?  max(data, key=lambda x: ...)                          ?
?  min(data, key=lambda x: ...)                          ?
?  map(lambda x: ..., data)                              ?
?  filter(lambda x: ..., data)                           ?
?  reduce(lambda x, y: ..., data)                        ?
??????????????????????????????????????????????????????????
?  ВАЖНО:                                                ?
?  • Только ОДНО выражение                               ?
?  • Не нужен return                                     ?
?  • Анонимная (без имени)                               ?
?  • PEP 8: не присваивайте лямбду переменной            ?
??????????????????????????????????????????????????????????
"""


# ============================================
# 14. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Несколько выражений в лямбде
# bad = lambda x: x + 1; x * 2  # SyntaxError

# ? Решение: использовать def
def good(x):
    x = x + 1
    return x * 2


# ? Ошибка 2: Присваивание лямбды переменной (PEP 8)
# Плохо:
square = lambda x: x ** 2

# ? Хорошо:
def square(x):
    return x ** 2


# ? Ошибка 3: Сложная логика в лямбде
# bad = lambda x: "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 60 else "F"

# ? Решение: использовать def для сложной логики
def get_grade(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    else:
        return "D"


# ? Ошибка 4: Замыкание в цикле
# functions = [lambda: i for i in range(3)]
# print([f() for f in functions])  # [2, 2, 2] — все ссылаются на последний i!

# ? Решение: использовать аргумент по умолчанию
functions = [lambda i=i: i for i in range(3)]
print([f() for f in functions])  # [0, 1, 2]