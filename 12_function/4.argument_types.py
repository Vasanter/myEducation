"""
ТИПЫ АРГУМЕНТОВ В PYTHON
==========================
Python предоставляет гибкую систему аргументов функций.
Всего существует 5 основных типов, которые можно комбинировать.

Порядок параметров ВАЖЕН:
    def func(pos_only, /, normal, *args, kw_only, **kwargs):
         ?          ?       ?        ?         ?        ?
         ?          ?       ?        ?         ?        ?? именованные
         ?          ?       ?        ?         ?? keyword-only
         ?          ?       ?        ?? позиционные переменные
         ?          ?       ?? обычные
         ?          ?? positional-only
         ?? начало
"""


# ============================================
# 1. ПОЗИЦИОННЫЕ АРГУМЕНТЫ (POSITIONAL)
# ============================================

"""
Передаются по порядку. Самый простой и распространённый тип.
"""

def greet(name, age):
    """Обычные позиционные аргументы"""
    print(f"Привет, {name}! Тебе {age} лет.")


# Передача по позиции:
greet("Alice", 30)       # Привет, Alice! Тебе 30 лет.
greet("Bob", 25)         # Привет, Bob! Тебе 25 лет.

# ?? Порядок важен:
# greet(30, "Alice")     # Привет, 30! Тебе Alice лет. — работает, но неверно


# ============================================
# 2. ИМЕНОВАННЫЕ АРГУМЕНТЫ (KEYWORD)
# ============================================

"""
Передаются по имени параметра. Порядок не важен.
Можно комбинировать с позиционными.
"""

def create_user(name, age, city):
    """Аргументы можно передавать по имени"""
    return {"name": name, "age": age, "city": city}


# Всё по имени:
user1 = create_user(name="Alice", age=30, city="Moscow")

# Порядок не важен:
user2 = create_user(city="SPb", name="Bob", age=25)

# Комбинация — позиционные СНАЧАЛА, именованные ПОТОМ:
user3 = create_user("Charlie", 35, city="Kazan")

# ?? Так нельзя:
# create_user(name="Dave", 40, "Sochi")  # SyntaxError


# ============================================
# 3. АРГУМЕНТЫ ПО УМОЛЧАНИЮ (DEFAULT)
# ============================================

"""
Если аргумент не передан — используется значение по умолчанию.
Параметры с default идут ПОСЛЕ обязательных.
"""

def power(base, exponent=2):
    """exponent по умолчанию = 2"""
    return base ** exponent


print(power(3))       # 9  (3^2)
print(power(3, 3))    # 27 (3^3)
print(power(2, 10))   # 1024


# --- Несколько значений по умолчанию ---
def connect(host="localhost", port=5432, timeout=30):
    return f"{host}:{port} (timeout={timeout})"


print(connect())                                    # localhost:5432 (timeout=30)
print(connect("prod.server"))                       # prod.server:5432 (timeout=30)
print(connect(port=3306))                           # localhost:3306 (timeout=30)
print(connect("prod.server", 8080, 60))             # prod.server:8080 (timeout=60)


# ?? ОПАСНО: изменяемые значения по умолчанию!
def bad_append(item, lst=[]):
    """Список создаётся ОДИН раз при определении функции!"""
    lst.append(item)
    return lst


print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] — не [2]!
print(bad_append(3))  # [1, 2, 3]


# ? Решение: использовать None
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(good_append(1))  # [1]
print(good_append(2))  # [2]
print(good_append(3))  # [3]


# ============================================
# 4. *ARGS — ПЕРЕМЕННОЕ ЧИСЛО ПОЗИЦИОННЫХ АРГУМЕНТОВ
# ============================================

"""
*args собирает все лишние позиционные аргументы в КОРТЕЖ.
Название args — условное, важен символ *.
"""

def sum_all(*args):
    """Сумма любого количества чисел"""
    print(f"args = {args}, type = {type(args)}")
    return sum(args)


print(sum_all(1, 2, 3))              # args = (1, 2, 3), 6
print(sum_all(1, 2, 3, 4, 5))        # args = (1, 2, 3, 4, 5), 15
print(sum_all())                     # args = (), 0
print(sum_all(10))                   # args = (10,), 10


# --- С обычными аргументами ---
def greet_all(greeting, *names):
    """greeting — обязательный, names — переменное"""
    for name in names:
        print(f"{greeting}, {name}!")


greet_all("Привет", "Alice", "Bob", "Charlie")
# Привет, Alice!
# Привет, Bob!
# Привет, Charlie!


