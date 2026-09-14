"""
ДЕКОРАТОРЫ В PYTHON
=====================
Декоратор — инструмент для модификации поведения функций или классов
без изменения их исходного кода.

Основная идея:
Декоратор «оборачивает» функцию, добавляя дополнительное поведение
до или после её выполнения.

Синтаксис:
    @decorator_name
    def function():
        ...
"""

import time
from functools import wraps


# ============================================
# 1. ПРОСТОЙ ПРИМЕР: ДЕКОРАТОР-ТАЙМЕР
# ============================================

def timer(func):
    """
    Декоратор для измерения времени выполнения функции.

    Принимает функцию (func) как объект, чтобы «обернуть» её новой логикой.
    """
    def wrapper(*args, **kwargs):
        """
        «Матрёшка»: *args и **kwargs позволяют обёртке принимать
        любые аргументы, которые могут быть у целевой функции.
        """
        time_start = time.time()      # время начала
        result = func(*args, **kwargs)  # выполняем функцию
        time_end = time.time()        # время окончания

        elapsed = time_end - time_start
        print(f"⏱️ {func.__name__}: {elapsed:.8f} сек")
        return result  # возвращаем результат функции

    return wrapper  # возвращаем готовую «обёртку»


@timer
def func_one():
    my_list = [i for i in range(1, 1_000_000)]


@timer
def func_two():
    my_list = [i for i in range(1, 1_000_000)]


func_one()
func_two()
# ⏱️ func_one: 0.04512382 сек
# ⏱️ func_two: 0.04489712 сек

# ⚠️ В исходном коде было два бага:
# 1. func() вызывалась без аргументов — упало бы на функциях с параметрами
# 2. wrapper возвращал строку с временем, а не результат функции


# ============================================
# 2. КАК ЭТО РАБОТАЕТ (ПОШАГОВО)
# ============================================

"""
Когда вы пишете:

    @timer
    def func_one():
        ...

Python делает следующее:

    func_one = timer(func_one)

То есть:
1. Функция func_one передаётся в timer как аргумент
2. timer возвращает wrapper
3. Имя func_one теперь ссылается на wrapper
4. При вызове func_one() вызывается wrapper()

Визуально:

    func_one() ──► wrapper() ──► func() (оригинал)
                     │
                     ├─ до:  time_start = time.time()
                     ├─ во время: func()
                     └─ после: time_end = time.time()
"""


# ============================================
# 3. БЕЗ @ И С @ — ОДИНАКОВЫЙ РЕЗУЛЬТАТ
# ============================================

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_hello():
    print("Hello!")


# Способ 1: явный вызов (без @)
my_decorator(say_hello)()
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# Способ 2: через @ (рекомендуется)
@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# ============================================
# 4. ДЕКОРАТОР С АРГУМЕНТАМИ
# ============================================

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello(*, name: str):
    print(f"Hello, {name}!")


say_hello(name="Sasha")
# Something is happening before the function is called.
# Hello, Sasha!
# Something is happening after the function is called.


# ============================================
# 5. ДЕКОРАТОР С ВОЗВРАТОМ РЕЗУЛЬТАТА
# ============================================

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)  # сохраняем результат
        print("Something is happening after the function is called.")
        return result  # возвращаем результат
    return wrapper


@my_decorator
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b


result = add_numbers(a=10, b=5)
print(f"The result is {result}")
# Something is happening before the function is called.
# Adding numbers...
# Something is happening after the function is called.
# The result is 15


# ============================================
# 6. ВАЖНО: @WRAPS ДЛЯ СОХРАНЕНИЯ МЕТАДАННЫХ
# ============================================

# ❌ Без @wraps теряется информация о функции:

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@bad_decorator
def greet(name):
    """Приветствие пользователя"""
    return f"Hello, {name}"


print(greet.__name__)   # wrapper  ← потеряли имя!
print(greet.__doc__)    # None     ← потеряли docstring!


# ✅ Решение: использовать @wraps

def good_decorator(func):
    @wraps(func)  # сохраняет __name__, __doc__ и др.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@good_decorator
def greet(name):
    """Приветствие пользователя"""
    return f"Hello, {name}"


print(greet.__name__)   # greet  ✅
print(greet.__doc__)    # Приветствие пользователя  ✅


# ============================================
# 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# --- 1. Логирование вызовов ---
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📞 Вызов: {func.__name__}")
        print(f"   args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"   → {result}")
        return result
    return wrapper


@log_calls
def multiply(a, b):
    return a * b


multiply(3, 5)
# 📞 Вызов: multiply
#    args=(3, 5), kwargs={}
#    → 15


# --- 2. Кэширование (мемоизация) ---
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))  # мгновенно благодаря кэшу


