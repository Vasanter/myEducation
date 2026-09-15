"""
СПИСКИ (LIST) В PYTHON
========================
Список — упорядоченная изменяемая коллекция элементов.
Элементы могут быть любого типа: числа, строки, объекты, другие списки.

Основные свойства:
- Упорядоченность: элементы хранятся в определённом порядке (индексация с 0)
- Изменяемость: можно изменять, добавлять и удалять элементы
- Гибкость: могут содержать элементы разных типов
"""

# ============================================
# 1. СОЗДАНИЕ СПИСКОВ
# ============================================

# Пустой список:
my_list = list()
print(my_list)  # []

empty = []
print(empty)  # []

# Создание из строки:
word = "Hello"
chars = list(word)
print(chars)  # ['H', 'e', 'l', 'l', 'o']

# Создание из диапазона:
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# Создание с элементами:
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # ['apple', 'banana', 'cherry']

# Создание из переменных:
element_1 = "apple"
element_2 = "banana"
element_3 = "cherry"
my_list = [element_1, element_2, element_3]
print(my_list)  # ['apple', 'banana', 'cherry']

# Список с разными типами:
mixed = [1, "apple", True, 1.5, [1, 2, 3]]
print(mixed)  # [1, 'apple', True, 1.5, [1, 2, 3]]
# ⚠️ Лучше не смешивать типы в одном списке!


# ============================================
# 2. ПРОВЕРКА СПИСКА
# ============================================

# Булево значение списка:
print(bool([]))  # False — пустой список
print(bool([0]))  # True — есть элементы (даже если это 0)
print(bool([""]))  # True — есть элемент (пустая строка)

# Проверка длины:
fruits = ['apple', 'banana', 'cherry']
print(len(fruits))  # 3

# Проверка наличия элемента:
print('banana' in fruits)  # True
print('watermelon' in fruits)  # False
print(1.5 in mixed)  # True
print("banana" in mixed)  # False

# ============================================
# 3. СРАВНЕНИЕ СПИСКОВ
# ============================================

# Сравнение по значениям (порядок важен!):
list_1 = [1, 2, 3]
list_2 = [1, 3, 2]
list_3 = [1, 2, 3]

print(list_1 == list_2)  # False — порядок разный
print(list_1 == list_3)  # True — значения и порядок совпадают

# Сравнение по длине:
print([1, 2] < [1, 2, 3])  # True — первый список короче

# Сравнение поэлементно:
print([1, 2, 3] < [1, 2, 4])  # True — 3 < 4

# ============================================
# 4. ОБЪЕДИНЕНИЕ СПИСКОВ
# ============================================

# Оператор + (создаёт новый список):
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)  # [1, 2, 3, 4, 5, 6]

# Оператор += (изменяет существующий):
list_1 += list_2
print(list_1)  # [1, 2, 3, 4, 5, 6]

# Оператор * (повторение):
print([0] * 5)  # [0, 0, 0, 0, 0]
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]

# Метод extend() (изменяет существующий):
list_1 = [1, 2]
list_1.extend([3, 4])
print(list_1)  # [1, 2, 3, 4]

# ============================================
# 5. ГЕНЕРАЦИЯ СПИСКОВ (LIST COMPREHENSION)
# ============================================

# Квадраты чисел:
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Чётные числа:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Преобразование строк:
words = ["hello", "world"]
upper = [w.upper() for w in words]
print(upper)  # ['HELLO', 'WORLD']

# Вложенные списки:
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# ============================================
# 6. ОСНОВНЫЕ МЕТОДЫ СПИСКОВ
# ============================================

fruits = ['apple', 'banana', 'cherry']

# --- ДОБАВЛЕНИЕ ---
fruits.append('date')  # добавить в конец
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

fruits.insert(1, 'apricot')  # вставить по индексу
print(fruits)  # ['apple', 'apricot', 'banana', 'cherry', 'date']

fruits.extend(['fig', 'grape'])  # добавить несколько
print(fruits)  # ['apple', 'apricot', 'banana', 'cherry', 'date', 'fig', 'grape']

# --- УДАЛЕНИЕ ---
fruits.remove('banana')  # удалить по значению (первое вхождение)
print(fruits)

popped = fruits.pop()  # удалить и вернуть последний
print(popped)  # 'grape'
print(fruits)

popped = fruits.pop(0)  # удалить и вернуть по индексу
print(popped)  # 'apple'

del fruits[0]  # удалить по индексу
print(fruits)

# fruits.clear()              # очистить весь список

# --- ПОИСК ---
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.index('banana'))  # 1 — первый индекс
print(fruits.count('banana'))  # 2 — количество вхождений

# --- СОРТИРОВКА ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # сортировка на месте (изменяет список)
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # обратная сортировка
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Сортировка по ключу:
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # ['apple', 'banana', 'cherry']

