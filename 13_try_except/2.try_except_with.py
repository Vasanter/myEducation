"""
КОНСТРУКЦИЯ TRY-EXCEPT С WITH
================================
Конструкция with — это менеджер контекста, который автоматически
управляет ресурсами: открывает и закрывает файлы, соединения и т.д.

Вместе с try-except она образует мощный инструмент для безопасной
работы с ресурсами, которые могут вызвать ошибки.

Преимущества with:
- Автоматическое закрытие ресурса (даже при ошибке)
- Код чище и безопаснее
- Нет необходимости вручную вызывать close()
"""

# ============================================
# 1. БЕЗ WITH VS С WITH
# ============================================

# ? БЕЗ WITH — нужно вручную закрывать ресурс:
file = open("data.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # обязательно закрыть!


# ? С WITH — ресурс закрывается автоматически:
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
    # файл автоматически закрыт здесь
except FileNotFoundError:
    print("Файл не найден")


# ============================================
# 2. БАЗОВЫЙ СИНТАКСИС
# ============================================

"""
try:
    with open(...) as resource:
        # работа с ресурсом
except SomeError:
    # обработка ошибки
"""

# Пример: безопасное чтение файла
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Прочитано {len(content)} символов")
except FileNotFoundError:
    print("Файл не существует")
except PermissionError:
    print("Нет прав на чтение файла")
except UnicodeDecodeError:
    print("Ошибка кодировки")


# ============================================
# 3. ОБРАБОТКА ОШИБОК ВНУТРИ WITH
# ============================================

# Ошибку можно обработать внутри блока with:
try:
    with open("numbers.txt", "r") as f:
        try:
            content = f.read()
            numbers = [int(x) for x in content.split()]
            print(f"Сумма: {sum(numbers)}")
        except ValueError as e:
            print(f"Ошибка в данных: {e}")
except FileNotFoundError:
    print("Файл не найден")


# ============================================
# 4. ЧТЕНИЕ ФАЙЛА С ОБРАБОТКОЙ
# ============================================

def read_file_safe(filename: str) -> str | None:
    """
    Безопасное чтение файла.

    Args:
        filename: Путь к файлу.

    Returns:
        Содержимое файла или None при ошибке.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"? Файл {filename} не найден")
    except PermissionError:
        print(f"? Нет доступа к {filename}")
    except UnicodeDecodeError:
        print(f"? Ошибка кодировки в {filename}")
    except Exception as e:
        print(f"? Неожиданная ошибка: {e}")
    return None


content = read_file_safe("example.txt")
if content:
    print(content[:100])


# ============================================
# 5. ЗАПИСЬ В ФАЙЛ С ОБРАБОТКОЙ
# ============================================

def write_file_safe(filename: str, content: str) -> bool:
    """
    Безопасная запись в файл.

    Returns:
        True при успехе, False при ошибке.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"? Записано в {filename}")
        return True
    except PermissionError:
        print(f"? Нет прав на запись в {filename}")
    except OSError as e:
        print(f"? Ошибка ОС: {e}")
    return False


write_file_safe("output.txt", "Привет, мир!")


# ============================================
# 6. ЧТЕНИЕ JSON
# ============================================

import json

def read_json_safe(filename: str) -> dict | None:
    """Безопасное чтение JSON-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"? Файл {filename} не найден")
    except json.JSONDecodeError as e:
        print(f"? Некорректный JSON: {e}")
    return None


config = read_json_safe("config.json")
if config:
    print(config)


# ============================================
# 7. ЗАПИСЬ JSON
# ============================================

def write_json_safe(filename: str, data: dict) -> bool:
    """Безопасная запись JSON"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except (TypeError, ValueError) as e:
        print(f"? Данные не сериализуются: {e}")
    except OSError as e:
        print(f"? Ошибка записи: {e}")
    return False


write_json_safe("config.json", {"name": "Alice", "age": 30})


# ============================================
# 8. РАБОТА С НЕСКОЛЬКИМИ ФАЙЛАМИ
# ============================================

def copy_file(source: str, destination: str) -> bool:
    """Копирование файла с обработкой ошибок"""
    try:
        with open(source, "r", encoding="utf-8") as src:
            with open(destination, "w", encoding="utf-8") as dst:
                dst.write(src.read())
        print(f"? Скопировано: {source} ? {destination}")
        return True
    except FileNotFoundError:
        print(f"? Файл {source} не найден")
    except PermissionError:
        print(f"? Нет прав для записи в {destination}")
    except OSError as e:
        print(f"? Ошибка: {e}")
    return False


# Можно объединить в один with:
def copy_file_v2(source: str, destination: str) -> bool:
    """Копирование через один with"""
    try:
        with open(source, "r", encoding="utf-8") as src, \
             open(destination, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        return True
    except (FileNotFoundError, PermissionError) as e:
        print(f"? Ошибка: {e}")
    return False


# ============================================
# 9. РАБОТА С БАЗОЙ ДАННЫХ (SQLITE)
# ============================================

import sqlite3

def get_users_safe(db_path: str) -> list:
    """Безопасное получение пользователей из БД"""
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"? Ошибка БД: {e}")
    except sqlite3.DatabaseError as e:
        print(f"? Ошибка базы данных: {e}")
    return []


# ============================================
# 10. СЕТЕВЫЕ ЗАПРОСЫ С WITH
# ============================================

import requests

