"""
СЛОВАРИ (DICTIONARY / DICT) В PYTHON
=======================================
Словарь — изменяемая структура данных, которая хранит элементы
в виде пар "ключ-значение".

Каждый ключ в словаре должен быть уникальным и неизменяемым.
Ключ используется для доступа к соответствующему значению.
Словари также называют ассоциативными массивами или отображениями.
"""

# ============================================
# 1. СОЗДАНИЕ СЛОВАРЕЙ
# ============================================

# Пустой словарь:
empty = {}
print(empty)  # {}

empty = dict()
print(empty)  # {}

# Словарь с элементами:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# Словарь с разными типами ключей:
mixed = {
    "name": "Alice",      # строка
    42: "ответ",          # число
    (1, 2): "координаты", # кортеж (хешируемый)
    True: "истина"        # булево
}
print(mixed)

# Создание из списка кортежей:
pairs = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(pairs)
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# Создание через dict.fromkeys():
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys)
print(default_dict)  # {'name': None, 'age': None, 'city': None}

# Со значением по умолчанию:
default_dict = dict.fromkeys(keys, "не указано")
print(default_dict)  # {'name': 'не указано', 'age': 'не указано', 'city': 'не указано'}

# Через генератор (dict comprehension):
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# ============================================
# 2. ДОСТУП К ЭЛЕМЕНТАМ
# ============================================

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Через квадратные скобки (KeyError, если ключа нет):
print(person["name"])  # 'John'
# print(person["country"])  # KeyError: 'country'

# Через get() (безопасно):
print(person.get("name"))              # 'John'
print(person.get("country"))           # None — ключа нет
print(person.get("country", "USA"))    # 'USA' — значение по умолчанию
print(person.get("name", "Donny"))     # 'John' — ключ есть

# Проверка наличия ключа:
print("name" in person)      # True
print("country" in person)   # False

# Проверка значений:
print("John" in person.values())  # True

# Получение всех ключей и значений:
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['John', 30, 'New York'])
print(person.items())   # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])


# ============================================
# 3. ДОБАВЛЕНИЕ И ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ
# ============================================

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Добавление нового ключа (в конец):
person["job"] = "Engineer"
print(person)  # {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Изменение существующего значения:
person["age"] = 31
print(person)  # {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Обновление через update():
person.update({"age": 32, "country": "USA"})
print(person)  # age=32, добавлен country

# setdefault() — вернуть значение или создать:
person = {"name": "John"}
result = person.setdefault("age", 25)  # ключа нет → создаёт
print(result)  # 25
print(person)  # {'name': 'John', 'age': 25}

result = person.setdefault("name", "Donny")  # ключ есть → возвращает
print(result)  # 'John'


# ============================================
# 4. УДАЛЕНИЕ ЭЛЕМЕНТОВ
# ============================================

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

# pop() — удалить и вернуть значение:
age = person.pop("age")
print(age)     # 30
print(person)  # без 'age'

# pop() с значением по умолчанию:
country = person.pop("country", "не найдено")
print(country)  # 'не найдено'

# del — удалить ключ:
del person["job"]
print(person)  # без 'job'

# clear() — очистить весь словарь:
# person.clear()
# print(person)  # {}

# popitem() — удалить последний добавленный элемент (Python 3.7+):
person = {"name": "John", "age": 30}
last_item = person.popitem()
print(last_item)  # ('age', 30)


# ============================================
# 5. ПЕРЕБОР ЭЛЕМЕНТОВ
# ============================================

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# По ключам:
for key in person:
    print(key)

for key in person.keys():
    print(key)

# По значениям:
for value in person.values():
    print(value)

# По парам ключ-значение:
for key, value in person.items():
    print(key, value)
# name John
# age 30
# city New York

# С индексами:
for i, (key, value) in enumerate(person.items(), start=1):
    print(f"{i}. {key}: {value}")


# ============================================
# 6. ВЛОЖЕННЫЕ СЛОВАРИ
# ============================================

# Словарь со вложенными структурами:
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "address": {
            "city": "Moscow",
            "zip": "101000"
        }
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "address": {
            "city": "SPb",
            "zip": "190000"
        }
    }
}

# Доступ к вложенным данным:
print(users["user1"]["name"])                # 'Alice'
print(users["user2"]["address"]["city"])     # 'SPb'

# Перебор вложенного словаря:
for user_id, user_data in users.items():
    print(f"\n{user_id}:")
    for key, value in user_data.items():
        print(f"  {key}: {value}")


# ============================================
# 7. ОБЪЕДИНЕНИЕ СЛОВАРЕЙ
# ============================================

