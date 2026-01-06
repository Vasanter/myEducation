"""МЕТОДЫ И ФУНКЦИИ СТРОК"""

# 1.БАЗОВЫЕ МЕТОДЫ
# str.capitalize() - первая буква заглавная
text = "hello world"
print(text.capitalize())  # Hello world

# str.title() - каждое слово будет с заглавной буквы
text = "hello world python"
print(text.title())  # Hello World Python

# str.upper() - перевод в верхний регистр
text = "Hello"
print(text.upper())  # HELLO

# str.lower() - перевод в нижний регистр
text = "HELLO"
print(text.lower())  # hello

# str.swapcase() - инвертировать регистр
text = "Hello World"
print(text.swapcase())  # hELLO wORLD

# 2. МЕТОДЫ ПРОВЕРКИ
# str.isalpha() - строка содержит только буквы
print("Hello".isalpha())  # True
print("Hello123".isalpha())  # False
print("Hello World".isalpha())  # False (пробел не буква)

# str.isdigit() - строка содержит только цифры
print("123".isdigit())  # True
print("123.45".isdigit())  # False
print("¹²³".isdigit())  # True (unicode цифры)

# str.isalnum() - строка содержит только буквы или цифры
print("Hello123".isalnum())  # True
print("Hello 123".isalnum())  # False (пробел)
print("Hello!".isalnum())  # False (спецсимвол)

# str.isdecimal() - строка содержит только десятичные цифры
print("123".isdecimal())  # True
print("½".isdecimal())  # False
print("0x1F".isdecimal())  # False

# str.isnumeric() - строка содержит только числовые символы
print("123".isnumeric())  # True
print("½".isnumeric())  # True
print("Ⅳ".isnumeric())  # True (римские цифры)

# str.islower() - проверяет что все буквы в нижнем регистре
print("hello".islower())  # True
print("Hello".islower())  # False
print("123".islower())  # False (нет букв)

# str.isupper() - проверяет что все буквы в верхнем регистре
print("HELLO".isupper())  # True
print("Hello".isupper())  # False

# str.isspace() - проверяет что строка содержит только пробельные символы
print("   ".isspace())  # True
print("\t\n".isspace())  # True
print("   a".isspace())  # False

# str.istitle() - проверяет что каждое слово написано с заглавной буквы
print("Hello World".istitle())  # True
print("Hello world".istitle())  # False
print("123 Hello".istitle())  # False

# str.startswith(prefix) - проверяет что строка начинается с ...
text = "Hello World"
print(text.startswith("Hello"))  # True
print(text.startswith("He"))  # True
print(text.startswith(("Hi", "He")))  # True (кортеж вариантов)
print(text.startswith("World", 6))  # True (начиная с позиции 6)

# str.endswith(suffix) - проверяет что строка заканчивается на ..
text = "file.txt"
print(text.endswith(".txt"))  # True
print(text.endswith((".txt", ".pdf")))  # True
print(text.endswith("txt", 0, 8))  # True (в срезе)

# str.isascii() - проверяет что строка содержит только ASCII символы
print("Hello".isascii())  # True
print("Привет".isascii())  # False
print("Hello123!".isascii())  # True

# str.isprintable() - проверяет что строка содержит только печатные символы
print("Hello".isprintable())  # True
print("Hello\n".isprintable())  # False (непечатный \n)

# str.isidentifier() - проверяет что строка содержит валидный идентификатор (именем переменной, функции, класса и т. д.)
print("variable".isidentifier())  # True
print("var_name".isidentifier())  # True
print("123var".isidentifier())  # False
print("var-name".isidentifier())  # False

# 3. МЕТОДЫ ПОИСКА И ЗАМЕНЫ
# str.find() - ищет первое вхождение подстроки в строке
text = "Hello World World"
print(text.find("World"))  # 6
print(text.find("world"))  # -1 (не найдено)
print(text.find("World", 7))  # 12 (начиная с позиции 7)
print(text.find("o", 5, 10))  # 7 (в диапазоне 5-10)

# str.rfind() - поиск с конца
text = "Hello World World"
print(text.rfind("World"))  # 12
print(text.rfind("o"))  # 15

# str.index() - ищет первое вхождение указанной подстроки (или символа) в строке и возвращает его начальный индекс
text = "Hello World"
try:
    print(text.index("World"))  # 6
    print(text.index("world"))  # ValueError
except ValueError as e:
    print("Подстрока не найдена")

