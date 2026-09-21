"""
РАБОТА С КОЛЛЕКЦИЯМИ: МЕТОДЫ, КОПИРОВАНИЕ, ОБРАБОТКА ДАННЫХ
==============================================================
"""

from copy import copy, deepcopy

# ============================================
# 1. МЕТОДЫ СПИСКОВ: ДОБАВЛЕНИЕ
# ============================================

# append() — добавление в конец (ИЗМЕНЯЕТ список)
fruits = ['apple', 'banana', 'cherry']
fruits.append('watermelon')
print(fruits)  # ['apple', 'banana', 'cherry', 'watermelon']

# insert() — вставка по индексу (ИЗМЕНЯЕТ список)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'watermelon')
print(fruits)  # ['apple', 'watermelon', 'banana', 'cherry']

# extend() — добавление элементов из другого списка
fruits = ['apple', 'banana', 'cherry']
fruits2 = ['fig', 'grape']
fruits.extend(fruits2)
print(fruits)  # ['apple', 'banana', 'cherry', 'fig', 'grape']


# ============================================
# 2. МЕТОДЫ СПИСКОВ: УДАЛЕНИЕ
# ============================================

# pop() — удаление последнего элемента (возвращает его)
fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop()
print(fruit)   # 'cherry'
print(fruits)  # ['apple', 'banana']

# pop(index) — удаление по индексу
fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop(1)
print(fruit)   # 'banana'
print(fruits)  # ['apple', 'cherry']

# remove() — удаление по значению
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # ['apple', 'cherry']

# clear() — очистка всего списка
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # []


# ============================================
# 3. МЕТОДЫ СПИСКОВ: ИЗМЕНЕНИЕ ПОРЯДКА
# ============================================

# reverse() — разворот на месте (ИЗМЕНЯЕТ список)
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']

# sort() — сортировка на месте (ИЗМЕНЯЕТ список)
my_list = [5, 4, 8, 10, 1, 2, 14, 4]
my_list.sort()
print(my_list)  # [1, 2, 4, 4, 5, 8, 10, 14]

my_list.sort(reverse=True)
print(my_list)  # [14, 10, 8, 5, 4, 4, 2, 1]

# sort() с ключом:
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # ['apple', 'banana', 'cherry']


# ============================================
# 4. СТРОКИ: НЕИЗМЕНЯЕМОСТЬ
# ============================================

# Строки НЕ изменяются — методы возвращают новую строку
my_string = "Hello, world! "
new_string = my_string.replace("world", "Python")
print(my_string)   # 'Hello, world! ' — оригинал не изменился
print(new_string)  # 'Hello, Python! ' — новая строка

# split() — разделение строки на список
my_string = "My name is Alex"
print(my_string.split(' '))  # ['My', 'name', 'is', 'Alex']

# join() — объединение списка в строку
my_list = ["My", "name", "is", "Alex"]
joined_string = "+".join(my_list)
print(joined_string)  # 'My+name+is+Alex'


# ============================================
# 5. ФУНКЦИИ ДЛЯ РАБОТЫ С ЧИСЛАМИ
# ============================================

my_list = [5, 4, 8, 10, 1, 2, 14, 4]
print(max(my_list))  # 14
print(min(my_list))  # 1
print(sum(my_list))  # 48
print(sum(my_list) / len(my_list))  # 6.0 — среднее значение

# Ошибка: смешанные типы
my_list = [5, 4, 8, 10, 1, 2, 14, "word"]
# print(sum(my_list))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ✅ Решение: фильтрация чисел
mixed = [5, 4, 8, "word", 1, 2]
numbers_only = [x for x in mixed if isinstance(x, (int, float))]
print(sum(numbers_only))  # 20


# ============================================
# 6. ПРАКТИЧЕСКИЙ ПРИМЕР: УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ
# ============================================

nums = [1, 5, 8, 2, 9, 3, 4, 7, 5, 6, 2, 9, 1, 8, 4, 3, 8]

# Способ 1: Через цикл
unique_nums = []
for i in nums:
    if i not in unique_nums:
        unique_nums.append(i)
print(unique_nums)  # [1, 5, 8, 2, 9, 3, 4, 7, 6]
print(sorted(unique_nums))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Способ 2: Через set (быстрее, но теряет порядок)
unique_set = list(set(nums))
print(sorted(unique_set))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Способ 3: С сохранением порядка (Python 3.7+)
unique_ordered = list(dict.fromkeys(nums))
print(unique_ordered)  # [1, 5, 8, 2, 9, 3, 4, 7, 6]


# ============================================
# 7. РУЧНОЙ ВВОД СПИСКА
# ============================================

# Ввод чисел через пробел:
test = list(map(int, input("Введите числа через пробел: ").split()))
print(test)

# Ввод строк:
names = input("Введите имена через запятую: ").split(",")
print(names)

# Ввод с обработкой ошибок:
def get_numbers():
    """Безопасный ввод списка чисел"""
    while True:
        try:
            return list(map(int, input("Введите числа через пробел: ").split()))
        except ValueError:
            print("Ошибка! Введите только числа.")


# ============================================
# 8. КОПИРОВАНИЕ ОБЪЕКТОВ
# ============================================

"""
⚠️ ВАЖНО: Присваивание НЕ создаёт копию!

list_1 = [1, 2, 3]
list_2 = list_1       # Обе переменные ссылаются на ОДИН объект!
list_2.append(4)
print(list_1)         # [1, 2, 3, 4] — оригинал изменился!
"""

# --- ПОВЕРХНОСТНАЯ КОПИЯ (shallow copy) ---
# Копирует только верхний уровень контейнера.
# Вложенные объекты остаются общими!

original = [[1, 2], [3, 4]]
shallow = copy(original)

