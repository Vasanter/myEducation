"""
ИНДЕКСЫ, СРЕЗЫ И РАЗВОРОТ СПИСКОВ В PYTHON
=============================================
"""

# ============================================
# 1. ИНДЕКСЫ
# ============================================

"""
Индексы — это числовые значения, указывающие на позицию элемента 
в последовательности (список, строка, кортеж).

Положительные индексы: 0, 1, 2, 3, 4 (слева направо)
Отрицательные индексы: -5, -4, -3, -2, -1 (справа налево)

  0   1   2   3   4
  H   e   l   l   o
 -5  -4  -3  -2  -1
"""

fruits = ['apple', 'banana', 'cherry', 'watermelon']

# Получение элементов по индексу:
print(fruits[0])   # 'apple' (первый элемент)
print(fruits[-1])  # 'watermelon' (последний элемент)
print(fruits[-4])  # 'apple' (эквивалентно fruits[0])
print(fruits[3])   # 'watermelon' (эквивалентно fruits[-1])

# Ошибки при выходе за границы:
# print(fruits[4])   # IndexError: list index out of range
# print(fruits[-5])  # IndexError: list index out of range

# Изменение элементов по индексу:
fruits[0] = 'pineapple'
print(fruits)  # ['pineapple', 'banana', 'cherry', 'watermelon']

# Множественное присваивание по индексам:
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)  # ['watermelon', 'banana', 'cherry', 'pineapple']

# Проверка перед обращением по индексу:
if len(fruits) > 10:
    print(fruits[10])
else:
    print("Индекс вне диапазона")


# ============================================
# 2. СРЕЗЫ (SLICING)
# ============================================

"""
Синтаксис среза: sequence[start:stop:step]
- start — начальный индекс (включительно, по умолчанию 0)
- stop — конечный индекс (не включительно, по умолчанию len(sequence))
- step — шаг (по умолчанию 1)
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Базовые срезы:
print(numbers[0:5])   # [0, 1, 2, 3, 4] — с 0 по 4 (5 не включается)
print(numbers[2:7])   # [2, 3, 4, 5, 6] — с 2 по 6
print(numbers[:5])    # [0, 1, 2, 3, 4] — с начала до 4
print(numbers[5:])    # [5, 6, 7, 8, 9] — с 5 до конца
print(numbers[:])     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] — весь список (копия)

# Срезы с шагом:
print(numbers[0:10:2])  # [0, 2, 4, 6, 8] — каждый второй
print(numbers[::2])     # [0, 2, 4, 6, 8] — тоже самое
print(numbers[1::2])    # [1, 3, 5, 7, 9] — нечётные позиции
print(numbers[::3])     # [0, 3, 6, 9] — каждый третий

# Отрицательные индексы в срезах:
print(numbers[-5:])    # [5, 6, 7, 8, 9] — последние 5 элементов
print(numbers[-5:-1])  # [5, 6, 7, 8] — с -5 по -2 (не включая -1)
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6] — всё кроме последних 3

# Отрицательный шаг (обратный порядок):
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] — разворот
print(numbers[8:2:-1]) # [8, 7, 6, 5, 4, 3] — с 8 до 3 в обратном порядке
print(numbers[::-2])   # [9, 7, 5, 3, 1] — каждый второй с конца

# Особые случаи:
print(numbers[5:2])    # [] — пустой список (start > stop)
print(numbers[0:20])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] — обрезается по длине
print(numbers[20:])    # [] — за пределами


# ============================================
# 3. СРЕЗЫ СТРОК
# ============================================

string = "Community university"

# Доступ по индексу:
print(string[0])    # 'C' — первый символ
print(string[4])    # 'u'
print(string[-1])   # 'y' — последний символ
print(string[-2])   # 't'

# Срезы строк:
print(string[0:9])    # 'Community' — первое слово
print(string[10:])    # 'university' — второе слово
print(string[6:12])   # 'ity un'
print(string[3:18:2]) # 'mnt nvri' — с шагом 2
print(string[::4])    # 'Cuyis' — каждый 4-й символ
print(string[::-1])   # 'ytisrevinu ytinummoC' — строка наоборот

# Практические примеры:
email = "user@example.com"
username = email[:email.index('@')]  # 'user'
domain = email[email.index('@')+1:]  # 'example.com'
print(f"Username: {username}, Domain: {domain}")

# Проверка палиндрома:
word = "radar"
is_palindrome = word == word[::-1]
print(f"'{word}' палиндром: {is_palindrome}")  # True


# ============================================
# 4. ТРИ СПОСОБА РАЗВЕРНУТЬ СПИСОК
# ============================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# СПОСОБ 1: Срез с отрицательным шагом (создаёт копию)
reversed_copy = numbers[::-1]
print(f"Срез: {reversed_copy}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Оригинал не изменён: {numbers}")  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# СПОСОБ 2: Метод reverse() (изменяет оригинал)
numbers.reverse()
print(f"reverse(): {numbers}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Восстановим для следующего примера:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# СПОСОБ 3: Функция reversed() (возвращает итератор)
reversed_iterator = reversed(numbers)
print(f"Тип: {type(reversed_iterator)}")  # <class 'list_reverseiterator'>

# Преобразование в список:
reversed_list = list(reversed_iterator)
print(f"reversed(): {reversed_list}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Оригинал не изменён: {numbers}")  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Сравнение способов:
print("\nСравнение способов разворота:")
print(f"1. Срез [::-1]: создаёт копию, оригинал не изменяется")
print(f"2. reverse(): изменяет оригинал, ничего не возвращает")
print(f"3. reversed(): возвращает итератор, оригинал не изменяется")


# ============================================
# 5. ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ СРЕЗОВ
# ============================================

# Присваивание срезу (изменение части списка):
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:3] = [10, 20, 30]  # замена элементов с 1 по 2 на новые
print(numbers)  # [0, 10, 20, 30, 3, 4, 5]

# Удаление среза:
numbers = [0, 1, 2, 3, 4, 5]
del numbers[1:4]  # удаление элементов с 1 по 3
print(numbers)  # [0, 4, 5]

# Вставка через срез:
numbers = [0, 1, 2, 3]
numbers[1:1] = [10, 20]  # вставка на позицию 1
print(numbers)  # [0, 10, 20, 1, 2, 3]

# Копирование списка через срез:
original = [1, 2, 3]
copy_list = original[:]  # создание копии
copy_list[0] = 99
print(f"Оригинал: {original}")  # [1, 2, 3]
print(f"Копия: {copy_list}")  # [99, 2, 3]


# ============================================
# 6. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Извлечение расширения файла:
filename = "document.pdf"
extension = filename[filename.rfind('.'):]
print(f"Расширение: {extension}")  # .pdf

# Разделение строки пополам:
text = "HelloWorld"
mid = len(text) // 2
first_half = text[:mid]
second_half = text[mid:]
print(f"Первая половина: {first_half}, Вторая: {second_half}")

# Получение каждого второго элемента:
data = list(range(20))
even_positions = data[::2]  # элементы с чётными индексами
odd_positions = data[1::2]  # элементы с нечётными индексами
print(f"Чётные позиции: {even_positions}")
print(f"Нечётные позиции: {odd_positions}")

# Циклический сдвиг списка:
numbers = [1, 2, 3, 4, 5]
shift = 2
shifted = numbers[shift:] + numbers[:shift]
print(f"Сдвиг на {shift}: {shifted}")  # [3, 4, 5, 1, 2]