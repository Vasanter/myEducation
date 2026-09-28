"""
СПИСКОВЫЕ ВКЛЮЧЕНИЯ (LIST COMPREHENSION) В PYTHON
====================================================
Списковые включения — компактный способ создания списков на основе
существующих последовательностей.

Синтаксис:
    [выражение for элемент in последовательность if условие]

Преимущества:
- Короче и читаемее обычного цикла
- Работает быстрее (оптимизировано в CPython)
- Часто используется в Python-коде
"""

# ============================================
# 1. БАЗОВЫЙ ШАБЛОН
# ============================================

# Простой шаблон без условия:
result = [i for i in range(-5, 14)]
print(result)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Эквивалент с обычным циклом:
result = []
for i in range(-5, 14):
    result.append(i)
print(result)  # тот же результат

# С выражением (преобразованием):
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# С строками:
upper_words = [word.upper() for word in ["hello", "world"]]
print(upper_words)  # ['HELLO', 'WORLD']


# ============================================
# 2. ФИЛЬТРАЦИЯ С УСЛОВИЕМ IF
# ============================================

# ПРИМЕР 1: Удаление нулей из списка
data = [11, 0, 3, 0, 5, 7, 0, 4, 1, 22, 0, 8]
res = [num for num in data if num != 0]
print(res)  # [11, 3, 5, 7, 4, 1, 22, 8]

# Разбор:
# num — переменная, принимающая каждое значение из data
# for num in data — цикл по всем элементам
# if num != 0 — условие фильтрации

# Аналогичный код с обычным циклом:
data = [11, 0, 3, 0, 5, 7, 0, 0, 4, 22, 0]
res = []
for num in data:
    if num != 0:
        res.append(num)
print(res)  # [11, 3, 5, 7, 4, 22]


