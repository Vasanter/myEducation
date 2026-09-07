"""
МЕТОДЫ И ФУНКЦИИ СТРОК В PYTHON
=================================
Строки в Python — неизменяемые последовательности символов.
Все методы возвращают НОВУЮ строку, не изменяя оригинал.
"""

# ============================================
# 1. БАЗОВЫЕ МЕТОДЫ (ИЗМЕНЕНИЕ РЕГИСТРА)
# ============================================

text = "hello world python"

# str.capitalize() — первая буква заглавная, остальные строчные
print(text.capitalize())  # Hello world python

# str.title() — каждое слово с заглавной буквы
print(text.title())  # Hello World Python

# str.upper() — все буквы в верхнем регистре
print(text.upper())  # HELLO WORLD PYTHON

# str.lower() — все буквы в нижнем регистре
print(text.upper().lower())  # hello world python

# str.swapcase() — инвертирование регистра
text_mixed = "Hello World"
print(text_mixed.swapcase())  # hELLO wORLD

# Цепочка методов:
print(text.title().swapcase())  # hELLO wORLD pYTHON

# ============================================
# 2. МЕТОДЫ ПРОВЕРКИ СОДЕРЖИМОГО
# ============================================

# str.isalpha() — только буквы (без пробелов и цифр)
print("Hello".isalpha())  # True
print("Hello123".isalpha())  # False
print("Hello World".isalpha())  # False (пробел)

# str.isdigit() — только цифры
print("123".isdigit())  # True
print("123.45".isdigit())  # False (точка)

# str.isalnum() — только буквы и цифры (без пробелов и спецсимволов)
print("Hello123".isalnum())  # True
print("Hello 123".isalnum())  # False (пробел)

# str.isdecimal() — только десятичные цифры
print("123".isdecimal())  # True
print("½".isdecimal())  # False (дробь)

# str.isnumeric() — числовые символы (включая дроби, римские цифры)
print("123".isnumeric())  # True
print("½".isnumeric())  # True
print("Ⅳ".isnumeric())  # True (римская цифра)

# str.islower() / str.isupper() — проверка регистра
print("hello".islower())  # True
print("HELLO".isupper())  # True
print("Hello".islower())  # False

# str.isspace() — только пробельные символы
print("   ".isspace())  # True
print("\t\n".isspace())  # True
print(" a ".isspace())  # False

# str.istitle() — каждое слово с заглавной буквы
print("Hello World".istitle())  # True
print("Hello world".istitle())  # False

# ============================================
# 3. ПРОВЕРКА НАЧАЛА И КОНЦА СТРОКИ
# ============================================

text = "Hello World"

# str.startswith() — начинается ли строка с префикса
print(text.startswith("Hello"))  # True
print(text.startswith("He"))  # True
print(text.startswith(("Hi", "He")))  # True (кортеж вариантов)
print(text.startswith("World", 6))  # True (начиная с позиции 6)

# str.endswith() — заканчивается ли строка суффиксом
filename = "document.pdf"
print(filename.endswith(".pdf"))  # True
print(filename.endswith((".txt", ".pdf")))  # True (кортеж)
print(filename.endswith("pdf", 0, 12))  # True (в срезе)


# Практическое применение:
def is_image_file(filename):
    """Проверка, является ли файл изображением"""
    return filename.lower().endswith(('.jpg', '.png', '.gif', '.bmp'))


print(is_image_file("photo.JPG"))  # True

# ============================================
# 4. ПРОВЕРКА ТИПОВ СИМВОЛОВ
# ============================================

# str.isascii() — только ASCII символы
print("Hello".isascii())  # True
print("Привет".isascii())  # False

# str.isprintable() — только печатные символы
print("Hello".isprintable())  # True
print("Hello\n".isprintable())  # False (перенос строки)

# str.isidentifier() — валидный идентификатор Python
print("variable".isidentifier())  # True
print("var_name".isidentifier())  # True
print("123var".isidentifier())  # False (начинается с цифры)
print("var-name".isidentifier())  # False (дефис)

# ============================================
# 5. МЕТОДЫ ПОИСКА
# ============================================

text = "Hello World World"

# str.find() — индекс первого вхождения (-1, если не найдено)
print(text.find("World"))  # 6
print(text.find("world"))  # -1 (регистр важен)
print(text.find("World", 7))  # 12 (поиск с позиции 7)
print(text.find("o", 5, 10))  # 7 (поиск в диапазоне)

# str.rfind() — индекс последнего вхождения
print(text.rfind("World"))  # 12
print(text.rfind("o"))  # 15

# str.index() — как find(), но вызывает ValueError, если не найдено
try:
    print(text.index("World"))  # 6
    print(text.index("world"))  # ValueError
except ValueError:
    print("Подстрока не найдена")

# str.rindex() — как rfind(), но с ValueError
print(text.rindex("World"))  # 12

# str.count() — количество вхождений
print(text.count("World"))  # 2
print(text.count("o"))  # 3
print(text.count("l", 0, 5))  # 2 (в диапазоне)

# ============================================
# 6. ЗАМЕНА ПОДСТРОК
# ============================================

text = "Hello World"

# str.replace(old, new[, count]) — замена подстрок
print(text.replace("World", "Python"))  # Hello Python
print(text.replace("l", "L", 2))  # HeLLo World (только первые 2)
print("aaaa".replace("aa", "b"))  # bb (последовательная замена)

# Практический пример:
phone = "+7 (999) 123-45-67"
cleaned = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(cleaned)  # +79991234567

# ============================================
# 7. УДАЛЕНИЕ ПРОБЕЛОВ И СИМВОЛОВ
# ============================================

text = "  Hello World  "

