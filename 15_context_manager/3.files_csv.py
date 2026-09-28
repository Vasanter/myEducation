"""
РАБОТА С CSV В PYTHON
=======================
CSV (Comma-Separated Values) — текстовый формат для табличных данных.
Модуль csv предоставляет инструменты для чтения и записи CSV-файлов.
"""

import csv

FILE_PATH = r'/15_context_manager\persons.csv'


# ============================================
# 1. БАЗОВЫЙ ПРИМЕР (как в исходном коде)
# ============================================

# --- ЗАПИСЬ ЧЕРЕЗ writer() ---
rows = [
    ['name', 'age', 'occupation'],
    ['John', 28, 'Engineer'],
    ['Marie', 22, 'Designer'],
    ['Mike', 32, 'Doctor']
]

file = open(FILE_PATH, 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(file)
csv_writer.writerows(rows)
file.close()

# --- ЧТЕНИЕ ЧЕРЕЗ DictReader() ---
file = open(FILE_PATH, 'r', newline='', encoding='utf-8')
csv_dict_reader = csv.DictReader(file)
for row in csv_dict_reader:
    print(row['name'], row['age'], row['occupation'])
file.close()
# John 28 Engineer
# Marie 22 Designer
# Mike 32 Doctor

# --- ДОБАВЛЕНИЕ ЧЕРЕЗ DictWriter() ---
file = open(FILE_PATH, 'a', newline='', encoding='utf-8')
persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]
fields = ['name', 'age', 'occupation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)
file.close()


# ============================================
# 2. УЛУЧШЕННАЯ ВЕРСИЯ С WITH И ENCODING
# ============================================

# --- ЗАПИСЬ ---
rows = [
    ['name', 'age', 'occupation'],
    ['John', 28, 'Engineer'],
    ['Marie', 22, 'Designer'],
    ['Mike', 32, 'Doctor']
]

with open(FILE_PATH, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(rows)

# --- ЧТЕНИЕ ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row['name'], row['age'], row['occupation'])

# --- ДОБАВЛЕНИЕ ---
persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]
fields = ['name', 'age', 'occupation']

with open(FILE_PATH, 'a', newline='', encoding='utf-8') as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
    csv_dict_writer.writerows(persons)


# ============================================
# 3. ЧТО УЛУЧШЕНО И ПОЧЕМУ
# ============================================

"""
┌──────────────────────────────┬──────────────────────────────────────┐
│  Было                        │  Стало                               │
├──────────────────────────────┼──────────────────────────────────────┤
│  file = open(...)            │  with open(...) as file:             │
│  file.close()                │  (автоматическое закрытие)           │
├──────────────────────────────┼──────────────────────────────────────┤
│  open(..., 'w')              │  open(..., 'w', newline='',          │
│                              │       encoding='utf-8')              │
├──────────────────────────────┼──────────────────────────────────────┤
│  без newline=''              │  с newline='' —                       │
│                              │  избегает пустых строк в Windows     │
└──────────────────────────────┴──────────────────────────────────────┘
"""


# ============================================
# 4. CSV.WRITER — ЗАПИСЬ СПИСКОВ
# ============================================

# --- writerow() — одна строка ---
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])       # заголовок
    writer.writerow(['Alice', 30])         # данные

# --- writerows() — несколько строк ---
data = [
    ['Bob', 25],
    ['Charlie', 35]
]
with open('output.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# --- С разделителем ---
with open('output.tsv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')  # табуляция
    writer.writerows([['a', 'b'], ['c', 'd']])

# --- С кавычками ---
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # все значения в кавычках
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])
# "name","age"
# "Alice","30"


# ============================================
# 5. CSV.READER — ЧТЕНИЕ
# ============================================

# --- reader() — список строк ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'age', 'occupation']
# ['John', '28', 'Engineer']
# ['Marie', '22', 'Designer']

# --- Пропуск заголовка ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # пропустить заголовок
    for row in reader:
        print(row)

# --- Чтение в список ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)


# ============================================
# 6. CSV.DICTREADER — ЧТЕНИЕ ПО КЛЮЧАМ
# ============================================

with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'name': 'John', 'age': '28', 'occupation': 'Engineer'}
# {'name': 'Marie', 'age': '22', 'occupation': 'Designer'}
# {'name': 'Mike', 'age': '32', 'occupation': 'Doctor'}

# ⚠️ Все значения — строки! Нужно преобразовывать:
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row['age'])  # преобразование в int
        print(f"{row['name']}: {age} лет")

# --- С доступом по индексу ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# --- Получить заголовки ---
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)  # ['name', 'age', 'occupation']


# ============================================
# 7. CSV.DICTWRITER — ЗАПИСЬ СЛОВАРЕЙ
# ============================================

persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]
fields = ['name', 'age', 'occupation']