# --- Распаковка списка в *args ---
numbers = [1, 2, 3, 4, 5]
print(sum_all(*numbers))  # 15

# Объединение списков:
more = [6, 7, 8]
print(sum_all(*numbers, *more))  # 36


# --- Практический пример ---
def calculate(operation, *numbers):
    """Универсальный калькулятор"""
    if operation == "sum":
        return sum(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)


print(calculate("sum", 1, 2, 3))     # 6
print(calculate("max", 5, 2, 9, 1))  # 9


# ============================================
# 5. **KWARGS — ПЕРЕМЕННОЕ ЧИСЛО ИМЕНОВАННЫХ АРГУМЕНТОВ
# ============================================

"""
**kwargs собирает все лишние именованные аргументы в СЛОВАРЬ.
Название kwargs — условное, важен символ **.
"""

def print_info(**kwargs):
    """Вывод информации о пользователе"""
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print_info(name="Alice", age=30, city="Moscow")
# kwargs = {'name': 'Alice', 'age': 30, 'city': 'Moscow'}
#   name: Alice
#   age: 30
#   city: Moscow


# --- Распаковка словаря в **kwargs ---
person = {"name": "Bob", "age": 25, "city": "SPb"}
print_info(**person)


# --- Практический пример ---
def create_html_tag(tag, **attributes):
    """Создаёт HTML-тег с атрибутами"""
    attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
    return f"<{tag} {attrs}>"


print(create_html_tag("a", href="https://example.com", target="_blank"))
# <a href="https://example.com" target="_blank">


# ============================================
# 6. KEYWORD-ONLY АРГУМЕНТЫ (*)
# ============================================

"""
После * все параметры должны передаваться ТОЛЬКО по имени.
Нельзя передать позиционно.
"""

def format_date(*, day: int, month: str) -> str:
    """day и month — только по имени"""
    return f"{day} {month}"


# ? Правильно:
print(format_date(day=15, month="January"))  # 15 January

# ? Нельзя:
# format_date(15, "January")  # TypeError: takes 0 positional arguments


# --- Практическая польза: защита от путаницы ---
# Без keyword-only легко перепутать:
def bad_format_date(day, month):
    return f"{day} {month}"

print(bad_format_date(15, "October"))     # 15 October ?
print(bad_format_date("October", 15))     # October 15 ? — ошибка!

# С keyword-only — невозможно перепутать:
def good_format_date(*, day: int, month: str):
    return f"{day} {month}"

# good_format_date("October", 15)  # TypeError — сразу видно ошибку


# --- Комбинация с *args ---
def func(a, *args, b, c):
    """b и c — только по имени"""
    print(f"a={a}, args={args}, b={b}, c={c}")


func(1, 2, 3, b=4, c=5)
# a=1, args=(2, 3), b=4, c=5

# func(1, 2, 3, 4, 5)  # TypeError: missing b, c


# --- Пример из реального API ---
def log(message, *, level="INFO", timestamp=None):
    """level и timestamp — только по имени"""
    print(f"[{level}] {message}")


log("Server started")                       # [INFO] Server started
log("Error!", level="ERROR")                # [ERROR] Error!
# log("Error!", "ERROR")                    # TypeError


# ============================================
# 7. POSITIONAL-ONLY АРГУМЕНТЫ (/)
# ============================================

"""
До / — параметры передаются ТОЛЬКО позиционно.
Появилось в Python 3.8.
"""

def divide(a, b, /):
    """a и b — только позиционно"""
    return a / b


print(divide(10, 2))    # 5.0
print(divide(10, 5))    # 2.0

# ? Нельзя:
# divide(a=10, b=2)     # TypeError: got some positional-only arguments passed as keyword arguments


# --- Зачем это нужно? ---

# 1. Защита от конфликта имён параметров и **kwargs:
def bad_func(name, **kwargs):
    """Если вызвать func(name="Alice", name="Bob") — конфликт!"""
    pass

def good_func(name, /, **kwargs):
    """name позиционный, name в kwargs — отдельный ключ"""
    print(f"name={name}, kwargs={kwargs}")

good_func("Alice", name="Bob")  # name=Alice, kwargs={'name': 'Bob'}


# 2. Стандартные функции используют это:
# print(*args, sep=" ", end="\n", file=None)
# help(object, /)
# len(obj, /)


# ============================================
# 8. КОМБИНАЦИЯ ВСЕХ ТИПОВ
# ============================================

"""
Полный порядок параметров:

    def func(pos_only, /, normal, *args, kw_only, **kwargs):
         ?          ?   ?        ?        ?         ?
         ?          ?   ?        ?        ?         ?? **kwargs
         ?          ?   ?        ?        ?? keyword-only
         ?          ?   ?        ?? *args
         ?          ?   ?? обычные
         ?          ?? разделитель /
         ?? positional-only
"""