# --- РАЗВОРОТ ---
numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # разворот на месте
print(numbers)  # [5, 4, 3, 2, 1]

# --- КОПИРОВАНИЕ ---
original = [1, 2, 3]
copy_list = original.copy()  # поверхностная копия
copy_list[0] = 99
print(original)  # [1, 2, 3] — оригинал не изменился
print(copy_list)  # [99, 2, 3]

# ============================================
# 7. ИНДЕКСАЦИЯ И СРЕЗЫ
# ============================================

fruits = ['apple', 'banana', 'cherry', 'watermelon']

# Доступ по индексу:
print(fruits[0])  # 'apple'
print(fruits[-1])  # 'watermelon'

# Срезы:
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])  # ['apple', 'banana']
print(fruits[2:])  # ['cherry', 'watermelon']
print(fruits[::-1])  # ['watermelon', 'cherry', 'banana', 'apple']

# Изменение через срез:
fruits[1:3] = ['grape', 'kiwi']
print(fruits)  # ['apple', 'grape', 'kiwi', 'watermelon']

# ============================================
# 8. ПЕРЕБОР ЭЛЕМЕНТОВ
# ============================================

fruits = ['apple', 'banana', 'cherry']

# Простой перебор:
for fruit in fruits:
    print(fruit)

# С индексами:
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# С enumerate (рекомендуется):
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# С enumerate и start:
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# ============================================
# 9. ВЛОЖЕННЫЕ СПИСКИ
# ============================================

# Матрица 3x3:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Доступ к элементам:
print(matrix[0])  # [1, 2, 3] — первая строка
print(matrix[1][2])  # 6 — элемент второй строки, третий столбец
print(matrix[-1][-1])  # 9 — последний элемент

# Перебор матрицы:
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()

# Транспонирование:
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# ============================================
# 10. ЧАСТЫЕ ОПЕРАЦИИ
# ============================================

# Сумма, минимум, максимум:
numbers = [4, 2, 9, 5, 1]
print(sum(numbers))  # 21
print(min(numbers))  # 1
print(max(numbers))  # 9

# Преобразование в другие типы:
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 2, 3]))  # {1, 2, 3}
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']

# Объединение строк:
words = ["Hello", "World"]
print(" ".join(words))  # "Hello World"

# Разбиение строки на список:
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']

# ============================================
# 11. ШПАРГАЛКА ПО МЕТОДАМ
# ============================================

"""
┌──────────────────────────────────────────────────────┐
│  МЕТОДЫ СПИСКОВ — ШПАРГАЛКА                          │
├──────────────────────────────────────────────────────┤
│  ДОБАВЛЕНИЕ:                                         │
│  append(x)      — добавить в конец                   │
│  insert(i, x)   — вставить по индексу                │
│  extend(seq)    — добавить все элементы              │
├──────────────────────────────────────────────────────┤
│  УДАЛЕНИЕ:                                           │
│  remove(x)      — удалить по значению                │
│  pop([i])       — удалить и вернуть элемент          │
│  del list[i]    — удалить по индексу                 │
│  clear()        — очистить список                    │
├──────────────────────────────────────────────────────┤
│  ПОИСК:                                              │
│  index(x)       — индекс первого вхождения           │
│  count(x)       — количество вхождений               │
├──────────────────────────────────────────────────────┤
│  СОРТИРОВКА/РАЗВОРОТ:                                │
│  sort()         — сортировка на месте                │
│  reverse()      — разворот на месте                  │
│  sorted(list)   — вернуть новый отсортированный      │
│  reversed(list) — вернуть итератор в обратном порядке│
├──────────────────────────────────────────────────────┤
│  КОПИРОВАНИЕ:                                        │
│  copy()         — поверхностная копия                │
│  list[:]        — копия через срез                   │
└──────────────────────────────────────────────────────┘
"""

# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Изменение списка во время итерации
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     if n % 2 == 0:
#         numbers.remove(n)  # пропустит некоторые элементы!

# ✅ Решение: создать новый список
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)  # [1, 3, 5]

# ❌ Ошибка 2: Копирование через присваивание (обе переменные ссылаются на один объект)
list_1 = [1, 2, 3]
list_2 = list_1  # НЕ копия!
list_2.append(4)
print(list_1)  # [1, 2, 3, 4] — изменился и оригинал!

# ✅ Решение: использовать copy() или срез
list_1 = [1, 2, 3]
list_2 = list_1.copy()  # или list_1[:]
list_2.append(4)
print(list_1)  # [1, 2, 3] — оригинал не изменился
print(list_2)  # [1, 2, 3, 4]

# ❌ Ошибка 3: sort() возвращает None
numbers = [3, 1, 2]
# result = numbers.sort()  # result = None!
# print(result)  # None

# ✅ Решение: sort() изменяет на месте, sorted() возвращает новый
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]

# Или:
result = sorted([3, 1, 2])
print(result)  # [1, 2, 3]