# ПРИМЕР 2: Фильтрация строк по длине
words = ["apple", "cat", "banana", "dog"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ['apple', 'banana']

# ПРИМЕР 3: Удаление отрицательных чисел
numbers = [1, -2, 3, -4, 5]
positive = [n for n in numbers if n > 0]
print(positive)  # [1, 3, 5]

# ПРИМЕР 4: Фильтрация по типу данных
mixed = [1, "hello", 2.5, "world", 3]
integers = [x for x in mixed if isinstance(x, int)]
print(integers)  # [1, 3]


# ============================================
# 3. ПРЕОБРАЗОВАНИЕ + ФИЛЬТРАЦИЯ
# ============================================

# Квадраты только чётных чисел:
evens_squared = [x ** 2 for x in range(10) if x % 2 == 0]
print(evens_squared)  # [0, 4, 16, 36, 64]

# Длина строк для слов длиннее 3 символов:
words = ["cat", "apple", "dog", "banana"]
lengths = [len(w) for w in words if len(w) > 3]
print(lengths)  # [5, 6]

# Приведение к верхнему регистру слов, начинающихся с гласной:
words = ["apple", "banana", "orange", "grape"]
vowel_words = [w.upper() for w in words if w[0].lower() in "aeiou"]
print(vowel_words)  # ['APPLE', 'ORANGE']


# ============================================
# 4. УСЛОВНОЕ ВЫРАЖЕНИЕ (ТЕРНАРНЫЙ ОПЕРАТОР)
# ============================================

# Синтаксис: [выражение_если_True if условие else выражение_если_False for ...]

# Замена отрицательных на 0:
numbers = [1, -2, 3, -4, 5]
non_negative = [n if n > 0 else 0 for n in numbers]
print(non_negative)  # [1, 0, 3, 0, 5]

# Классификация чисел:
numbers = [-5, -2, 0, 3, 8, -1]
classified = ["+" if n > 0 else "-" if n < 0 else "0" for n in numbers]
print(classified)  # ['-', '-', '0', '+', '+', '-']

# Чётные/нечётные:
labels = ["чёт" if n % 2 == 0 else "нечёт" for n in range(1, 6)]
print(labels)  # ['нечёт', 'чёт', 'нечёт', 'чёт', 'нечёт']


# ============================================
# 5. ВЛОЖЕННЫЕ СПИСКОВЫЕ ВКЛЮЧЕНИЯ
# ============================================

# Матрица (список списков):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Разворачивание матрицы в плоский список:
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Эквивалент с обычным циклом:
flat = []
for row in matrix:
    for num in row:
        flat.append(num)

# Транспонирование матрицы:
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Квадраты чётных чисел из вложенного списка:
nested = [[1, 2], [3, 4], [5, 6]]
evens_sq = [x ** 2 for row in nested for x in row if x % 2 == 0]
print(evens_sq)  # [4, 16, 36]


# ============================================
# 6. РАБОТА СО СТРОКАМИ
# ============================================

text = "Hello World Python"

# Список символов:
chars = [ch for ch in text]
print(chars)  # ['H', 'e', 'l', 'l', 'o', ...]

# Только буквы (без пробелов):
letters = [ch for ch in text if ch != " "]
print(letters)  # ['H', 'e', 'l', 'l', 'o', ...]

# Только гласные:
vowels = [ch for ch in text.lower() if ch in "aeiou"]
print(vowels)  # ['e', 'o', 'o', 'o', 'u']

# Разбиение строки на слова:
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Первые буквы слов:
initials = [w[0] for w in text.split()]
print(initials)  # ['H', 'W', 'P']


# ============================================
# 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Чтение чисел из файла:
# with open("numbers.txt") as f:
#     numbers = [int(line.strip()) for line in f if line.strip()]

# 2. Очистка данных:
raw_data = ["  Alice  ", "Bob  ", "  Charlie", ""]
cleaned = [name.strip() for name in raw_data if name.strip()]
print(cleaned)  # ['Alice', 'Bob', 'Charlie']

# 3. Извлечение email из списка:
users = [
    {"name": "Alice", "email": "alice@mail.com"},
    {"name": "Bob", "email": "bob@mail.com"},
    {"name": "Charlie"},
]
emails = [u["email"] for u in users if "email" in u]
print(emails)  # ['alice@mail.com', 'bob@mail.com']

# 4. Генерация HTML-списка:
items = ["Home", "About", "Contact"]
html = [f'<li>{item}</li>' for item in items]
print("\n".join(html))

# 5. Фильтрация файлов по расширению:
files = ["doc.txt", "image.jpg", "notes.txt", "photo.png"]
txt_files = [f for f in files if f.endswith(".txt")]
print(txt_files)  # ['doc.txt', 'notes.txt']

# 6. Преобразование температур:
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# 7. Декартово произведение:
colors = ["red", "green"]
sizes = ["S", "M", "L"]
combinations = [f"{c}-{s}" for c in colors for s in sizes]
print(combinations)  # ['red-S', 'red-M', 'red-L', 'green-S', 'green-M', 'green-L']


# ============================================
# 8. СРАВНЕНИЕ С ДРУГИМИ КОНСТРУКЦИЯМИ
# ============================================

# LIST COMPREHENSION (список):
squares_list = [x ** 2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# GENERATOR EXPRESSION (генератор):
squares_gen = (x ** 2 for x in range(5))
print(squares_gen)  # <generator object>
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# SET COMPREHENSION (множество):
squares_set = {x ** 2 for x in range(5)}
print(squares_set)  # {0, 1, 4, 9, 16}

# DICT COMPREHENSION (словарь):
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# ============================================
# 9. КОГДА ИСПОЛЬЗОВАТЬ LIST COMPREHENSION
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

# Плохой пример (сложно читать):
# result = [x if x > 0 else -x if x < 0 else 0 for x in data if x is not None and x != ""]

# Хороший пример (простое преобразование):
numbers = [1, -2, 3, -4, 5]
absolute = [abs(n) for n in numbers]
print(absolute)  # [1, 2, 3, 4, 5]


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

print(f"Обычный цикл: {loop_time:.4f} сек")
print(f"Comprehension: {comp_time:.4f} сек")
print(f"Comprehension быстрее в {loop_time / comp_time:.2f} раз")


# ============================================
# 11. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────┐
│  LIST COMPREHENSION — ШПАРГАЛКА                  │
├──────────────────────────────────────────────────┤
│  [выражение for элемент in последовательность]   │
│  [выражение for элемент in последовательность    │
│              if условие]                         │
│  [выражение if условие else выражение            │
│              for элемент in последовательность]  │
├──────────────────────────────────────────────────┤
│  Аналоги для других типов:                       │
│  {x for x in ...}       — множество (set)        │
│  {k: v for ...}         — словарь (dict)         │
│  (x for x in ...)       — генератор              │
└──────────────────────────────────────────────────┘
"""