def full_function(a, b, /, c, d, *args, e, f, **kwargs):
    """
    Демонстрация всех типов аргументов.

    Args:
        a, b: positional-only (до /)
        c, d: обычные (позиционные или именованные)
        *args: переменное число позиционных
        e, f: keyword-only (после *)
        **kwargs: переменное число именованных
    """
    print(f"a={a}, b={b}")
    print(f"c={c}, d={d}")
    print(f"args={args}")
    print(f"e={e}, f={f}")
    print(f"kwargs={kwargs}")


full_function(
    1, 2,           # a, b — позиционные
    3, 4,           # c, d — позиционные
    5, 6, 7,        # args
    e=8, f=9,       # keyword-only
    g=10, h=11,     # kwargs
)
# a=1, b=2
# c=3, d=4
# args=(5, 6, 7)
# e=8, f=9
# kwargs={'g': 10, 'h': 11}


# ============================================
# 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# --- 1. Гибкая функция логирования ---
def log(message, *args, level="INFO", **kwargs):
    """
    Логирование с любыми параметрами.

    Пример:
        log("Error", "file.py", 42, level="ERROR", user="admin")
    """
    prefix = f"[{level}]"
    extra = " ".join(str(a) for a in args)
    context = " ".join(f"{k}={v}" for k, v in kwargs.items())

    parts = [prefix, message]
    if extra:
        parts.append(extra)
    if context:
        parts.append(f"({context})")

    print(" ".join(parts))


log("Server started")
# [INFO] Server started

log("File loaded", "data.csv", 1024)
# [INFO] File loaded data.csv 1024

log("Error", "file.py", 42, level="ERROR", user="admin")
# [ERROR] Error file.py 42 (user=admin)


# --- 2. Обёртка с сохранением аргументов ---
from functools import wraps


def logged(func):
    """Декоратор, который логирует все аргументы"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}:")
        print(f"  args = {args}")
        print(f"  kwargs = {kwargs}")
        result = func(*args, **kwargs)
        print(f"  ? {result}")
        return result
    return wrapper


@logged
def add(a, b, *, verbose=False):
    if verbose:
        print(f"Складываю {a} + {b}")
    return a + b


add(2, 3)
# Вызов add:
#   args = (2, 3)
#   kwargs = {}
#   ? 5

add(2, 3, verbose=True)
# Вызов add:
#   args = (2, 3)
#   kwargs = {'verbose': True}
#   Складываю 2 + 3
#   ? 5


# --- 3. Функция с конфигурацией ---
def configure(
    host: str,
    port: int,
    /,
    *,
    timeout: int = 30,
    retries: int = 3,
    **options,
):
    """
    Настройка соединения.

    host, port — только позиционно.
    timeout, retries — только по имени.
    options — любые дополнительные параметры.
    """
    config = {
        "host": host,
        "port": port,
        "timeout": timeout,
        "retries": retries,
        **options,
    }
    return config


config = configure(
    "localhost", 5432,
    timeout=60,
    retries=5,
    ssl=True,
    compression="gzip",
)
print(config)
# {'host': 'localhost', 'port': 5432, 'timeout': 60,
#  'retries': 5, 'ssl': True, 'compression': 'gzip'}


# --- 4. Универсальный декоратор с параметрами ---
def retry(retries=3, delay=1, *, exceptions=(Exception,)):
    """
    Декоратор с параметрами.

    retries, delay — можно позиционно или по имени.
    exceptions — только по имени.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        raise
                    print(f"Попытка {attempt} неудачна: {e}")
            return None
        return wrapper
    return decorator


@retry(3, 0.5, exceptions=(ValueError,))
def unstable():
    import random
    if random.random() < 0.5:
        raise ValueError("Ошибка")
    return "OK"


# ============================================
# 10. РАСПАКОВКА ПРИ ВЫЗОВЕ
# ============================================

# --- * для списков/кортежей ---
def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
print(add(*numbers))       # 6

# --- ** для словарей ---
def greet(name, age):
    return f"{name}, {age}"


person = {"name": "Alice", "age": 30}
print(greet(**person))     # Alice, 30

# --- Комбинация ---
def full(a, b, c, d):
    return a + b + c + d


args = [1, 2]
kwargs = {"d": 4}
print(full(*args, c=3, **kwargs))  # 10

# ?? Осторожно: одинаковые ключи перезаписываются
def func(a, b):
    return a + b


