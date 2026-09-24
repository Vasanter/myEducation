"""
РАБОТА С JSON В PYTHON
========================
JSON (JavaScript Object Notation) — текстовый формат обмена данными.
Модуль json позволяет сериализовать (dict ? JSON) и десериализовать
(JSON ? dict) данные.
"""

import json


# ============================================
# 1. БАЗОВЫЙ ПРИМЕР (как в исходном коде)
# ============================================

data = {"name": "Mike", "age": 30, "city": "New York"}

# Запись в файл:
file = open(r'/15_context_manager\data.json', 'w')
json.dump(data, file)
file.close()

# Чтение из файла:
file = open(r'/15_context_manager\data.json', 'r')
loaded_data = json.load(file)
print(loaded_data)  # {'name': 'Mike', 'age': 30, 'city': 'New York'}
file.close()


# ============================================
# 2. УЛУЧШЕННАЯ ВЕРСИЯ С WITH И ENCODING
# ============================================

FILE_PATH = r'/15_context_manager\data.json'

data = {"name": "Mike", "age": 30, "city": "New York"}

# Запись (с with + encoding + ensure_ascii=False + indent):
with open(FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Чтение (с with + encoding):
with open(FILE_PATH, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print(loaded_data)  # {'name': 'Mike', 'age': 30, 'city': 'New York'}


# ============================================
# 3. ЧТО УЛУЧШЕНО И ПОЧЕМУ
# ============================================

"""
???????????????????????????????????????????????????????????????????????
?  Было                    ?  Стало                                   ?
???????????????????????????????????????????????????????????????????????
?  file = open(...)        ?  with open(...) as file:                 ?
?  file.close()            ?  (автоматическое закрытие)               ?
???????????????????????????????????????????????????????????????????????
?  open(..., 'w')          ?  open(..., 'w', encoding='utf-8')        ?
?                          ?  (правильная работа с кириллицей)        ?
???????????????????????????????????????????????????????????????????????
?  json.dump(data, file)   ?  json.dump(data, file,                   ?
?                          ?            ensure_ascii=False,           ?
?                          ?            indent=4)                     ?
?                          ?  (читаемый JSON, кириллица без \\uXXXX) ?
???????????????????????????????????????????????????????????????????????
"""


# ============================================
# 4. ПАРАМЕТРЫ JSON.DUMP()
# ============================================

data = {
    "name": "Иван",           # кириллица
    "age": 30,
    "city": "Москва",
    "skills": ["Python", "QA"]
}

# --- ensure_ascii=False ---
# По умолчанию True — кириллица превращается в \uXXXX:
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
# {"name": "\u0418\u0432\u0430\u043d", "age": 30, ...}

# С ensure_ascii=False — кириллица сохраняется:
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
# {"name": "Иван", "age": 30, ...}

# --- indent ---
# indent=4 — красивое форматирование с отступами:
with open('data3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# {
#     "name": "Иван",
#     "age": 30,
#     "city": "Москва",
#     "skills": [
#         "Python",
#         "QA"
#     ]
# }

# --- sort_keys ---
# Сортировка ключей по алфавиту:
with open('data4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


# ============================================
# 5. ПАРАМЕТРЫ JSON.LOAD()
# ============================================

with open('data3.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

print(loaded["name"])    # Иван
print(loaded["skills"])  # ['Python', 'QA']


# ============================================
# 6. РАБОТА С JSON БЕЗ ФАЙЛА
# ============================================

# --- dumps() — dict ? строка JSON ---
data = {"name": "Mike", "age": 30}
json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>

# --- loads() — строка JSON ? dict ---
json_string = '{"name": "Mike", "age": 30}'
parsed = json.loads(json_string)
print(parsed)         # {'name': 'Mike', 'age': 30}
print(type(parsed))   # <class 'dict'>


# ============================================
# 7. БЕЗОПАСНАЯ РАБОТА С JSON
# ============================================

def save_json(filename: str, data: dict) -> bool:
    """Безопасная запись JSON в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"? Данные сохранены в {filename}")
        return True
    except (TypeError, ValueError) as e:
        print(f"? Данные не сериализуются: {e}")
    except OSError as e:
        print(f"? Ошибка записи: {e}")
    return False


def load_json(filename: str) -> dict | None:
    """Безопасное чтение JSON из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"? Файл {filename} не найден")
    except json.JSONDecodeError as e:
        print(f"? Некорректный JSON: {e}")
    except OSError as e:
        print(f"? Ошибка чтения: {e}")
    return None


# Использование:
save_json('config.json', {"theme": "dark", "lang": "ru"})
config = load_json('config.json')
if config:
    print(config)


# ============================================
# 8. СЕРИАЛИЗАЦИЯ СЛОЖНЫХ ОБЪЕКТОВ
# ============================================

# Проблема: JSON не поддерживает все типы Python
from datetime import datetime

data = {
    "name": "Alice",
    "created_at": datetime.now(),  # datetime не сериализуется!
}

# ? TypeError: Object of type datetime is not JSON serializable

# ? Решение 1: преобразовать вручную
data = {
    "name": "Alice",
    "created_at": datetime.now().isoformat(),  # строка
}

# ? Решение 2: параметр default
def json_serializer(obj):
    """Преобразование нестандартных типов"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Тип {type(obj)} не сериализуется")


data = {
    "name": "Alice",
    "created_at": datetime.now(),
    "tags": {"python", "qa"},
}

with open('data5.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4, default=json_serializer)


# ============================================
# 9. ЧТО JSON ПОДДЕРЖИВАЕТ
# ============================================

"""
???????????????????????????????????????????????
?  Python              ?  JSON                ?
???????????????????????????????????????????????
?  dict                ?  object {}           ?
?  list, tuple         ?  array []            ?
?  str                 ?  string ""           ?
?  int, float          ?  number              ?
?  True                ?  true                ?
?  False               ?  false               ?
?  None                ?  null                ?
???????????????????????????????????????????????
?  datetime            ?  ? не поддерживается?
?  set                 ?  ? не поддерживается?
?  complex             ?  ? не поддерживается?
?  bytes               ?  ? не поддерживается?
???????????????????????????????????????????????
"""


# ============================================
# 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Чтение конфигурации:
def load_config(filename: str = "config.json") -> dict:
    """Загружает конфигурацию с значениями по умолчанию"""
    defaults = {"theme": "light", "lang": "ru", "debug": False}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return {**defaults, **json.load(f)}
    except FileNotFoundError:
        return defaults


# 2. Сохранение списка пользователей:
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
]

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

# Чтение:
with open('users.json', 'r', encoding='utf-8') as f:
    loaded_users = json.load(f)

for user in loaded_users:
    print(f"{user['name']}: {user['age']}")


# 3. Вложенные структуры:
data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Moscow",
            "zip": "101000"
        }
    },
    "orders": [
        {"id": 1, "total": 500},
        {"id": 2, "total": 1200},
    ]
}

with open('nested.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Доступ к вложенным данным:
with open('nested.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

print(loaded["user"]["address"]["city"])  # Moscow
print(loaded["orders"][0]["total"])       # 500


# ============================================
# 11. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????????
?  JSON В PYTHON — ШПАРГАЛКА                               ?
????????????????????????????????????????????????????????????
?  ФАЙЛ ? ОБЪЕКТ:                                          ?
?  json.dump(data, file)      — dict ? файл                ?
?  json.load(file)            — файл ? dict                ?
????????????????????????????????????????????????????????????
?  СТРОКА ? ОБЪЕКТ:                                        ?
?  json.dumps(data)           — dict ? строка              ?
?  json.loads(string)         — строка ? dict              ?
????????????????????????????????????????????????????????????
?  ПАРАМЕТРЫ DUMP:                                         ?
?  ensure_ascii=False  — сохранить кириллицу               ?
?  indent=4            — красивое форматирование           ?
?  sort_keys=True      — сортировка ключей                 ?
?  default=func        — для нестандартных типов           ?
????????????????????????????????????????????????????????????
?  ПОЛЕЗНО ЗНАТЬ:                                          ?
?  • Всегда указывайте encoding='utf-8'                    ?
?  • ensure_ascii=False — для читаемой кириллицы           ?
?  • JSON поддерживает не все типы Python                  ?
?  • Используйте with для авто-закрытия файла              ?
????????????????????????????????????????????????????????????
"""


# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Забыли encoding
# with open('file.json', 'w') as f:
#     json.dump(data, f)

# ? Решение:
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)


# ? Ошибка 2: Кириллица как \uXXXX
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump({"name": "Иван"}, f)
# {"name": "\u0418\u0432\u0430\u043d"}

# ? Решение:
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump({"name": "Иван"}, f, ensure_ascii=False)
# {"name": "Иван"}


# ? Ошибка 3: Забыли file.close()
# file = open('file.json', 'w')
# json.dump(data, file)
# # забыли file.close()

# ? Решение: использовать with
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)


# ? Ошибка 4: Сериализация datetime
# data = {"created": datetime.now()}
# json.dump(data, f)  # TypeError!

# ? Решение:
data = {"created": datetime.now().isoformat()}
json.dump(data, f, ensure_ascii=False)


# ? Ошибка 5: Некорректный JSON при чтении
# json.load(open('broken.json'))  # JSONDecodeError

# ? Решение: обработка ошибки
try:
    with open('broken.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Ошибка JSON: {e}")


# ? Ошибка 6: Использование json.dumps() вместо json.dump()
# json.dumps(data, file)  # TypeError: dumps() не принимает file!

# ? Правильно:
# json.dump(data, file)    — в файл
# json.dumps(data)         — в строку