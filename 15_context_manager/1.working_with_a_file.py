"""
РАБОТА С ФАЙЛАМИ В PYTHON
============================
Для работы с файлами используются:
- open() — открытие файла
- .read() / .write() — операции чтения/записи
- .close() — закрытие (лучше использовать with)

Лучший способ — with open(...) as f: (автоматическое закрытие).
Для кириллицы обязательно указывать encoding='utf-8'.
"""

import os
import shutil


# ============================================
# 1. ОСНОВНЫЕ ШАГИ РАБОТЫ С ФАЙЛАМИ
# ============================================

"""
1. Открытие:   open('filename.txt', 'режим')
2. Операции:   .read(), .readline(), .readlines() — чтение
               .write() — запись
3. Закрытие:   .close() — или использовать with (рекомендуется)
"""


# ============================================
# 2. РЕЖИМЫ ОТКРЫТИЯ ФАЙЛОВ
# ============================================

"""
┌──────┬────────────────────────────────────────────────────────┐
│ Режим│ Описание                                               │
├──────┼────────────────────────────────────────────────────────┤
│ 'r'  │ Чтение (по умолчанию). Ошибка, если файла нет          │
│ 'w'  │ Запись. Создаёт файл, удаляет старое содержимое        │
│ 'a'  │ Добавление (append) в конец файла                      │
│ 'x'  │ Создание нового файла. Ошибка, если файл существует    │
│ 'b'  │ Бинарный режим (для изображений и т.д.)                │
│ '+'  │ Чтение и запись одновременно                           │
└──────┴────────────────────────────────────────────────────────┘

Комбинации: 'rb', 'wb', 'ab', 'r+', 'w+', 'a+'
"""


# ============================================
# 3. ЗАПИСЬ, ДОБАВЛЕНИЕ И ЧТЕНИЕ ФАЙЛА
# ============================================

