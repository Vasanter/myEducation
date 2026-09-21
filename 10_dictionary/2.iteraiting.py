"""
ПЕРЕБОР ЭЛЕМЕНТОВ СЛОВАРЯ В PYTHON
=====================================
Словарь можно перебирать тремя способами:
1. По парам (ключ, значение) — items()
2. По ключам — keys()
3. По значениям — values()
"""

# Исходный словарь:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# ============================================
# 1. ПЕРЕБОР ПО ПАРАМ (ключ, значение)
# ============================================

# items() возвращает объект dict_items с кортежами:
for item in person.items():
    print(item)
    print(type(item))
# ('name', 'John')
# <class 'tuple'>
# ('age', 30)
# <class 'tuple'>
# ('city', 'New York')
# <class 'tuple'>

# Распаковка кортежа прямо в цикле (рекомендуется):
for key, value in person.items():
    print(f"{key}: {value}")
# name: John
# age: 30
# city: New York


# ============================================
# 2. ПЕРЕБОР ПО КЛЮЧАМ
# ============================================

# Явное использование keys():
for key in person.keys():
    print(key)
# name
# age
# city

# Неявный перебор (по умолчанию — по ключам):
for key in person:
    print(key)
# name
# age
# city

# Доступ к значению через ключ:
for key in person:
    print(f"{key}: {person[key]}")
# name: John
# age: 30
# city: New York


# ============================================
# 3. ПЕРЕБОР ПО ЗНАЧЕНИЯМ
# ============================================

for value in person.values():
    print(value)
# John
# 30
# New York


# ============================================
# 4. ПЕРЕБОР С ИНДЕКСАМИ
# ============================================

# С enumerate():
for i, (key, value) in enumerate(person.items(), start=1):
    print(f"{i}. {key}: {value}")
# 1. name: John
# 2. age: 30
# 3. city: New York


# ============================================
# 5. СОРТИРОВКА ПРИ ПЕРЕБОРЕ
# ============================================

# По ключам (по алфавиту):
for key in sorted(person.keys()):
    print(f"{key}: {person[key]}")
# age: 30
# city: New York
# name: John

# По значениям:
for key, value in sorted(person.items(), key=lambda x: x[1]):
    print(f"{key}: {value}")


# ============================================
# 6. ФИЛЬТРАЦИЯ ПРИ ПЕРЕБОРЕ
# ============================================

# Только строковые значения:
for key, value in person.items():
    if isinstance(value, str):
        print(f"{key}: {value}")
# name: John
# city: New York

# Только числовые значения:
for key, value in person.items():
    if isinstance(value, (int, float)):
        print(f"{key}: {value}")
# age: 30


# ============================================
# 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Вывод в виде таблицы:
person = {"name": "John", "age": 30, "city": "New York"}
print(f"{'Ключ':<10} | {'Значение':<15}")
print("-" * 30)
for key, value in person.items():
    print(f"{key:<10} | {str(value):<15}")

# 2. Формирование строки:
info = ", ".join(f"{k}={v}" for k, v in person.items())
print(info)  # name=John, age=30, city=New York

# 3. Поиск ключа по значению:
target = 30
for key, value in person.items():
    if value == target:
        print(f"Ключ для {target}: {key}")  # age

# 4. Подсчёт суммы значений:
prices = {"apple": 50, "banana": 30, "cherry": 80}
total = sum(prices.values())
print(f"Итого: {total} руб.")

# 5. Проверка наличия значения:
if "John" in person.values():
    print("John найден!")


# ============================================
# 8. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????
?  ПЕРЕБОР СЛОВАРЯ — ШПАРГАЛКА                         ?
????????????????????????????????????????????????????????
?  ПО КЛЮЧАМ:                                          ?
?  for key in d:                  — неявно             ?
?  for key in d.keys():           — явно               ?
????????????????????????????????????????????????????????
?  ПО ЗНАЧЕНИЯМ:                                       ?
?  for value in d.values():                            ?
????????????????????????????????????????????????????????
?  ПО ПАРАМ:                                           ?
?  for item in d.items():         — кортеж             ?
?  for key, value in d.items():   — распаковка         ?
????????????????????????????????????????????????????????
?  С ИНДЕКСАМИ:                                        ?
?  for i, (k, v) in enumerate(d.items(), 1):           ?
????????????????????????????????????????????????????????
"""