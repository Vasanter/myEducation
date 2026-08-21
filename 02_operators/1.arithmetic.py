import math

"""
АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ В PYTHON
==================================
Python поддерживает все основные арифметические операции.
"""

# ============================================
# 1. СЛОЖЕНИЕ (+)
# ============================================

# Обычное сложение:
x = 10
y = 5
summary = x + y
print(summary)  # 15

# Сложение с булевыми значениями (True=1, False=0):
summ = True + False
print(summ, type(summ))  # 1 <class 'int'>

# Сложение строк (конкатенация):
str_result = "Hello " + "my " + "friend!"
print(str_result)  # Hello my friend!

# Сложение списков:
list_result = [1, 2] + [3, 4]
print(list_result)  # [1, 2, 3, 4]

# Сложение с присваиванием:
x = 5
x += 3  # эквивалентно x = x + 3
print(x)  # 8


# ============================================
# 2. ВЫЧИТАНИЕ (-)
# ============================================

x = 10.5
y = 5.5
result = x - y
print(result)  # 5.0

# Вычитание с булевыми значениями:
summ = False - True + 1.5
print(summ, type(summ))  # 0.5 <class 'float'>

# Унарный минус:
number = 5
negative = -number
print(negative)  # -5

# Вычитание с присваиванием:
x = 10
x -= 4  # эквивалентно x = x - 4
print(x)  # 6


# ============================================
# 3. УМНОЖЕНИЕ (*)
# ============================================

x = 10
y = 5
z = x * y
print(z)  # 50

# Умножение строк:
print("Ha" * 3)  # HaHaHa

# Умножение списков:
print([0] * 5)  # [0, 0, 0, 0, 0]

# Умножение с присваиванием:
x = 4
x *= 3  # эквивалентно x = x * 3
print(x)  # 12


# ============================================
# 4. ДЕЛЕНИЕ (/)
# ============================================

# Обычное деление (всегда возвращает float):
x = 10
y = 5
z = x / y
print(z, type(z))  # 2.0 <class 'float'>

# Деление с остатком:
print(7 / 2)  # 3.5

# Деление на ноль:
# x = 10
# y = 0
# z = x / y  # ZeroDivisionError: division by zero

# Безопасное деление:
def safe_divide(a, b):
    """Безопасное деление с обработкой ошибки"""
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf') if a > 0 else float('-inf') if a < 0 else float('nan')

print(safe_divide(10, 0))  # inf
print(safe_divide(0, 0))   # nan


# ============================================
# 5. ВОЗВЕДЕНИЕ В СТЕПЕНЬ (**)
# ============================================

x = 2
print(x ** 3)  # 8

# Встроенная функция pow():
print(pow(2, 3))  # 8
print(pow(2, 3, 5))  # 3 (2^3 % 5)

# Квадратный корень:
print(16 ** 0.5)  # 4.0
print(math.sqrt(16))  # 4.0

# Большие числа:
big_number = 10 ** 100
print(f"10^100 = {big_number}")  # число с 101 цифрой

# Отрицательные степени:
print(2 ** -1)  # 0.5


# ============================================
# 6. ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ (//)
# ============================================

