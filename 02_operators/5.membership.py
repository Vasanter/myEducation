"""
ОПЕРАТОРЫ ПРИНАДЛЕЖНОСТИ В PYTHON
===================================
Операторы принадлежности используются для проверки присутствия
элемента в коллекции (списках, кортежах, множествах, словарях)
или в строке. Возвращают True или False.

Существуют два оператора принадлежности:
1. in — проверяет наличие элемента
2. not in — проверяет отсутствие элемента
"""

# ============================================
# IN — ПРОВЕРКА НАЛИЧИЯ ЭЛЕМЕНТА
# ============================================
# True, если элемент присутствует в коллекции

# Проверка в списке:
my_list = [1, 2, 3, 4, 5]
print(f"3 in {my_list}: {3 in my_list}")  # True
print(f"10 in {my_list}: {10 in my_list}")  # False

# Проверка в строке (поиск подстроки):
my_string = 'Hello, world!'
print(f"'world' in '{my_string}': {'world' in my_string}")  # True
print(f"'planet' in '{my_string}': {'planet' in my_string}")  # False

# Проверка в кортеже:
my_tuple = (10, 20, 30)
print(f"20 in {my_tuple}: {20 in my_tuple}")  # True

# Проверка в множестве:
my_set = {1, 2, 3, 4, 5}
print(f"3 in {my_set}: {3 in my_set}")  # True

# Проверка в словаре (проверяет ключи, не значения):
my_dict = {'name': 'Alice', 'age': 30}
print(f"'name' in {my_dict}: {'name' in my_dict}")  # True (ключ)
print(f"'Alice' in {my_dict}: {'Alice' in my_dict}")  # False (значение)

# ============================================
# NOT IN — ПРОВЕРКА ОТСУТСТВИЯ ЭЛЕМЕНТА
# ============================================
# True, если элемент отсутствует в коллекции

# Проверка в списке:
print(f"\n6 not in {my_list}: {6 not in my_list}")  # True
print(f"1 not in {my_list}: {1 not in my_list}")  # False

# Проверка в строке:
print(f"'planet' not in '{my_string}': {'planet' not in my_string}")  # True
print(f"'world' not in '{my_string}': {'world' not in my_string}")  # False

# Проверка в словаре:
print(f"'email' not in {my_dict}: {'email' not in my_dict}")  # True

# ============================================
# ОСОБЕННОСТИ РАБОТЫ
# ============================================

# Регистр важен при проверке строк:
text = "Hello World"
print(f"\n'hello' in '{text}': {'hello' in text}")  # False (регистр)
print(f"'Hello' in '{text}': {'Hello' in text}")  # True

# Проверка с приведением регистра:
print(f"'hello' in '{text}'.lower(): {'hello' in text.lower()}")  # True

# Проверка в пустой коллекции:
empty_list = []
print(f"1 in {empty_list}: {1 in empty_list}")  # False

# Проверка в списке с разными типами:
mixed_list = [1, "two", 3.0, [4, 5]]
print(f"'two' in {mixed_list}: {'two' in mixed_list}")  # True
print(f"4 in {mixed_list}: {4 in mixed_list}")  # False (4 во вложенном списке)
print(f"[4, 5] in {mixed_list}: {[4, 5] in mixed_list}")  # True (проверка вложенного списка)

# ============================================
# ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# Проверка прав доступа:
user_roles = ['admin', 'editor', 'viewer']
if 'admin' in user_roles:
    print("\nПользователь имеет права администратора")

# Проверка запрещённых символов:
forbidden_chars = ['@', '#', '$']
username = "user@name"
if '@' in username:
    print("Имя пользователя содержит запрещённый символ")

# Проверка расширения файла:
filename = "document.pdf"
if filename.endswith('.pdf') and 'document' in filename:
    print("Это PDF документ")

# Проверка наличия элемента перед удалением:
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    fruits.remove('banana')
    print(f"Банан удалён. Осталось: {fruits}")

# Проверка вложенности:
config = {
    'database': {
        'host': 'localhost',
        'port': 5432
    }
}
if 'database' in config and 'port' in config['database']:
    print(f"Порт: {config['database']['port']}")