# str.rindex() - Index с конца
text = "Hello World World"
print(text.rindex("World"))  # 12

# str.count() - количество вхождений
text = "Hello World World"
print(text.count("World"))  # 2
print(text.count("o"))  # 3
print(text.count("l", 0, 5))  # 2 (в диапазоне)

# str.replace(old, new) - замена подстроки
text = "Hello World"
print(text.replace("World", "Python"))  # Hello Python
print(text.replace("l", "L", 1))  # HeLlo World (только первое)
print("aaaa".replace("aa", "b"))  # bb (последовательная замена)

# 4. МЕТОДЫ ФОРМАТИРОВАНИЯ
# str.strip([chars]) - удаление пробелов с обоих сторон
text = "  Hello World  "
print(text.strip())  # "Hello World"
print("###Hello###".strip("#"))  # "Hello"
print("  Hello  ".strip(" H"))  # "ello" (удалил H и пробелы)

# str.lstrip([chars]) - удаление слева
text = "  Hello  "
print(text.lstrip())  # "Hello  "
print("www.example.com".lstrip("w."))  # "example.com"

# str.rstrip([chars]) - удаление справа
text = "  Hello  "
print(text.rstrip())  # "  Hello"
print("example.com...".rstrip("."))  # "example.com"

# str.ljust(width[, fillchar]) - выравнивание влево
text = "Hello"
print(text.ljust(10))  # "Hello     "
print(text.ljust(10, "*"))  # "Hello*****"
print(text.ljust(3))  # "Hello" (если width меньше длины)

# str.rjust(width[, fillchar]) - выравнивание вправо
text = "Hello"
print(text.rjust(10))  # "     Hello"
print(text.rjust(10, "-"))  # "-----Hello"

# str.center(width[, fillchar]) - выравнивание по центру
text = "Hello"
print(text.center(11))  # "   Hello   "
print(text.center(11, "="))  # "===Hello==="
print(text.center(3))  # "Hello"

# str.zfill(width) - заполнение нулями слева
print("42".zfill(5))  # "00042"
print("-42".zfill(5))  # "-0042" (знак остается слева)
print("3.14".zfill(6))  # "003.14"

# str.expandtabs([tabsize]) - замена табуляций
text = "Hello\tWorld"
print(text.expandtabs())  # "Hello   World" (8 пробелов по умолчанию)
print(text.expandtabs(4))  # "Hello World" (4 пробела)

# 5. МЕТОДЫ РАЗБИЕНИЯ И СОЕДИНЕНИЯ
# str.split([sep[, maxsplit]]) - разделяет строку на список подстрок (слов) на основе заданного разделителя
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']
print("a b c d".split())  # ['a', 'b', 'c', 'd'] (по пробелам)
print("a,b,c,d".split(",", 2))  # ['a', 'b', 'c, d'] (максимум 2 разбиения)
print("".split(","))  # [''] (особый случай)

# str.rsplit([sep[, maxsplit]]) - разделяет строку на список подстрок по заданному разделителю, возвращая этот список
text = "apple,banana,cherry"
print(text.rsplit(",", 1))  # ['apple,banana', 'cherry']

# str.splitlines([keepends]) - разбивает строку на список отдельных строк по символам переноса строки
# (например, \n, \r, \r\n), удаляя сами символы переноса по умолчанию
text = "Hello\nWorld\nPython"
print(text.splitlines())  # ['Hello', 'World', 'Python']
print(text.splitlines(True))  # ['Hello\n', 'World\n', 'Python']

# str.partition(sep) - разбивает строку на три части по первому вхождению заданного разделителя (подстроки) и
# возвращает их в виде кортежа: [часть_до_разделителя, сам_разделитель, часть_после_разделителя].
text = "Hello World Python"
print(text.partition(" "))  # ('Hello', ' ', 'World Python')
print("Hello".partition(" "))  # ('Hello', '', '') (если разделитель не найден)

# str.rpartition(sep) - разбивает строку на три части по последнему вхождению заданного разделителя (sep), возвращая
# кортеж из трех элементов
text = "Hello World Python World"
print(text.rpartition(" "))  # ('Hello World Python', ' ', 'World')

# str.join(iterable) -  объединяет элементы итерируемого объекта (например, списка строк) в одну строку, используя
# строку, к которой метод был применен, в качестве разделителя между элементами
words = ["Hello", "World", "Python"]
print(", ".join(words))  # "Hello, World, Python"
print("".join(["a", "b", "c"]))  # "abc"
print("-".join("123"))  # "1-2-3"

