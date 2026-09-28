"""
ТЕРНАРНЫЙ ОПЕРАТОР В PYTHON
==============================
Тернарный оператор — это специальная конструкция, позволяющая записывать
условное выражение в одну строку.

Синтаксис:
    значение_если_True if условие else значение_если_False

Особенности:
- Не может содержать elif (только if-else)
- Ветка else обязательна (в отличие от обычного if)
- Возвращает значение, а не выполняет действие
"""

# ============================================
# 1. ПРЕОБРАЗОВАНИЕ IF-ELSE В ТЕРНАРНЫЙ ОПЕРАТОР
# ============================================

# Обычный if-else:
a, b = 3, -1

if a > b:
    print(a)
else:
    print(b)

# Тернарный оператор (более компактно):
res = a if a > b else b
print(res)  # 3

# С выражениями:
res = a + 2 if a > b else b - 4
print(res)  # 5

# С вызовом функций:
res = abs(a) if a < b else abs(b)
print(res)  # 1


# ============================================
# 2. ПРИМЕРЫ ПРЕОБРАЗОВАНИЯ
# ============================================

# Пример 1: Ограничение значения
num = int(input("Enter a number: "))

# Обычный вариант:
if num < 20:
    number = num
else:
    number = 100

# Тернарный вариант:
number = num if num < 20 else 100
print(number)


# Пример 2: Максимум из двух чисел
a = 12
b = 7
maximum = a if a > b else b
print(maximum)  # 12


# Пример 3: Проверка чётности
a = int(input("Enter a number: "))
result = "чётное" if a % 2 == 0 else "нечётное"
print(result)


# Пример 4: Выбор метода обработки строки
s = 'python'
_type = 'upper'
res = s.upper() if _type == 'upper' else s.lower()
print(res)  # PYTHON


# ============================================
# 3. ТЕРНАРНЫЙ ОПЕРАТОР С РАЗНЫМИ ТИПАМИ ДАННЫХ
# ============================================

# Со строками:
name = "Alice"
greeting = f"Привет, {name}!" if name else "Привет, незнакомец!"
print(greeting)  # Привет, Alice!

# Со списками:
numbers = [1, 2, 3]
result = numbers[0] if numbers else None
print(result)  # 1

empty = []
result = empty[0] if empty else "Список пуст"
print(result)  # Список пуст

# Со словарями:
user = {"name": "Bob"}
display_name = user["name"] if "name" in user else "Аноним"
print(display_name)  # Bob

# С None:
value = None
result = value if value is not None else "по умолчанию"
print(result)  # по умолчанию


# ============================================
# 4. ВЛОЖЕННЫЕ ТЕРНАРНЫЕ ОПЕРАТОРЫ
# ============================================

# Вложенность (не рекомендуется для сложной логики):
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(f"Оценка: {grade}")  # B

# Альтернатива для читаемости:
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Оценка: {grade}")  # B


# ============================================
# 5. ТЕРНАРНЫЙ ОПЕРАТОР В КОЛЛЕКЦИЯХ
# ============================================

# Списковые включения с условием:
numbers = [-5, -2, 0, 3, 8, -1]

# Классификация чисел:
classified = ["положительное" if n > 0 else "отрицательное" if n < 0 else "ноль" for n in numbers]
print(classified)

# Замена отрицательных значений на 0:
positive_only = [n if n > 0 else 0 for n in numbers]
print(positive_only)  # [0, 0, 0, 3, 8, 0]

# Словарь с условием:
users = ["Alice", "Bob", ""]
user_dict = {name: "активен" if name else "неактивен" for name in users}
print(user_dict)


# ============================================
# 6. ТЕРНАРНЫЙ ОПЕРАТОР В АРГУМЕНТАХ ФУНКЦИЙ
# ============================================

def greet(name, is_formal=True):
    """Приветствие с выбором стиля"""
    title = "Уважаемый" if is_formal else "Привет"
    return f"{title}, {name}!"

print(greet("Иван"))  # Уважаемый, Иван!
print(greet("Иван", False))  # Привет, Иван!

# Внутри f-строк:
age = 17
status = f"{'совершеннолетний' if age >= 18 else 'несовершеннолетний'}"
print(status)  # несовершеннолетний


# ============================================
# 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Безопасное деление:
def safe_divide(a, b):
    return a / b if b != 0 else None

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None

# Получение значения из словаря с дефолтом:
config = {"debug": True}
debug_mode = config.get("debug", False)
log_level = "DEBUG" if debug_mode else "INFO"
print(f"Уровень логирования: {log_level}")  # DEBUG

# Форматирование множественного числа:
def pluralize(count, singular, plural):
    return f"{count} {singular if count == 1 else plural}"

print(pluralize(1, "яблоко", "яблока"))  # 1 яблоко
print(pluralize(5, "яблоко", "яблок"))  # 5 яблок

# Проверка прав доступа:
user_role = "admin"
can_delete = True if user_role == "admin" else False
print(f"Может удалять: {can_delete}")  # True

# Установка значений по умолчанию:
username = input("Введите имя: ").strip()
display_name = username if username else "Гость"
print(f"Добро пожаловать, {display_name}!")


# ============================================
# 8. КОГДА ИСПОЛЬЗОВАТЬ ТЕРНАРНЫЙ ОПЕРАТОР
# ============================================

"""
✅ ХОРОШО использовать:
- Для простых условий в одну строку
- Для присваивания одного из двух значений
- В списковых включениях и генераторах
- В f-строках для условного форматирования
- Для возврата значения из функции

❌ ПЛОХО использовать:
- Для сложной логики с множеством условий (elif)
- Для побочных эффектов (print, вызовы функций с действиями)
- Для вложенных условий глубиной более 2 уровней
- Когда это ухудшает читаемость кода
"""

# Плохой пример (сложно читать):
# result = "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 60 else "F"

# Хороший пример (простое условие):
x = 5
parity = "чётное" if x % 2 == 0 else "нечётное"
print(parity)  # нечётное