# str.strip() — удаление с обеих сторон
print(text.strip())  # "Hello World"
print("###Hello###".strip("#"))  # "Hello"

# str.lstrip() — удаление слева
print(text.lstrip())  # "Hello World  "
print("www.example.com".lstrip("w."))  # "example.com"

# str.rstrip() — удаление справа
print(text.rstrip())  # "  Hello World"
print("example.com...".rstrip("."))  # "example.com"

# Практическое применение (очистка пользовательского ввода):
user_input = "  admin@example.com  \n"
email = user_input.strip()
print(email)  # "admin@example.com"

# ============================================
# 8. ВЫРАВНИВАНИЕ И ДОПОЛНЕНИЕ
# ============================================

text = "Hello"

# str.ljust(width) — выравнивание влево
print(text.ljust(10))  # "Hello     "
print(text.ljust(10, "*"))  # "Hello*****"

# str.rjust(width) — выравнивание вправо
print(text.rjust(10))  # "     Hello"
print(text.rjust(10, "-"))  # "-----Hello"

# str.center(width) — выравнивание по центру
print(text.center(11))  # "   Hello   "
print(text.center(11, "="))  # "===Hello==="

# str.zfill(width) — заполнение нулями слева
print("42".zfill(5))  # "00042"
print("-42".zfill(5))  # "-0042" (знак остаётся слева)

# Практическое применение (форматирование таблицы):
headers = ["Name", "Age", "City"]
print(f"{headers[0]:<10} | {headers[1]:>3} | {headers[2]:<10}")
print("Alice".ljust(10) + "|" + "25".rjust(3) + "|" + "New York".ljust(10))

# ============================================
# 9. РАЗБИЕНИЕ СТРОК
# ============================================

# str.split() — разделение по разделителю
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']
print("a b c d".split())  # ['a', 'b', 'c', 'd'] (по пробелам)
print("a,b,c,d".split(",", 2))  # ['a', 'b', 'c,d'] (максимум 2 разбиения)

# str.rsplit() — разделение справа
print("a,b,c,d".rsplit(",", 2))  # ['a,b', 'c', 'd']

# str.splitlines() — разделение по переносам строк
text = "Hello\nWorld\r\nPython"
print(text.splitlines())  # ['Hello', 'World', 'Python']
print(text.splitlines(True))  # ['Hello\n', 'World\r\n', 'Python'] (с переносами)

# str.partition() — разбиение на 3 части (до, разделитель, после)
text = "Hello World Python"
print(text.partition(" "))  # ('Hello', ' ', 'World Python')

# str.rpartition() — разбиение с конца
text = "Hello World Python World"
print(text.rpartition(" "))  # ('Hello World Python', ' ', 'World')

# ============================================
# 10. ОБЪЕДИНЕНИЕ СТРОК
# ============================================

# str.join() — объединение списка строк
words = ["Hello", "World", "Python"]
print(" ".join(words))  # "Hello World Python"
print(", ".join(words))  # "Hello, World, Python"
print("".join(["a", "b", "c"]))  # "abc"

# Практическое применение:
numbers = ["1", "2", "3", "4"]
print("-".join(numbers))  # "1-2-3-4"

# Ошибка при попытке объединить нестроковые элементы:
# print(", ".join([1, 2, 3]))  # TypeError
print(", ".join(map(str, [1, 2, 3])))  # "1, 2, 3"

# ============================================
# 11. СОВРЕМЕННЫЕ МЕТОДЫ (Python 3.9+)
# ============================================

# str.removeprefix() — удаление префикса
text = "HelloWorld"
print(text.removeprefix("Hello"))  # "World"
print(text.removeprefix("Hi"))  # "HelloWorld" (не изменяет, если нет)

# str.removesuffix() — удаление суффикса
filename = "file.txt"
print(filename.removesuffix(".txt"))  # "file"
print(filename.removesuffix(".pdf"))  # "file.txt"

# ============================================
# 12. РАБОТА С UNICODE
# ============================================

unicode_text = "Hello Привет 你好 🌍"

print(f"Длина строки: {len(unicode_text)}")  # количество символов
print(f"Только ASCII: {unicode_text.isascii()}")  # False

# Проверка на наличие кириллицы:
has_cyrillic = any('\u0400' <= char <= '\u04FF' for char in unicode_text)
print(f"Содержит кириллицу: {has_cyrillic}")  # True

# Проверка на наличие эмодзи:
has_emoji = any('\U0001F300' <= char <= '\U0001F9FF' for char in unicode_text)
print(f"Содержит эмодзи: {has_emoji}")  # True

# Кодирование и декодирование:
encoded = unicode_text.encode('utf-8')
print(f"Закодировано: {encoded}")
decoded = encoded.decode('utf-8')
print(f"Декодировано: {decoded}")

# ============================================
# 13. СВОДНАЯ ТАБЛИЦА ЧАСТО ИСПОЛЬЗУЕМЫХ МЕТОДОВ
# ============================================

methods_table = [
    ("capitalize()", "Первая буква заглавная"),
    ("title()", "Каждое слово с заглавной"),
    ("upper()", "Верхний регистр"),
    ("lower()", "Нижний регистр"),
    ("strip()", "Удаление пробелов"),
    ("split()", "Разбиение на список"),
    ("join()", "Объединение списка"),
    ("replace()", "Замена подстроки"),
    ("find()", "Поиск подстроки"),
    ("startswith()", "Проверка начала"),
    ("endswith()", "Проверка конца"),
]

print("\n" + "=" * 50)
print("ЧАСТО ИСПОЛЬЗУЕМЫЕ МЕТОДЫ СТРОК")
print("=" * 50)
for method, description in methods_table:
    print(f"{method:15} — {description}")
