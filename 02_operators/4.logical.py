"""
ЛОГИЧЕСКИЕ ОПЕРАТОРЫ В PYTHON
===============================
Используются для выполнения логических операций (часто вместе
с операторами сравнения), возвращающих True или False.

Приоритет логических операторов (от высшего к низшему):
1. not — логическое НЕ (наивысший приоритет)
2. and — логическое И
3. or  — логическое ИЛИ (низший приоритет)
"""

# ============================================
# AND — ЛОГИЧЕСКОЕ И
# ============================================
# True, если ОБА условия истинны

x = 5
y = 8
print(f"{x} > 1 and {y} < 10: {x > 1 and y < 10}")  # True (оба условия True)

# Пример с False:
print(f"{x} > 10 and {y} < 10: {x > 10 and y < 10}")  # False (первое условие False)

# Таблица истинности для and:
print("\nТаблица истинности AND:")
print(f"True and True: {True and True}")  # True
print(f"True and False: {True and False}")  # False
print(f"False and True: {False and True}")  # False
print(f"False and False: {False and False}")  # False

# ============================================
# OR — ЛОГИЧЕСКОЕ ИЛИ
# ============================================
# True, если ХОТЯ БЫ ОДНО условие истинно

x = 5
print(f"\n{x} < 1 or {x} > 10: {x < 1 or x > 10}")  # False (оба условия False)

# Пример с True:
print(f"{x} < 1 or {x} > 4: {x < 1 or x > 4}")  # True (второе условие True)

# Таблица истинности для or:
print("\nТаблица истинности OR:")
print(f"True or True: {True or True}")  # True
print(f"True or False: {True or False}")  # True
print(f"False or True: {False or True}")  # True
print(f"False or False: {False or False}")  # False

# ============================================
# NOT — ЛОГИЧЕСКОЕ НЕ
# ============================================
# Инвертирует логическое значение (True ↔ False)

x = 5
y = 8
result = x > 1 and y < 10
print(f"\nresult = {result}")  # True
print(f"not result: {not result}")  # False

# Инверсия False:
print(f"not (5 > 10): {not (5 > 10)}")  # True

# Таблица истинности для not:
print("\nТаблица истинности NOT:")
print(f"not True: {not True}")  # False
print(f"not False: {not False}")  # True

# ============================================
# КОМБИНИРОВАНИЕ ОПЕРАТОРОВ
# ============================================

# Приоритет: not → and → or
age = 25
has_license = True
is_suspended = False

# Комбинация and и not:
print(f"\nПроверка прав: {age >= 18 and has_license and not is_suspended}")  # True

# Скобки меняют приоритет:
a = True
b = False
c = True

print(f"\nnot a and b: {not a and b}")  # False (сначала not, потом and)
print(f"not (a and b): {not (a and b)}")  # True (скобки меняют порядок)

# Комбинация and и or:
print(f"a and b or c: {a and b or c}")  # True (and выполняется первым)
print(f"a and (b or c): {a and (b or c)}")  # True (скобки меняют порядок)

# ============================================
# ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Проверка диапазона:
score = 75
if score >= 0 and score <= 100:
    print(f"\nБалл {score} в допустимом диапазоне")

# Проверка нескольких условий:
username = "admin"
password = "secret123"
if username == "admin" and password == "secret123":
    print("Доступ разрешён")

# Проверка с or:
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Сегодня выходной")

# Комплексная проверка:
age = 20
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:
    print("Вход разрешён")
else:
    print("Вход запрещён")

# ============================================
# ПОЛНАЯ ТАБЛИЦА ПРИОРИТЕТОВ ОПЕРАТОРОВ
# ============================================
"""
1. ( )              - скобки
2. **               - возведение в степень
3. +x, -x, ~x       - унарные плюс, минус, битовое НЕ
4. *, /, //, %      - умножение, деление
5. +, -             - сложение, вычитание
6. <<, >>           - битовые сдвиги
7. &                - битовое И
8. ^                - битовое исключающее ИЛИ
9. |                - битовое ИЛИ
10. <, <=, >, >=, ==, !=, is, is not, in, not in  - сравнения
11. not             - логическое НЕ
12. and             - логическое И
13. or              - логическое ИЛИ
"""