# --- writerows() — несколько словарей ---
with open('new.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()       # записать заголовок
    writer.writerows(persons)  # записать данные

# --- writerow() — один словарь ---
with open('new.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writerow({'name': 'Sophia', 'age': 28, 'occupation': 'Teacher'})

# --- С extraaction для лишних полей ---
persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist', 'city': 'Moscow'}
]
fields = ['name', 'age', 'occupation']

with open('new.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
    writer.writerow(persons[0])  # поле 'city' будет проигнорировано


# ============================================
# 8. БЕЗОПАСНАЯ РАБОТА С CSV
# ============================================

def save_csv(filename: str, rows: list) -> bool:
    """Безопасная запись CSV"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"✅ Сохранено в {filename}")
        return True
    except OSError as e:
        print(f"❌ Ошибка записи: {e}")
    return False


def load_csv(filename: str) -> list:
    """Безопасное чтение CSV"""
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден")
    except csv.Error as e:
        print(f"❌ Ошибка CSV: {e}")
    return []


# Использование:
save_csv('users.csv', [['name', 'age'], ['Alice', 30]])
users = load_csv('users.csv')
for user in users:
    print(user)


# ============================================
# 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Чтение с преобразованием типов:
def load_persons(filename: str) -> list[dict]:
    """Загружает CSV с правильными типами"""
    result = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                result.append({
                    'name': row['name'],
                    'age': int(row['age']),
                    'occupation': row['occupation']
                })
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    return result


persons = load_persons(FILE_PATH)
for p in persons:
    print(f"{p['name']} ({p['age']}) — {p['occupation']}")


# 2. Фильтрация при чтении:
with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    adults = [row for row in reader if int(row['age']) >= 30]
print(adults)


# 3. Запись с сортировкой:
persons = load_persons(FILE_PATH)
persons_sorted = sorted(persons, key=lambda p: p['age'])

with open('sorted.csv', 'w', newline='', encoding='utf-8') as f:
    fields = ['name', 'age', 'occupation']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(persons_sorted)


# 4. Обновление записи:
def update_person(filename: str, name: str, **updates):
    """Обновляет данные человека в CSV"""
    persons = load_persons(filename)
    for p in persons:
        if p['name'] == name:
            p.update(updates)

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'occupation'])
        writer.writeheader()
        writer.writerows(persons)


# update_person(FILE_PATH, 'John', age=29)


# ============================================
# 10. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  CSV В PYTHON — ШПАРГАЛКА                                │
├──────────────────────────────────────────────────────────┤
│  ЗАПИСЬ СПИСКОВ:                                         │
│  writer = csv.writer(f)                                  │
│  writer.writerow([...])     — одна строка                │
│  writer.writerows([[...]])  — несколько строк            │
├──────────────────────────────────────────────────────────┤
│  ЗАПИСЬ СЛОВАРЕЙ:                                        │
│  writer = csv.DictWriter(f, fieldnames=[...])            │
│  writer.writeheader()       — заголовок                  │
│  writer.writerow({...})     — один словарь               │
│  writer.writerows([{...}])  — несколько словарей         │
├──────────────────────────────────────────────────────────┤
│  ЧТЕНИЕ СПИСКОВ:                                         │
│  reader = csv.reader(f)                                  │
│  for row in reader: ...     — row это список             │
├──────────────────────────────────────────────────────────┤
│  ЧТЕНИЕ СЛОВАРЕЙ:                                        │
│  reader = csv.DictReader(f)                              │
│  for row in reader: ...     — row это словарь            │
│  reader.fieldnames          — заголовки                  │
├──────────────────────────────────────────────────────────┤
│  ВАЖНО:                                                  │
│  • Всегда newline='' — иначе пустые строки в Windows     │
│  • Всегда encoding='utf-8' — для кириллицы               │
│  • Значения в DictReader — ВСЕГДА строки!                │
│  • Используйте with для авто-закрытия                    │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 11. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Забыли newline=''
# with open('file.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['a', 'b'])
# # В Windows между строками будут пустые строки!

# ✅ Решение:
with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b'])


# ❌ Ошибка 2: Забыли encoding
# with open('file.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Имя', 'Возраст'])

# ✅ Решение:
with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Имя', 'Возраст'])


# ❌ Ошибка 3: Ожидание int в DictReader
# with open('file.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['age'] + 1)  # TypeError: str + int

# ✅ Решение: преобразовать
with open('file.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(int(row['age']) + 1)


# ❌ Ошибка 4: Забыли writeheader() в DictWriter
# with open('file.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=['name', 'age'])
#     writer.writerow({'name': 'Alice', 'age': 30})  # заголовка нет

# ✅ Решение:
with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30})


# ❌ Ошибка 5: Лишние поля в DictWriter
# with open('file.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=['name', 'age'])
#     writer.writerow({'name': 'Alice', 'age': 30, 'city': 'Moscow'})
# # ValueError: dict contains fields not in fieldnames

# ✅ Решение 1: Указать все поля
with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'Moscow'})

# ✅ Решение 2: Игнорировать лишние
with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'],
                            extrasaction='ignore')
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'Moscow'})


# ❌ Ошибка 6: Открытие с 'a' без newline=''
# with open('file.csv', 'a', encoding='utf-8') as f:  # без newline
#     writer = csv.writer(f)
#     writer.writerow(['новые', 'данные'])

# ✅ Решение:
with open('file.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['новые', 'данные'])