# --- 3. Проверка прав доступа ---
def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Доступ запрещён: нужны права администратора")
        return func(user, *args, **kwargs)
    return wrapper


@require_admin
def delete_user(user, user_id):
    return f"Пользователь {user_id} удалён"


admin = {"name": "Alice", "role": "admin"}
user = {"name": "Bob", "role": "user"}

print(delete_user(admin, 42))  # Пользователь 42 удалён
# print(delete_user(user, 42))  # PermissionError


# --- 4. Повторные попытки при ошибке ---
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {attempt}/{max_attempts}: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.1)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Временная ошибка")
    return "Успех!"


# unstable_function()


# --- 5. Валидация аргументов ---
def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Аргумент {arg} должен быть положительным")
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def sqrt(x):
    return x ** 0.5


print(sqrt(16))  # 4.0
# print(sqrt(-4))  # ValueError


# --- 6. Замер времени выполнения (production-версия) ---
def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"⏱️ {func.__name__}: {elapsed*1000:.3f} мс")
    return wrapper


@benchmark
def slow_operation():
    time.sleep(0.1)
    return "готово"


slow_operation()


# ============================================
# 8. НЕСКОЛЬКО ДЕКОРАТОРОВ
# ============================================

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


@bold
@italic
def greet(name):
    return f"Hello, {name}"


print(greet("Alice"))  # <b><i>Hello, Alice</i></b>

# Порядок важен!
# @bold
# @italic
# def greet(): ...  →  bold(italic(greet))

# @italic
# @bold
# def greet(): ...  →  italic(bold(greet))


# ============================================
# 9. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  ДЕКОРАТОРЫ — ШПАРГАЛКА                                  │
├──────────────────────────────────────────────────────────┤
│  СТРУКТУРА:                                              │
│  def decorator(func):                                    │
│      @wraps(func)                                        │
│      def wrapper(*args, **kwargs):                       │
│          # до вызова                                     │
│          result = func(*args, **kwargs)                  │
│          # после вызова                                  │
│          return result                                   │
│      return wrapper                                      │
├──────────────────────────────────────────────────────────┤
│  ИСПОЛЬЗОВАНИЕ:                                          │
│  @decorator                                              │
│  def my_func(): ...                                      │
├──────────────────────────────────────────────────────────┤
│  С АРГУМЕНТАМИ:                                          │
│  def decorator(arg1, arg2):                              │
│      def wrapper(func):                                  │
│          def inner(*args, **kwargs):                     │
│              return func(*args, **kwargs)                │
│          return inner                                    │
│      return wrapper                                      │
│                                                          │
│  @decorator(arg1, arg2)                                  │
│  def my_func(): ...                                      │
├──────────────────────────────────────────────────────────┤
│  ВАЖНО:                                                  │
│  • @wraps сохраняет __name__, __doc__                    │
│  • *args, **kwargs — принимают любые аргументы           │
│  • Возвращайте result, если функция что-то возвращает    │
│  • Порядок декораторов: снизу вверх                      │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 10. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Забыли *args, **kwargs
def bad_timer(func):
    def wrapper():        # не примет аргументы!
        func()
    return wrapper


@bad_timer
def add(a, b):
    return a + b


# add(1, 2)  # TypeError: wrapper() takes 0 positional arguments


# ✅ Решение:
def good_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# ❌ Ошибка 2: Не возвращаем результат
def bad_logger(func):
    def wrapper(*args, **kwargs):
        print("Calling...")
        func(*args, **kwargs)  # результат потерян!
    return wrapper


# ✅ Решение:
def good_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling...")
        result = func(*args, **kwargs)
        return result
    return wrapper


# ❌ Ошибка 3: Нет @wraps
def bad(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@bad
def greet(name):
    """Docstring"""
    return f"Hi, {name}"


print(greet.__name__)   # wrapper (а должно быть greet)
print(greet.__doc__)    # None

# ✅ Решение: использовать @wraps


# ❌ Ошибка 4: Декоратор без скобок, когда нужны аргументы
# @retry  ← ошибка, если retry требует аргументов
# def my_func(): ...

# ✅ Решение:
# @retry(max_attempts=3)
# def my_func(): ...


# ❌ Ошибка 5: Путаница с порядком декораторов
@bold
@italic
def greet1():
    return "Hi"

@italic
@bold
def greet2():
    return "Hi"

print(greet1())  # <b><i>Hi</i></b>
print(greet2())  # <i><b>Hi</b></i>
# Порядок важен!