# 1. Создаём файл записью (если его нет):
with open('persons.csv', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!\n")
    f.write("Это новая строка.")

# 2. Добавляем ещё текст:
with open('persons.csv', 'a', encoding='utf-8') as f:
    f.write("\nДобавлено позже.")

# 3. Читаем содержимое:
with open('persons.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Содержимое файла:")
    print(content)
# Привет, мир!
# Это новая строка.
# Добавлено позже.


# ============================================
# 4. СПОСОБЫ ЧТЕНИЯ ФАЙЛА
# ============================================

# --- read() — весь файл одной строкой ---
with open('persons.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)


# --- readline() — одна строка за раз ---
with open('persons.csv', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()


# --- readlines() — список строк ---
with open('persons.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())


# --- Итерация по файлу (рекомендуется для больших файлов) ---
with open('persons.csv', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())


# ============================================
# 5. БЕЗ WITH (ручное управление)
# ============================================

# ⚠️ Не рекомендуется, но важно знать:

# Чтение:
file = open(file='message.txt', mode='r', encoding='utf-8')
print(file.read())        # весь файл
print(file.readline())    # первая строка
file.close()              # обязательно закрыть!

# Перезапись:
file = open(file='message.txt', mode='w', encoding='utf-8')
file.write('Hello World Man')
file.close()

# Добавление:
file = open(file='message.txt', mode='a', encoding='utf-8')
file.write('\nAPPEND TEXT')
file.close()


# ============================================
# 6. ДОПОЛНИТЕЛЬНЫЕ ДЕЙСТВИЯ (os, shutil)
# ============================================

# Проверка существования:
print(os.path.exists('persons.csv'))  # True

# Удаление файла:
if os.path.exists('temp.txt'):
    os.remove('temp.txt')

# Переименование:
os.rename('old_name.txt', 'new_name.txt')

# Перемещение (через shutil):
shutil.move('src/file.txt', 'dst/file.txt')

# Копирование:
shutil.copy('src/file.txt', 'dst/file.txt')

# Информация о файле:
print(os.path.getsize('persons.csv'))   # размер в байтах
print(os.path.abspath('persons.csv'))   # абсолютный путь


# ============================================
# ЗАДАНИЕ 1: ЧТЕНИЕ ФАЙЛА ПОСТРОЧНО
# ============================================

# Создаём файл:
with open('data.txt', 'w', encoding='utf-8') as file:
    file.write("Милан\n")
    file.write("Интер\n")
    file.write("Лацио")

# Читаем построчно:
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
# Милан
# Интер
# Лацио

# ✅ Исправление: в исходном коде было enumerate(file) — это даёт кортеж (индекс, строка).
# Правильно: for line in file — просто строки.


# Через enumerate для нумерации:
with open('data.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")
# 1. Милан
# 2. Интер
# 3. Лацио


# ============================================
# ЗАДАНИЕ 2: ЗАПИСЬ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
# ============================================

while True:
    name = input("Enter your name (или 'stop' для выхода): ")
    if name == 'stop':
        break
    age = input("Enter your age: ")
    user_info = f'{name}: {age}\n'
    with open('userinfo.txt', 'a', encoding='utf-8') as file:
        file.write(user_info)

print("Данные сохранены в userinfo.txt")


# ============================================
# ЗАДАНИЕ 3: КОПИРОВАНИЕ ФАЙЛА
# ============================================

# Создаём исходный файл:
with open('original.txt', 'w', encoding='utf-8') as file:
    file.write('Это содержимое исходного файла.\nЗдесь что-то написано.')

# Открываем оба файла сразу (рекомендуемый способ):
with open('original.txt', 'r', encoding='utf-8') as src, \
     open('copy.txt', 'w', encoding='utf-8') as dst:
    content = src.read()  # читаем всё из первого
    dst.write(content)    # записываем во второй

print("Файл успешно скопирован!")

# Альтернатива — через shutil:
shutil.copy('original.txt', 'copy.txt')


# ============================================
# 7. ПОЛЕЗНЫЕ ПРИЁМЫ
# ============================================

# 1. Проверка существования файла перед открытием:
from pathlib import Path

file_path = Path('data.txt')
if file_path.exists():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
else:
    print("Файл не найден")


# 2. Безопасное чтение с обработкой ошибок:
def read_file_safe(filename: str) -> str | None:
    """Безопасное чтение файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден")
    except PermissionError:
        print(f"❌ Нет доступа к {filename}")
    except UnicodeDecodeError:
        print(f"❌ Ошибка кодировки в {filename}")
    return None


# 3. Чтение больших файлов построчно (экономия памяти):
def count_lines(filename: str) -> int:
    """Подсчёт строк без загрузки всего файла в память"""
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    return count


# 4. Запись списка строк:
lines = ["Первая строка", "Вторая строка", "Третья строка"]
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))


# 5. Чтение файла в список без символов переноса:
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
print(lines)  # ['Милан', 'Интер', 'Лацио']


# 6. Работа с бинарными файлами (изображения):
with open('image.jpg', 'rb') as src, open('copy.jpg', 'wb') as dst:
    dst.write(src.read())


# 7. Временные файлы:
import tempfile

with tempfile.NamedTemporaryFile(mode='w', suffix='.txt',
                                  delete=True, encoding='utf-8') as tmp:
    tmp.write("Временные данные")
    tmp.flush()
    print(f"Временный файл: {tmp.name}")


# ============================================
# 8. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  РАБОТА С ФАЙЛАМИ — ШПАРГАЛКА                            │
├──────────────────────────────────────────────────────────┤
│  ОТКРЫТИЕ:                                               │
│  with open('file.txt', 'r', encoding='utf-8') as f:      │
│      ...                                                 │
├──────────────────────────────────────────────────────────┤
│  РЕЖИМЫ:                                                 │
│  'r'  — чтение                                           │
│  'w'  — запись (перезапись)                              │
│  'a'  — добавление                                       │
│  'x'  — создать новый                                    │
│  'b'  — бинарный                                         │
│  '+'  — чтение и запись                                  │
├──────────────────────────────────────────────────────────┤
│  ЧТЕНИЕ:                                                 │
│  f.read()         — весь файл                            │
│  f.readline()     — одна строка                          │
│  f.readlines()    — список строк                         │
│  for line in f:   — построчно (лучше для больших файлов) │
├──────────────────────────────────────────────────────────┤
│  ЗАПИСЬ:                                                 │
│  f.write('text')  — записать строку                      │
│  f.writelines()   — записать список строк                │
├──────────────────────────────────────────────────────────┤
│  МОДУЛЬ OS:                                              │
│  os.path.exists() — проверка существования               │
│  os.remove()      — удаление                             │
│  os.rename()      — переименование                       │
│  os.path.getsize()— размер                               │
├──────────────────────────────────────────────────────────┤
│  МОДУЛЬ SHUTIL:                                          │
│  shutil.copy()    — копирование                          │
│  shutil.move()    — перемещение                          │
│  shutil.rmtree()  — удаление папки                       │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 9. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Забыли encoding
# with open('file.txt', 'r') as f:  # может быть ошибка на Windows
#     content = f.read()

# ✅ Решение:
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()


# ❌ Ошибка 2: Не закрыли файл
# f = open('file.txt')
# content = f.read()
# # забыли f.close()

# ✅ Решение: использовать with
with open('file.txt', encoding='utf-8') as f:
    content = f.read()


# ❌ Ошибка 3: Перезапись при повторном открытии в 'w'
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("Первая запись")

with open('file.txt', 'w', encoding='utf-8') as f:  # ПЕРЕЗАПИШЕТ!
    f.write("Вторая запись")

# ✅ Решение: использовать 'a' для добавления
with open('file.txt', 'a', encoding='utf-8') as f:
    f.write("\nВторая запись")


# ❌ Ошибка 4: enumerate(file) вместо просто line
# for line in enumerate(file):
#     print(line.strip())  # AttributeError: 'tuple' object has no attribute 'strip'

# ✅ Решение:
with open('file.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# Или с нумерацией:
with open('file.txt', encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")


# ❌ Ошибка 5: Открытие несуществующего файла в режиме 'r'
# with open('nonexistent.txt', 'r') as f:  # FileNotFoundError
#     content = f.read()

# ✅ Решение: обработка ошибки
try:
    with open('nonexistent.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("Файл не найден")


# ❌ Ошибка 6: Забыли \n при записи строк
# with open('file.txt', 'w') as f:
#     f.write("Строка 1")
#     f.write("Строка 2")  # Склеится: "Строка 1Строка 2"

# ✅ Решение: добавлять \n
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("Строка 1\n")
    f.write("Строка 2\n")