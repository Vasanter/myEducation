"""
СПИСКОВЫЕ ВКЛЮЧЕНИЯ (LIST COMPREHENSIONS) В PYTHON
=====================================================
Списковые включения — компактный и элегантный способ создания списков.
Заменяют циклы for и map() при создании новых списков.

Синтаксис:
    [выражение for элемент in последовательность if условие]

Преимущества:
- Короче и читаемее обычного цикла
- Работает быстрее (оптимизировано в CPython)
- Часто используется в Python-коде
"""

# ============================================
# 1. БАЗОВЫЙ ПРИМЕР
# ============================================

# Квадраты чисел от 0 до 19:
squares = [x ** 2 for x in range(20)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# Эквивалент с обычным циклом:
squares = []
for x in range(20):
    squares.append(x ** 2)
print(squares)


# ============================================
# 2. С УСЛОВИЕМ IF
# ============================================

# Только чётные числа:
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Только положительные числа:
numbers = [-5, 3, -2, 8, -1, 4]
positives = [n for n in numbers if n > 0]
print(positives)  # [3, 8, 4]

# Слова длиннее 3 символов:
words = ["cat", "apple", "dog", "banana"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ['apple', 'banana']


# ============================================
# 3. С ТЕРНАРНЫМ ОПЕРАТОРОМ (IF-ELSE)
# ============================================

# Замена отрицательных на 0:
numbers = [-5, 3, -2, 8, -1, 4]
non_negative = [n if n > 0 else 0 for n in numbers]
print(non_negative)  # [0, 3, 0, 8, 0, 4]

# Классификация чисел:
labels = ["+" if n > 0 else "-" if n < 0 else "0" for n in numbers]
print(labels)  # ['-', '+', '-', '+', '-', '+']


# ============================================
# 4. СЛОВАРНЫЕ ВКЛЮЧЕНИЯ (DICT COMPREHENSION)
# ============================================

# Квадраты чисел:
square_dict = {x: x ** 2 for x in range(11)}
print(square_dict)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Из двух списков:
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# Инверсия словаря:
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}


# ============================================
# 5. МНОЖЕСТВЕННЫЕ ВКЛЮЧЕНИЯ (SET COMPREHENSION)
# ============================================

# Уникальные квадраты:
squares_set = {x ** 2 for x in range(-5, 6)}
print(squares_set)  # {0, 1, 4, 9, 16, 25}

# Уникальные слова:
text = "hello world hello python world"
unique_words = {word for word in text.split()}
print(unique_words)  # {'hello', 'world', 'python'}


# ============================================
# 6. ВЛОЖЕННЫЕ СПИСКОВЫЕ ВКЛЮЧЕНИЯ
# ============================================

# Транспонирование матрицы:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Разворачивание матрицы в плоский список:
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Декартово произведение:
colors = ["red", "green"]
sizes = ["S", "M", "L"]
combinations = [f"{c}-{s}" for c in colors for s in sizes]
print(combinations)
# ['red-S', 'red-M', 'red-L', 'green-S', 'green-M', 'green-L']


# ============================================
# 7. ПРОВЕРКА ИСТИННОСТИ ЭЛЕМЕНТОВ
# ============================================

"""
В Python у каждого объекта есть встроенное логическое значение.
Все «пустые» объекты, нули и None считаются ложью (False),
а заполненные объекты и ненулевые числа — истиной (True).

┌────────────────────┬──────────┐
│  Значение          │  bool()  │
├────────────────────┼──────────┤
│  0, 0.0            │  False   │
│  "", [], {}, ()    │  False   │
│  None              │  False   │
│  False             │  False   │
│  set()             │  False   │
├────────────────────┼──────────┤
│  1, -1, 3.14       │  True    │
│  "hello", [1, 2]   │  True    │
│  {'id': 777}       │  True    │
│  True              │  True    │
└────────────────────┴──────────┘
"""

items = [1.1, False, 18, '', 0, [], {}, {'id': 777}, True, 'hello', 0.0, (), None]

# Фильтрация — оставляем только «истинные» элементы:
list_comp = [item for item in items if item]
print(list_comp)  # [1.1, 18, {'id': 777}, True, 'hello']

# Только «ложные» элементы:
false_items = [item for item in items if not item]
print(false_items)  # [False, '', 0, [], {}, 0.0, (), None]


# ============================================
# 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Очистка данных:
raw = ["  Alice  ", "Bob  ", "", "  ", "Charlie"]
cleaned = [name.strip() for name in raw if name.strip()]
print(cleaned)  # ['Alice', 'Bob', 'Charlie']

# 2. Преобразование температур:
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# 3. Извлечение email из списка словарей:
users = [
    {"name": "Alice", "email": "alice@mail.com"},
    {"name": "Bob", "email": "bob@mail.com"},
    {"name": "Charlie"},
]
emails = [u["email"] for u in users if "email" in u]
print(emails)  # ['alice@mail.com', 'bob@mail.com']

# 4. Фильтрация файлов по расширению:
files = ["doc.txt", "image.jpg", "notes.txt", "photo.png"]
txt_files = [f for f in files if f.endswith(".txt")]
print(txt_files)  # ['doc.txt', 'notes.txt']

# 5. Генерация HTML:
items = ["Home", "About", "Contact"]
html = [f'<li>{item}</li>' for item in items]
print("\n".join(html))


# ============================================
# 9. СРАВНЕНИЕ С ДРУГИМИ КОНСТРУКЦИЯМИ
# ============================================

# --- LIST COMPREHENSION (список) ---
squares_list = [x ** 2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# --- GENERATOR EXPRESSION (генератор) ---
squares_gen = (x ** 2 for x in range(5))
print(squares_gen)  # <generator object>
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# --- SET COMPREHENSION (множество) ---
squares_set = {x ** 2 for x in range(5)}
print(squares_set)  # {0, 1, 4, 9, 16}

# --- DICT COMPREHENSION (словарь) ---
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# ============================================
# 10. ПРОИЗВОДИТЕЛЬНОСТЬ
# ============================================

import timeit

# List comprehension быстрее обычного цикла:
loop_time = timeit.timeit(
    "result = []\nfor i in range(1000):\n    result.append(i ** 2)",
    number=10000
)

comp_time = timeit.timeit(
    "result = [i ** 2 for i in range(1000)]",
    number=10000
)

print(f"Обычный цикл:   {loop_time:.4f} сек")
print(f"Comprehension:  {comp_time:.4f} сек")
print(f"Comprehension быстрее в {loop_time / comp_time:.2f} раз")


# ============================================
# 11. КОГДА ИСПОЛЬЗОВАТЬ
# ============================================

"""
✅ ХОРОШО использовать:
- Для простого преобразования элементов
- Для фильтрации коллекций
- Когда логика умещается в одну строку
- Для создания списков из других коллекций

❌ ПЛОХО использовать:
- Для сложной логики с множеством условий
- Когда есть побочные эффекты (print, запись в файл)
- Для вложенных условий глубиной более 2 уровней
- Когда это ухудшает читаемость

Правило: если comprehension не умещается в одну строку
        или требует комментариев — используйте обычный цикл.
"""

# ❌ Плохо (сложно читать):
# result = [x if x > 0 else -x if x < 0 else 0 for x in data if x is not None and x != ""]

# ✅ Хорошо (простое преобразование):
numbers = [1, -2, 3, -4, 5]
absolute = [abs(n) for n in numbers]
print(absolute)  # [1, 2, 3, 4, 5]


# ============================================
# 12. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  СПИСКОВЫЕ ВКЛЮЧЕНИЯ — ШПАРГАЛКА                         │
├──────────────────────────────────────────────────────────┤
│  СПИСОК:                                                 │
│  [x for x in data]                                       │
│  [x for x in data if условие]                            │
│  [x if условие else y for x in data]                     │
│  [x for x in data for y in other]                        │
├──────────────────────────────────────────────────────────┤
│  СЛОВАРЬ:                                                │
│  {k: v for k, v in items}                                │
│  {k: v for k, v in items if условие}                     │
├──────────────────────────────────────────────────────────┤
│  МНОЖЕСТВО:                                              │
│  {x for x in data}                                       │
│  {x for x in data if условие}                            │
├──────────────────────────────────────────────────────────┤
│  ГЕНЕРАТОР:                                              │
│  (x for x in data)                                       │
├──────────────────────────────────────────────────────────┤
│  СРАВНЕНИЕ:                                              │
│  [ ] — список (в памяти)                                 │
│  ( ) — генератор (ленивый)                               │
│  { } — множество (уникальные)                            │
│  {:} — словарь (пары)                                    │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 13. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Слишком сложная логика
# bad = [x if x > 0 else -x if x < 0 else 0 for x in data if x is not None and x != ""]

# ✅ Решение: обычный цикл
result = []
for x in data:
    if x is not None and x != "":
        result.append(x if x > 0 else -x if x < 0 else 0)


# ❌ Ошибка 2: Побочные эффекты в comprehension
# bad = [print(x) for x in range(5)]  # создаёт список из None!

# ✅ Решение: обычный цикл
for x in range(5):
    print(x)


# ❌ Ошибка 3: Путаница с порядком for
# matrix = [[1, 2], [3, 4]]
# bad = [num for num in row for row in matrix]  # NameError: 'row' не определён

# ✅ Правильно: внешний цикл первый
good = [num for row in matrix for num in row]
print(good)  # [1, 2, 3, 4]


# ❌ Ошибка 4: Изменение исходного списка
# numbers = [1, 2, 3, 4, 5]
# bad = [numbers.remove(n) for n in numbers]  # изменяет список во время итерации!

# ✅ Решение: создать новый список
numbers = [1, 2, 3, 4, 5]
good = [n for n in numbers if n % 2 == 0]
print(good)  # [2, 4]


# ❌ Ошибка 5: Забыли [ ] — получился генератор
# gen = (x ** 2 for x in range(5))
# print(gen)  # <generator object>, а не список

# ✅ Решение:
lst = [x ** 2 for x in range(5)]
print(lst)  # [0, 1, 4, 9, 16]