data = {"a": 1, "b": 2}
# func(**data, b=5)  # TypeError: got multiple values for 'b'


# ============================================
# 11. ВСТРОЕННЫЕ ФУНКЦИИ С РАЗНЫМИ ТИПАМИ
# ============================================

"""
Примеры из стандартной библиотеки:

???????????????????????????????????????????????????????????????????????
?  Функция                     ?  Типы аргументов                     ?
???????????????????????????????????????????????????????????????????????
?  print(*args, sep, end)      ?  *args + keyword-only                ?
?  len(obj, /)                 ?  positional-only                     ?
?  sorted(iterable, *, key)    ?  positional + keyword-only           ?
?  max(*args, key=...)         ?  *args + keyword-only                ?
?  dict(**kwargs)              ?  **kwargs                            ?
?  str.format(*args, **kwargs) ?  *args + **kwargs                    ?
?  range(start, stop, step)    ?  позиционные + default               ?
???????????????????????????????????????????????????????????????????????
"""

# print — классический пример:
print("a", "b", "c", sep="-", end="!\n")
# a-b-c!

# sorted — keyword-only для key и reverse:
print(sorted([3, 1, 2], key=lambda x: -x))
# [3, 2, 1]

# max с *args:
print(max(1, 5, 3, 2))  # 5

# dict с **kwargs:
d = dict(name="Alice", age=30)
print(d)  # {'name': 'Alice', 'age': 30}


# ============================================
# 12. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????????
?  ТИПЫ АРГУМЕНТОВ — ШПАРГАЛКА                             ?
????????????????????????????????????????????????????????????
?  ОБЪЯВЛЕНИЕ:                                             ?
?  def f(a, b):                — позиционные               ?
?  def f(a, b=10):             — default                   ?
?  def f(*args):               — переменные позиционные    ?
?  def f(**kwargs):            — переменные именованные    ?
?  def f(*, a, b):             — keyword-only              ?
?  def f(a, b, /):             — positional-only           ?
?  def f(a, /, b, *, c):       — комбинация                ?
????????????????????????????????????????????????????????????
?  ПОРЯДОК ПАРАМЕТРОВ:                                     ?
?  pos_only, /, normal, *args, kw_only, **kwargs           ?
????????????????????????????????????????????????????????????
?  ПЕРЕДАЧА:                                               ?
?  f(1, 2)                     — по позиции                ?
?  f(a=1, b=2)                 — по имени                  ?
?  f(*[1, 2])                  — распаковка списка         ?
?  f(**{"a": 1})               — распаковка словаря        ?
????????????????????????????????????????????????????????????
?  ВАЖНО:                                                  ?
?  ? Не используйте изменяемые default (list, dict)        ?
?  ? *args и **kwargs — условные имена                     ?
?  ? Keyword-only защищает от путаницы                     ?
?  ? Positional-only для API-совместимости                 ?
????????????????????????????????????????????????????????????
"""


# ============================================
# 13. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Изменяемые значения по умолчанию
def bad(item, lst=[]):
    lst.append(item)
    return lst


print(bad(1))  # [1]
print(bad(2))  # [1, 2] — не [2]!


# ? Решение:
def good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# ? Ошибка 2: Порядок аргументов
# def bad(a=1, b):   # SyntaxError: non-default argument follows default argument
#     pass


# ? Решение: сначала обязательные, потом с default
def good(a, b=1):
    pass


# ? Ошибка 3: Забыли * для keyword-only
def bad_format(day, month):
    return f"{day} {month}"


print(bad_format("October", 15))  # October 15 — перепутали!


# ? Решение:
def good_format(*, day: int, month: str):
    return f"{day} {month}"


# good_format("October", 15)  # TypeError — сразу видно


# ? Ошибка 4: Позиционные после keyword в вызове
# func(a=1, 2)  # SyntaxError: positional argument follows keyword argument


# ? Решение: сначала позиционные
# func(2, a=1)


# ? Ошибка 5: Дублирование аргумента
def func(a, b):
    return a + b


# func(1, a=2)  # TypeError: got multiple values for argument 'a'


# ? Решение: не дублировать
func(1, b=2)  # 3


# ? Ошибка 6: Изменение kwargs во время итерации
def process(**kwargs):
    # for key in kwargs:
    #     del kwargs[key]   # RuntimeError
    for key in list(kwargs.keys()):
        del kwargs[key]


# ? Решение: list(kwargs.keys())


# ? Ошибка 7: args как обычное имя
def bad(args):     # это НЕ *args — обычный параметр!
    pass


def good(*args):   # это *args — кортеж
    pass