# Оператор | (Python 3.9+):
dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}
merged = dict_1 | dict_2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Оператор |= (обновление):
dict_1 |= dict_2
print(dict_1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Через update():
dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}
dict_1.update(dict_2)
print(dict_1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Через распаковку (Python 3.5+):
merged = {**dict_1, **dict_2}
print(merged)

# При конфликте ключей побеждает правый:
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 99, "c": 3}
print({**dict_1, **dict_2})  # {'a': 1, 'b': 99, 'c': 3}


# ============================================
# 8. ГЕНЕРАЦИЯ СЛОВАРЕЙ (DICT COMPREHENSION)
# ============================================

# Квадраты чисел:
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Из двух списков:
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# С условием:
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Инверсия словаря (ключ ↔ значение):
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}


# ============================================
# 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Подсчёт частоты слов:
text = "hello world hello python world hello"
words = text.split()
counter = {}
for word in words:
    counter[word] = counter.get(word, 0) + 1
print(counter)  # {'hello': 3, 'world': 2, 'python': 1}

# Более короткая запись:
from collections import Counter
counter = Counter(words)
print(counter)  # Counter({'hello': 3, 'world': 2, 'python': 1})

# 2. Хранение данных о студентах:
students = {
    "Иванов": {"возраст": 20, "оценки": [5, 4, 5]},
    "Петров": {"возраст": 21, "оценки": [4, 4, 3]},
}

for name, data in students.items():
    avg = sum(data["оценки"]) / len(data["оценки"])
    print(f"{name}: средний балл — {avg:.2f}")

# 3. Конфигурация приложения:
config = {
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}
print(config["database"]["host"])  # localhost

# 4. Инвентарь в игре:
inventory = {
    "яблоко": 5,
    "зелье": 2,
    "меч": 1
}

def use_item(inventory, item):
    """Использовать предмет из инвентаря"""
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        if inventory[item] == 0:
            del inventory[item]
        print(f"Использовано: {item}")
    else:
        print(f"Нет в наличии: {item}")

use_item(inventory, "зелье")
print(inventory)  # {'яблоко': 5, 'зелье': 1, 'меч': 1}


# ============================================
# 10. МЕТОДЫ СЛОВАРЕЙ — ШПАРГАЛКА
# ============================================

"""
┌────────────────────────────────────────────────────────┐
│  МЕТОДЫ СЛОВАРЕЙ — ШПАРГАЛКА                           │
├────────────────────────────────────────────────────────┤
│  ДОСТУП:                                               │
│  d[key]              — доступ (KeyError если нет)      │
│  d.get(key[, def])   — безопасный доступ               │
│  d.keys()            — все ключи                       │
│  d.values()          — все значения                    │
│  d.items()           — пары (ключ, значение)           │
├────────────────────────────────────────────────────────┤
│  ИЗМЕНЕНИЕ:                                            │
│  d[key] = value      — добавить/изменить               │
│  d.update(other)     — обновить словарь                │
│  d.setdefault(k, v)  — вернуть или создать             │
├────────────────────────────────────────────────────────┤
│  УДАЛЕНИЕ:                                             │
│  d.pop(key[, def])   — удалить и вернуть               │
│  d.popitem()         — удалить последнюю пару          │
│  del d[key]          — удалить по ключу                │
│  d.clear()           — очистить словарь                │
├────────────────────────────────────────────────────────┤
│  ОБЪЕДИНЕНИЕ:                                          │
│  d1 | d2             — объединение (Python 3.9+)       │
│  {**d1, **d2}        — распаковка                      │
│  d1.update(d2)       — обновление                      │
└────────────────────────────────────────────────────────┘
"""


# ============================================
# 11. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: KeyError при обращении к несуществующему ключу
person = {"name": "John"}
# print(person["age"])  # KeyError: 'age'

# ✅ Решение: использовать get()
print(person.get("age", "не указано"))  # 'не указано'

# ❌ Ошибка 2: Использование изменяемого ключа
# bad_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# ✅ Решение: использовать неизменяемые типы
good_dict = {(1, 2): "value"}
print(good_dict)  # {(1, 2): 'value'}

# ❌ Ошибка 3: Изменение словаря во время итерации
# person = {"a": 1, "b": 2, "c": 3}
# for key in person:
#     if person[key] == 2:
#         del person[key]  # RuntimeError: dictionary changed size during iteration

# ✅ Решение: создать копию ключей
person = {"a": 1, "b": 2, "c": 3}
for key in list(person.keys()):
    if person[key] == 2:
        del person[key]
print(person)  # {'a': 1, 'c': 3}

# ❌ Ошибка 4: Проверка вхождения значения через in
person = {"name": "John", "age": 30}
print("name" in person)    # True — проверяет КЛЮЧИ!
print("John" in person)    # False — не проверяет значения!

# ✅ Решение: проверять через values()
print("John" in person.values())  # True