# 6. СОВРЕМЕННЫЕ МЕТОДЫ (Python 3.9+)
# str.removeprefix(prefix) - удаление префикса
text = "HelloWorld"
print(text.removeprefix("Hello"))  # "World"
print(text.removeprefix("Hi"))  # "HelloWorld" (не удаляет если нет)

# str.removesuffix(suffix) - удаление суффикса
text = "file.txt"
print(text.removesuffix(".txt"))  # "file"
print(text.removesuffix(".pdf"))  # "file.txt"

# 7. СПЕЦИАЛЬНЫЕ МЕТОДЫ ФОРМАТИРОВАНИЯ
# str.format(*args, **kwargs) - форматирование с помощью метода format
# Позиционные аргументы
print("{} {}".format("Hello", "World"))  # Hello World
print("{1} {0}".format("World", "Hello"))  # Hello World

# Именованные аргументы
print("{name} is {age} years old".format(name="Alice", age=25))

# Форматирование чисел
print("{:.2f}".format(3.14159))  # 3.14
print("{:,}".format(1000000))  # 1,000,000
print("{:>10}".format("Hello"))  # "     Hello"

# str.format_map(mapping) - форматирование из словаря
data = {"name": "Alice", "age": 25}
print("{name} is {age} years old".format_map(data))  # Alice is 25 years old

# str.maketrans(x[, y[, z]]) и str.translate(table) - замена символов
# Простая замена
trans_table = str.maketrans("aeiou", "12345")
text = "hello world"
print(text.translate(trans_table))  # h2ll4 w4rld

# Удаление символов
trans_table = str.maketrans("", "", "aeiou")
print(text.translate(trans_table))  # hll wrld

# Словарь для замены
trans_dict = {ord('a'): 'A', ord('e'): 'E', ord('o'): None}
trans_table = str.maketrans(trans_dict)
print("hello world".translate(trans_table))  # hEll w rld


# 8. ПРИМЕР КОМПЛЕКСНОГО ИСПОЛЬЗОВАНИЯ
def process_text(text):
    """Пример комплексной обработки текста"""

    # 1. Очистка и нормализация
    text = text.strip()
    text = text.lower()

    # 2. Замена нескольких пробелов на один
    import re
    text = re.sub(r'\s+', ' ', text)

    # 3. Каждое слово с заглавной буквы
    text = text.title()

    # 4. Удаление определенных символов
    text = text.replace("-", " ")

    # 5. Разбиение на слова
    words = text.split()

    # 6. Фильтрация слов
    filtered_words = [word for word in words if word.isalpha()]

    # 7. Соединение обратно
    result = " ".join(filtered_words)

    return result


# Пример использования
input_text = "  HELLO-WORLD  python123  programming!!!  "
print(process_text(input_text))  # Hello World Python Programming

# 9. ПРОВЕРКА РАБОТЫ С РАЗНЫМИ ККОДИРОВКАМИ
# Работа с Unicode
unicode_text = "Hello Привет 你好 🌍"
print(f"Длина строки: {len(unicode_text)}")  # 19 символов
print(f"Только буквы: {unicode_text.isalpha()}")  # False
print(f"Только ASCII: {unicode_text.isascii()}")  # False

# Проверка на наличие определенных символов
print("Содержит кириллицу:", any('\u0400' <= c <= '\u04FF' for c in unicode_text))
print("Содержит эмодзи:", any('\U0001F300' <= c <= '\U0001F9FF' for c in unicode_text))

# 10. СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ МЕТОДОВ
import timeit

# Сравнение разных способов проверки
text = "Hello123"

# Метод 1: isdigit()
time1 = timeit.timeit('text.isdigit()', globals=globals(), number=1000000)

# Метод 2: Регулярные выражения
import re

pattern = re.compile(r'^\d+$')
time2 = timeit.timeit('pattern.match(text)', globals=globals(), number=1000000)


# Метод 3: Цикл
def is_digit_loop(s):
    for char in s:
        if not char.isdigit():
            return False
    return bool(s)


time3 = timeit.timeit('is_digit_loop(text)', globals=globals(), number=1000000)

print(f"isdigit(): {time1:.4f} сек")
print(f"regex: {time2:.4f} сек")
print(f"loop: {time3:.4f} сек")