# Изменяем вложенный список:
shallow[0][0] = 99
print(f"Оригинал: {original}")  # [[99, 2], [3, 4]] — ИЗМЕНИЛСЯ!
print(f"Копия:    {shallow}")   # [[99, 2], [3, 4]]

# Но замена верхнего уровня не влияет:
shallow[1] = [7, 8]
print(f"Оригинал: {original}")  # [[99, 2], [3, 4]] — не изменился
print(f"Копия:    {shallow}")   # [[99, 2], [7, 8]]


# --- ГЛУБОКАЯ КОПИЯ (deep copy) ---
# Рекурсивно копирует ВСЕ уровни вложенности.
# Полностью независимая копия!

original = [[1, 2], [3, 4]]
deep = deepcopy(original)

# Изменяем вложенный список:
deep[0][0] = 88
print(f"Оригинал: {original}")  # [[1, 2], [3, 4]] — НЕ изменился!
print(f"Копия:    {deep}")      # [[88, 2], [3, 4]]


# ============================================
# 9. СРАВНЕНИЕ СПОСОБОВ КОПИРОВАНИЯ
# ============================================

"""
┌────────────────────┬──────────────────┬──────────────────┐
│  Способ            │  Верхний уровень │  Вложенные       │
├────────────────────┼──────────────────┼──────────────────┤
│  = (присваивание)  │  Общий объект    │  Общие объекты   │
│  copy()            │  Копия           │  Общие объекты   │
│  deepcopy()        │  Копия           │  Копии           │
│  list[:]           │  Копия           │  Общие объекты   │
│  list.copy()       │  Копия           │  Общие объекты   │
└────────────────────┴──────────────────┴──────────────────┘
"""

# Демонстрация:
import copy

original = [1, [2, 3], 4]

# Присваивание:
assigned = original
assigned[1][0] = 99
print(f"После присваивания: {original}")  # [1, [99, 3], 4]

# Восстановим:
original = [1, [2, 3], 4]

# Поверхностная копия:
shallow = copy.copy(original)
shallow[1][0] = 99
print(f"После copy():       {original}")  # [1, [99, 3], 4] — изменился!

# Восстановим:
original = [1, [2, 3], 4]

# Глубокая копия:
deep = copy.deepcopy(original)
deep[1][0] = 99
print(f"После deepcopy():   {original}")  # [1, [2, 3], 4] — НЕ изменился!


# ============================================
# 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Безопасное копирование конфигурации:
config = {
    "database": {"host": "localhost", "port": 5432},
    "debug": True
}

# Глубокая копия для изменения:
new_config = deepcopy(config)
new_config["database"]["host"] = "production.server"
print(f"Оригинал: {config['database']['host']}")     # localhost
print(f"Копия:    {new_config['database']['host']}")  # production.server

# 2. Создание снимка состояния:
game_state = {
    "player": {"hp": 100, "inventory": ["sword", "potion"]},
    "level": 5
}
snapshot = deepcopy(game_state)
game_state["player"]["hp"] = 50
game_state["player"]["inventory"].append("shield")
print(f"Снимок: {snapshot}")  # Оригинальное состояние сохранено

# 3. Копирование матрицы:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Неправильно (все строки — один объект):
wrong_copy = [row for row in matrix]
wrong_copy[0][0] = 99
print(f"Матрица после wrong_copy: {matrix}")  # [[99, 2, 3], ...] — изменилась!

# Правильно (глубокая копия):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
right_copy = deepcopy(matrix)
right_copy[0][0] = 99
print(f"Матрица после deepcopy: {matrix}")  # [[1, 2, 3], ...] — не изменилась!


# ============================================
# 11. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────┐
│  КОПИРОВАНИЕ ОБЪЕКТОВ — ШПАРГАЛКА                    │
├──────────────────────────────────────────────────────┤
│  ПРИСВАИВАНИЕ (=):                                   │
│  Обе переменные ссылаются на один объект             │
│  list_2 = list_1                                     │
├──────────────────────────────────────────────────────┤
│  ПОВЕРХНОСТНАЯ КОПИЯ (shallow):                      │
│  Копирует верхний уровень, вложенные — общие         │
│  copy.copy(obj)                                      │
│  list.copy()                                         │
│  list[:]                                             │
│  dict.copy()                                         │
├──────────────────────────────────────────────────────┤
│  ГЛУБОКАЯ КОПИЯ (deep):                              │
│  Полностью независимая копия всех уровней            │
│  copy.deepcopy(obj)                                  │
├──────────────────────────────────────────────────────┤
│  КОГДА ИСПОЛЬЗОВАТЬ:                                 │
│  =          — когда нужна ссылка на тот же объект    │
│  copy()     — для плоских структур (без вложенности) │
│  deepcopy() — для вложенных структур (списки в списке│
│               словари в словаре, и т.д.)             │
└──────────────────────────────────────────────────────┘
"""


# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Думать, что присваивание создаёт копию
list_1 = [1, 2, 3]
list_2 = list_1
list_2.append(4)
print(f"list_1: {list_1}")  # [1, 2, 3, 4] — изменился!

# ✅ Решение:
list_1 = [1, 2, 3]
list_2 = list_1.copy()
list_2.append(4)
print(f"list_1: {list_1}")  # [1, 2, 3] — не изменился

# ❌ Ошибка 2: Использование copy() для вложенных структур
original = [[1, 2], [3, 4]]
shallow = copy(original)
shallow[0].append(99)
print(f"Оригинал: {original}")  # [[1, 2, 99], [3, 4]] — изменился!

# ✅ Решение:
original = [[1, 2], [3, 4]]
deep = deepcopy(original)
deep[0].append(99)
print(f"Оригинал: {original}")  # [[1, 2], [3, 4]] — не изменился