def fetch_url_safe(url: str) -> str | None:
    """Безопасный HTTP-запрос через Session"""
    try:
        with requests.Session() as session:
            response = session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
    except requests.exceptions.ConnectionError:
        print("? Нет соединения")
    except requests.exceptions.Timeout:
        print("? Превышено время ожидания")
    except requests.exceptions.HTTPError as e:
        print(f"? HTTP-ошибка: {e}")
    except requests.exceptions.RequestException as e:
        print(f"? Ошибка запроса: {e}")
    return None


# ============================================
# 11. СОЗДАНИЕ СВОЕГО МЕНЕДЖЕРА КОНТЕКСТА
# ============================================

class DatabaseConnection:
    """Собственный менеджер контекста для БД"""

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Вызывается при входе в блок with"""
        print(f"Подключение к {self.db_path}...")
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Вызывается при выходе из блока with"""
        print("Закрытие соединения...")
        if self.connection:
            if exc_type is None:
                self.connection.commit()  # коммит при успехе
            else:
                self.connection.rollback()  # откат при ошибке
            self.connection.close()
        return False  # не подавляем исключения


# Использование:
try:
    with DatabaseConnection("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
        print("Таблица создана")
except sqlite3.Error as e:
    print(f"Ошибка БД: {e}")


# ============================================
# 12. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Чтение CSV-файла:
import csv

def read_csv_safe(filename: str) -> list:
    """Безопасное чтение CSV"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"? Файл {filename} не найден")
    except csv.Error as e:
        print(f"? Ошибка CSV: {e}")
    return []


# 2. Логирование в файл:
def log_message(message: str, log_file: str = "app.log") -> None:
    """Запись в лог-файл"""
    from datetime import datetime
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")
    except OSError as e:
        print(f"? Не удалось записать лог: {e}")


# 3. Чтение больших файлов построчно:
def process_large_file(filename: str) -> int:
    """Обработка большого файла построчно (экономия памяти)"""
    line_count = 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line_count += 1
                # обработка строки
        return line_count
    except FileNotFoundError:
        print(f"? Файл {filename} не найден")
    return 0


# 4. Временные файлы:
import tempfile

def use_temp_file():
    """Работа с временным файлом"""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            delete=True,  # удалить после закрытия
            encoding="utf-8"
        ) as tmp:
            tmp.write("Временные данные")
            tmp.flush()
            print(f"Временный файл: {tmp.name}")
    except OSError as e:
        print(f"? Ошибка: {e}")


# ============================================
# 13. ОБРАБОТКА ОШИБОК В __EXIT__
# ============================================

class SafeFile:
    """Менеджер контекста с подавлением ошибок"""

    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        # Подавить FileNotFoundError:
        if exc_type is FileNotFoundError:
            print(f"?? Файл {self.filename} не найден, но программа продолжает работу")
            return True  # True = подавить исключение

        return False  # остальные ошибки пробрасываем


# Использование:
with SafeFile("nonexistent.txt") as f:
    content = f.read()  # не вызовет краш программы

print("Программа продолжает работу!")


# ============================================
# 14. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????????
?  TRY-EXCEPT С WITH — ШПАРГАЛКА                           ?
????????????????????????????????????????????????????????????
?  БАЗОВЫЙ СИНТАКСИС:                                      ?
?  try:                                                    ?
?      with open(...) as f:                                ?
?          # работа с ресурсом                             ?
?  except SomeError:                                       ?
?      # обработка                                         ?
????????????????????????????????????????????????????????????
?  ЧТО ДАЁТ WITH:                                          ?
?  • Автоматическое закрытие ресурса                       ?
?  • Закрытие даже при ошибке                              ?
?  • Чистый код без finally                                ?
?  • Безопасность работы с файлами, БД, сетью              ?
????????????????????????????????????????????????????????????
?  ЧАСТЫЕ ОШИБКИ:                                          ?
?  FileNotFoundError    — файл не найден                   ?
?  PermissionError      — нет прав                         ?
?  UnicodeDecodeError   — ошибка кодировки                 ?
?  json.JSONDecodeError — некорректный JSON                ?
?  OSError              — общая ошибка ОС                  ?
?  sqlite3.Error        — ошибка БД                        ?
????????????????????????????????????????????????????????????
?  МЕНЕДЖЕР КОНТЕКСТА:                                     ?
?  __enter__()  — при входе в with                         ?
?  __exit__()   — при выходе из with                       ?
?  return True  — подавить исключение                      ?
?  return False — пробросить исключение                    ?
????????????????????????????????????????????????????????????
"""


# ============================================
# 15. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Открытие файла вне with
# f = open("file.txt")
# content = f.read()
# f.close()  # забудем — утечка ресурса

# ? Решение:
with open("file.txt") as f:
    content = f.read()


# ? Ошибка 2: Ловить все ошибки подряд
# try:
#     with open("file.txt") as f:
#         content = f.read()
# except:  # ПЛОХО
#     pass

# ? Решение:
try:
    with open("file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Нет прав")


# ? Ошибка 3: Возврат из with без закрытия
# def bad():
#     f = open("file.txt")
#     return f.read()  # файл не закрыт!

# ? Решение:
def good():
    with open("file.txt") as f:
        return f.read()  # файл закроется автоматически


# ? Ошибка 4: Забыть encoding
# with open("file.txt") as f:  # может быть ошибка на Windows
#     content = f.read()

# ? Решение: всегда указывать encoding
with open("file.txt", encoding="utf-8") as f:
    content = f.read()