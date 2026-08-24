"""
ОПЕРАТОРЫ СРАВНЕНИЯ В PYTHON
==============================
Операторы сравнения используются для сравнения значений и возвращают True или False.
Они необходимы в условных выражениях, циклах и фильтрации данных.
"""

# ============================================
# 1. ОСНОВНЫЕ ОПЕРАТОРЫ СРАВНЕНИЯ
# ============================================

# == (равенство)
x = 5
y = 3
print(f"x == y: {x == y}")  # False

# Сравнение разных типов:
print(5 == 5.0)  # True (int и float сравниваются по значению)
print("hello" == "hello")  # True
print([1, 2] == [1, 2])  # True
print((1, 2) == (1, 2))  # True
print({1, 2} == {2, 1})  # True (порядок не важен для множеств)
print(True == 1)  # True (True эквивалентно 1)

# != (неравенство)
x = 5
y = 3
print(f"x != y: {x != y}")  # True

# Практические примеры:
password = "secret123"
if password != "secret123":
    print("Неверный пароль!")
else:
    print("Доступ разрешён!")

# > (больше)
x = 5
y = 3
print(f"x > y: {x > y}")  # True

# Сравнение строк (лексикографическое):
print("apple" > "banana")  # False ('a' < 'b' в алфавите)
print("abc" > "ABC")  # True (заглавные буквы меньше строчных)

# < (меньше)
x = 5
y = 3
print(f"x < y: {x < y}")  # False

# Сравнение списков:
print([1, 2, 3] < [1, 2, 4])  # True (сравнивает поэлементно)

# >= (больше или равно)
x = 5
y = 5
print(f"x >= y: {x >= y}")  # True

# Практический пример:
age = 18
if age >= 18:
    print("Вы совершеннолетний")

# <= (меньше или равно)
x = 5
y = 7
print(f"x <= y: {x <= y}")  # True

# Практический пример:
score = 75
if score <= 100:
    print("Допустимый балл")

# ============================================
# 2. ЦЕПОЧКИ СРАВНЕНИЙ
# ============================================

# Python позволяет объединять несколько сравнений в цепочку
x = 5
y = 10
z = 15

# Проверка диапазона:
print(x < y < z)  # True (5 < 10 < 15)
# Эквивалентно: (x < y) and (y < z)

# Проверка равенства нескольких значений:
print(x == y == z)  # False
# Эквивалентно: (x == y) and (y == z)

# Смешанные сравнения:
print(x < y > z)  # False (10 не больше 15)
print(x < y <= z)  # True (5 < 10 <= 15)

# Практические примеры:
age = 25
if 18 <= age <= 65:
    print("Вы трудоспособного возраста")

temperature = 22
if 20 <= temperature <= 25:
    print("Комфортная температура")

# Проверка нескольких переменных:
a = 10
b = 10
c = 10
if a == b == c:
    print("Все значения равны")

# ============================================
# 3. СПЕЦИАЛЬНЫЕ ОПЕРАТОРЫ СРАВНЕНИЯ
# ============================================

# IS — проверка идентичности (тот же объект в памяти)
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)  # True (содержимое одинаковое)
print(x is y)  # False (разные объекты в памяти)
print(x is z)  # True (тот же объект)

# Особенности с None:
value = None
print(value is None)  # True
print(value == None)  # True (но лучше использовать is)

# Особенности с булевыми значениями:
print(True is 1)  # False (разные объекты)
print(True == 1)  # True (равны по значению)

# IS NOT — проверка неидентичности
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)  # True

# IN — проверка вхождения
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False

my_string = "Hello World"
print("World" in my_string)  # True
print("world" in my_string)  # False (регистр важен)

my_dict = {"name": "Alice", "age": 30}
print("name" in my_dict)  # True (проверяет ключи)
print("Alice" in my_dict)  # False (не проверяет значения)

# NOT IN — проверка отсутствия
my_list = [1, 2, 3, 4, 5]
print(6 not in my_list)  # True
print(3 not in my_list)  # False

# ============================================
# 4. СРАВНЕНИЕ РАЗНЫХ ТИПОВ ДАННЫХ
# ============================================

# Числа разных типов сравниваются корректно:
print(5 == 5.0)  # True
print(5 == 5 + 0j)  # True (комплексные числа)

# Строки сравниваются лексикографически:
print("apple" < "banana")  # True
print("apple" < "Apple")  # False (заглавные буквы идут раньше)
print("2" > "10")  # True (строки сравниваются посимвольно!)

# Списки и кортежи сравниваются поэлементно:
print([1, 2, 3] < [1, 2, 4])  # True
print((1, 2, 3) < (1, 2, 4))  # True
print([1, 2, 3] == (1, 2, 3))  # False (разные типы)

