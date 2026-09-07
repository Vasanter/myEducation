"""
ИНДЕКСЫ В PYTHON
=================
Индексы — это числовые значения, указывающие на позицию элемента
в последовательности (список, строка, кортеж).

Индексация начинается с 0 (первый элемент) и может быть отрицательной
(с конца последовательности).
"""

# ============================================
# 1. ОСНОВЫ ИНДЕКСАЦИИ
# ============================================

# Визуализация индексов строки "Hello":
# Положительные:  0    1    2    3    4
#                 H    e    l    l    o
# Отрицательные: -5   -4   -3   -2   -1

# Создание списка для примеров:
fruits = ['apple', 'banana', 'cherry', 'watermelon']

# Положительные индексы (с начала):
print(fruits[0])  # 'apple' — первый элемент
print(fruits[1])  # 'banana' — второй элемент
print(fruits[3])  # 'watermelon' — последний элемент

# Отрицательные индексы (с конца):
print(fruits[-1])  # 'watermelon' — последний элемент
print(fruits[-3])  # 'banana' — третий с конца
print(fruits[-4])  # 'apple' — первый элемент

# Вычисление индекса последнего элемента:
last_index = len(fruits) - 1
print(fruits[last_index])  # 'watermelon' — тоже самое, что fruits[-1]

# ============================================
# 2. ОШИБКИ ПРИ ИНДЕКСАЦИИ
# ============================================

# IndexError: индекс вне диапазона
try:
    print(fruits[4])  # IndexError: list index out of range
except IndexError as e:
    print(f"Ошибка: {e}")

try:
    print(fruits[-5])  # IndexError: list index out of range
except IndexError as e:
    print(f"Ошибка: {e}")


# Безопасное обращение по индексу:
def safe_get(sequence, index, default=None):
    """Безопасное получение элемента по индексу"""
    try:
        return sequence[index]
    except IndexError:
        return default


print(safe_get(fruits, 10, "Нет элемента"))  # "Нет элемента"
print(safe_get(fruits, 1))  # 'banana'

# ============================================
# 3. ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ ПО ИНДЕКСУ
# ============================================

# Замена элемента:
fruits[0] = 'pineapple'
print(fruits)  # ['pineapple', 'banana', 'cherry', 'watermelon']

# Восстановим список:
fruits = ['apple', 'banana', 'cherry', 'watermelon']

# Замена через отрицательный индекс:
fruits[-1] = 'grape'
print(fruits)  # ['apple', 'banana', 'cherry', 'grape']

# ============================================
# 4. ОБМЕН ЗНАЧЕНИЙ ПО ИНДЕКСАМ
# ============================================

fruits = ['apple', 'banana', 'cherry', 'watermelon']

# Обмен первого и последнего элемента:
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)  # ['watermelon', 'banana', 'cherry', 'apple']

# Обмен соседних элементов:
fruits[1], fruits[2] = fruits[2], fruits[1]
print(fruits)  # ['watermelon', 'cherry', 'banana', 'apple']

# ============================================
# 5. ИНДЕКСАЦИЯ РАЗНЫХ ТИПОВ ДАННЫХ
# ============================================

# Строки (только чтение):
text = "Hello"
print(f"Первый символ: {text[0]}")  # 'H'
print(f"Последний символ: {text[-1]}")  # 'o'
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment

# Кортежи (только чтение):
my_tuple = (10, 20, 30, 40)
print(f"Элемент кортежа: {my_tuple[2]}")  # 30
# my_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment

# Словари (по ключу, не по индексу):
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Значение по ключу: {my_dict['b']}")  # 2

# Множества (не поддерживают индексацию):
my_set = {1, 2, 3}
# print(my_set[0])  # TypeError: 'set' object is not subscriptable

# Вложенные структуры:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Первый вложенный список: {nested_list[0]}")  # [1, 2, 3]
print(f"Элемент вложенного списка: {nested_list[1][2]}")  # 6
print(f"Последний элемент последнего списка: {nested_list[-1][-1]}")  # 9

# ============================================
# 6. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Получение первого и последнего элемента:
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
last = numbers[-1]
print(f"Первое число: {first}, последнее: {last}")

# Проверка на пустоту перед индексацией:
empty_list = []
if empty_list:
    print(empty_list[0])
else:
    print("Список пуст")

# Итерация с индексами:
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f"Индекс {i}: {fruits[i]}")

# Использование enumerate() для индексов:
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Доступ к символам строки в цикле:
word = "Python"
for i in range(len(word)):
    print(f"Символ {i}: {word[i]}")

# Работа с матрицей (список списков):
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Получение диагонали:
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Диагональ: {diagonal}")  # [1, 5, 9]

# Обратная диагональ:
reverse_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(f"Обратная диагональ: {reverse_diagonal}")  # [3, 5, 7]

# Поиск индекса элемента:
fruits = ['apple', 'banana', 'cherry', 'watermelon']
index = fruits.index('banana')
print(f"Индекс 'banana': {index}")  # 1

# Поиск с обработкой ошибки:
try:
    index = fruits.index('grape')
    print(f"Индекс 'grape': {index}")
except ValueError:
    print("'grape' не найден в списке")


# Проверка существования индекса:
def has_index(sequence, index):
    """Проверка, существует ли индекс в последовательности"""
    return -len(sequence) <= index < len(sequence)


print(has_index(fruits, 0))  # True
print(has_index(fruits, 5))  # False
print(has_index(fruits, -1))  # True
print(has_index(fruits, -5))  # False