x = 9
y = 4
print(x // y)  # 2

# Особенности с отрицательными числами:
print(-9 // 4)  # -3 (округление вниз)
print(9 // -4)  # -3

# Целочисленное деление с присваиванием:
x = 10
x //= 3  # эквивалентно x = x // 3
print(x)  # 3


# ============================================
# 7. ОСТАТОК ОТ ДЕЛЕНИЯ (%)
# ============================================

x = 9
y = 4
print(x % y)  # 1

# Практические применения:
# Проверка на чётность:
print(10 % 2)  # 0 (чётное)
print(7 % 2)   # 1 (нечётное)

# Выделение цифр числа:
number = 12345
print(number % 10)  # 5 (последняя цифра)
print(number % 100)  # 45 (последние две цифры)

# Циклический перебор:
for i in range(10):
    print(i % 3, end=' ')  # 0 1 2 0 1 2 0 1 2 0
print()

# Остаток с присваиванием:
x = 17
x %= 5  # эквивалентно x = x % 5
print(x)  # 2


# ============================================
# 8. ПРЕОБРАЗОВАНИЕ ТИПОВ ДАННЫХ
# ============================================

# int в float:
my_int = 1
my_float = float(my_int)
print(my_float, type(my_float))  # 1.0 <class 'float'>

# float в int (отбрасывание дробной части):
my_float = 1.9999
my_int = int(my_float)
print(my_int)  # 1 (не округляет, а отбрасывает!)

# Строка в число:
str_num = "123"
print(int(str_num))  # 123
print(float(str_num))  # 123.0

# Булевы значения в числа:
nonsense = True
print(int(nonsense))  # 1
print(float(nonsense))  # 1.0
print(str(nonsense))  # True

# Числа в строку:
print(str(123))  # "123"
print(str(1.5))  # "1.5"

# В двоичную, восьмеричную, шестнадцатеричную системы:
print(bin(42))  # '0b101010'
print(oct(42))  # '0o52'
print(hex(42))  # '0x2a'

# Из других систем в десятичную:
print(int('101010', 2))  # 42 (из двоичной)
print(int('52', 8))  # 42 (из восьмеричной)
print(int('2a', 16))  # 42 (из шестнадцатеричной)


# ============================================
# 9. ОКРУГЛЕНИЕ ЧИСЕЛ
# ============================================

# Функция round():
my_float = 1.9999
my_int = round(my_float)
print(my_int)  # 2

# round() с указанием количества знаков:
print(round(3.14159, 2))  # 3.14
print(round(3.14159, 3))  # 3.142

# Особенности round() (банковское округление):
print(round(2.5))  # 2 (не 3! - округление к чётному)
print(round(3.5))  # 4 (округление к чётному)
print(round(4.5))  # 4

# Округление вверх (ceil):
print(math.ceil(1.1))  # 2
print(math.ceil(1.9))  # 2
print(math.ceil(-1.1))  # -1

# Округление вниз (floor):
print(math.floor(1.1))  # 1
print(math.floor(1.9))  # 1
print(math.floor(-1.1))  # -2

# Модуль числа:
print(abs(-42))  # 42
print(abs(42))  # 42
print(abs(-3.14))  # 3.14


# ============================================
# 10. ФОРМАТИРОВАНИЕ ЧИСЕЛ
# ============================================

# Число Пи:
print(math.pi)  # 3.141592653589793
print(f'{math.pi:.2f}')  # 3.14
print(f'{math.pi:.4f}')  # 3.1416

# Разделители тысяч:
large_number = 123456789
print(f'{large_number:,}')  # 123,456,789

# Проценты:
percentage = 0.25
print(f'{percentage:.0%}')  # 25%
print(f'{percentage:.1%}')  # 25.0%

# Экспоненциальная запись:
print(f'{large_number:e}')  # 1.234568e+08
print(f'{large_number:.2e}')  # 1.23e+08

# Выравнивание чисел:
for num in [1, 12, 123, 1234]:
    print(f'|{num:>5}|')  # выравнивание вправо
    print(f'|{num:<5}|')  # выравнивание влево
    print(f'|{num:^5}|')  # выравнивание по центру


# ============================================
# 11. МАТЕМАТИЧЕСКИЕ ФУНКЦИИ МОДУЛЯ MATH
# ============================================

# Основные функции:
print(math.sqrt(16))  # 4.0 — квадратный корень
print(math.pow(2, 3))  # 8.0 — возведение в степень
print(math.factorial(5))  # 120 — факториал
print(math.gcd(12, 18))  # 6 — наибольший общий делитель
print(math.lcm(12, 18))  # 36 — наименьшее общее кратное (Python 3.9+)

# Тригонометрические функции:
angle = math.pi / 2
print(math.sin(angle))  # 1.0
print(math.cos(angle))  # 6.123233995736766e-17 (~0)
print(math.tan(0))  # 0.0

# Константы:
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.tau)  # 6.283185307179586 (2π)
print(math.inf)  # бесконечность
print(math.nan)  # Not a Number


# ============================================
# 12. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Вычисление площади круга:
radius = 5
area = math.pi * radius ** 2
print(f'Площадь круга радиусом {radius}: {area:.2f}')  # 78.54

# Конвертация температуры:
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f'{celsius}°C = {fahrenheit}°F')  # 25°C = 77.0°F

# Вычисление среднего значения:
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f'Среднее: {average}')  # 30.0

# Проверка на простое число:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(18))  # False

# Решение квадратного уравнения:
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Нет действительных корней"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Один корень: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Два корня: x1 = {x1}, x2 = {x2}"

print(solve_quadratic(1, -5, 6))  # Два корня: x1 = 3.0, x2 = 2.0
print(solve_quadratic(1, 2, 1))  # Один корень: x = -1.0
print(solve_quadratic(1, 1, 1))  # Нет действительных корней