# Множества:
print({1, 2, 3} == {3, 2, 1})  # True (порядок не важен)
# print({1, 2} < {1, 2, 3})  # True (подмножество)

# Словари сравниваются по ключам и значениям:
print({"a": 1} == {"a": 1})  # True
print({"a": 1} == {"a": 2})  # False
print({"a": 1} == {"b": 1})  # False

# ============================================
# 5. СРАВНЕНИЕ С None, True, False
# ============================================

# None сравнивается только с None:
print(None == None)  # True
print(None == 0)  # False
print(None == "")  # False
print(None == False)  # False

# Правильный способ проверки на None:
value = None
if value is None:
    print("Значение отсутствует")

# Булевы значения:
print(True == 1)  # True
print(False == 0)  # True
print(True > False)  # True (True=1, False=0)


# ============================================
# 6. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Проверка пароля:
def check_password(password):
    if len(password) < 8:
        return "Пароль слишком короткий"
    elif len(password) >= 12:
        return "Отличный пароль!"
    else:
        return "Пароль нормальный"


# Проверка возраста:
def check_age(age):
    if 0 <= age < 13:
        return "Ребёнок"
    elif 13 <= age < 18:
        return "Подросток"
    elif 18 <= age < 65:
        return "Взрослый"
    elif age >= 65:
        return "Пенсионер"
    else:
        return "Некорректный возраст"


# Проверка диапазона:
def is_valid_score(score):
    return 0 <= score <= 100


# Сравнение строк без учёта регистра:
str1 = "Hello"
str2 = "hello"
print(str1.lower() == str2.lower())  # True

# Поиск элемента в списке:
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Банан есть в списке!")

# Проверка на пустоту:
empty_list = []
if not empty_list:
    print("Список пуст")

empty_string = ""
if not empty_string:
    print("Строка пуста")

# ============================================
# 7. СРАВНИТЕЛЬНАЯ ТАБЛИЦА
# ============================================

print("\n" + "=" * 50)
print("ТАБЛИЦА ОПЕРАТОРОВ СРАВНЕНИЯ")
print("=" * 50)

comparisons = [
    ("==", "5 == 5", True, "Равенство"),
    ("!=", "5 != 3", True, "Неравенство"),
    (">", "5 > 3", True, "Больше"),
    ("<", "5 < 3", False, "Меньше"),
    (">=", "5 >= 5", True, "Больше или равно"),
    ("<=", "5 <= 3", False, "Меньше или равно"),
    ("is", "5 is 5", True, "Идентичность"),
    ("is not", "5 is not 3", True, "Неидентичность"),
    ("in", "'a' in 'abc'", True, "Вхождение"),
    ("not in", "'d' not in 'abc'", True, "Отсутствие"),
]

for op, example, result, description in comparisons:
    print(f"{op:8} | {example:12} | {result:5} | {description}")

# ============================================
# 8. ЛОГИЧЕСКИЕ ОПЕРАТОРЫ С СРАВНЕНИЯМИ
# ============================================

# Комбинирование с and, or, not:
age = 25
has_license = True

# AND — оба условия должны быть True:
if age >= 18 and has_license:
    print("Можно водить машину")

# OR — хотя бы одно условие True:
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Сегодня выходной")

# NOT — инверсия результата:
is_blocked = False
if not is_blocked:
    print("Пользователь не заблокирован")

# Комбинирование операторов:
score = 85
attendance = 90

if (score >= 80 and attendance >= 85) or score >= 95:
    print("Отличный результат!")

# ============================================
# 9. СОВЕТЫ И ЛУЧШИЕ ПРАКТИКИ
# ============================================

# 1. Используйте is для None:
# Правильно:
if value is None:
    pass
# Не рекомендуется:
if value == None:
    pass

# 2. Используйте цепочки сравнений:
# Вместо:
if x > 0 and x < 10:
    pass
# Лучше:
if 0 < x < 10:
    pass

# 3. Будьте осторожны с сравнением строк и чисел:
# print("5" > 3)  # TypeError: '>' not supported between instances of 'str' and 'int'

# 4. Используйте in для проверки нескольких значений:
# Вместо:
if color == "red" or color == "green" or color == "blue":
    pass
# Лучше:
if color in ["red", "green", "blue"]:
    pass

# 5. Помните о приоритете операторов:
# Сначала выполняются сравнения, потом and, затем or
x = 5
print(3 < x < 7)  # True (цепочка)
print(3 < x and x < 7)  # True (аналогично)
print(3 < x or x > 10)  # True (достаточно одного условия)
