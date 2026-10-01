"""
ТИПЫ СЛОВАРЕЙ В PYTHON
========================
В Python есть несколько типов словарей — от встроенного dict
до специализированных из модуля collections.

Основные типы:
1. dict — стандартный словарь
2. OrderedDict — словарь с гарантированным порядком
3. defaultdict — словарь со значением по умолчанию
4. Counter — словарь для подсчёта
5. ChainMap — объединение нескольких словарей
6. MappingProxyType — неизменяемое представление словаря
7. TypedDict — типизированный словарь (type hints)
8. UserDict — обёртка для наследования
"""

from collections import OrderedDict, defaultdict, Counter, ChainMap, UserDict
from types import MappingProxyType
from typing import TypedDict

# ============================================
# 1. DICT — СТАНДАРТНЫЙ СЛОВАРЬ
# ============================================

"""
Обычный словарь — изменяемая коллекция пар «ключ-значение».
С Python 3.7 сохраняет порядок вставки.
"""

# Создание:
person = {"name": "Alice", "age": 30, "city": "Moscow"}

# Альтернативные способы:
person2 = dict(name="Bob", age=25)
person3 = dict([("name", "Charlie"), ("age", 35)])
person4 = {k: v for k, v in [("name", "Dave"), ("age", 40)]}

print(person)  # {'name': 'Alice', 'age': 30, 'city': 'Moscow'}

# Основные операции:
person["email"] = "alice@mail.com"  # добавить
person["age"] = 31  # изменить
del person["city"]  # удалить
print(person.get("phone", "нет"))  # безопасный доступ

# Порядок сохраняется:
for key in person:
    print(key)  # name, age, email — в порядке вставки

# Когда использовать:
# ? Универсальный выбор для 90% задач
# ? Быстрый доступ по ключу O(1)
# ? Изменяемый, упорядоченный (3.7+)


# ============================================
# 2. ORDEREDDICT — СЛОВАРЬ С ПОРЯДКОМ
# ============================================

"""
OrderedDict гарантирует порядок вставки (актуально до Python 3.7).
Сейчас почти не нужен — обычный dict тоже сохраняет порядок.

Остались особенности:
- Метод move_to_end()
- Равенство учитывает порядок
"""

from collections import OrderedDict

# Создание:
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

print(od)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Перемещение в конец:
od.move_to_end("first")
print(od)  # OrderedDict([('second', 2), ('third', 3), ('first', 1)])

# Перемещение в начало:
od.move_to_end("first", last=False)
print(od)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Удаление с конца:
od.popitem(last=True)  # удаляет последний
od.popitem(last=False)  # удаляет первый

# ?? Равенство учитывает порядок:
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(od1 == od2)  # False!

# А обычный dict — не учитывает:
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)  # True

# Когда использовать:
# ? Явный порядок с move_to_end()
# ? Равенство с учётом порядка
# ? Совместимость с Python 3.6 и ниже


# ============================================
# 3. DEFAULTDICT — СЛОВАРЬ СО ЗНАЧЕНИЕМ ПО УМОЛЧАНИЮ
# ============================================

"""
defaultdict автоматически создаёт значение для отсутствующего ключа.
Избавляет от проверки «а есть ли ключ?».
"""

from collections import defaultdict

# Без defaultdict — неудобно:
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter_plain = {}
for word in words:
    if word not in counter_plain:
        counter_plain[word] = 0
    counter_plain[word] += 1
print(counter_plain)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# С defaultdict — элегантно:
counter = defaultdict(int)  # значение по умолчанию — int() = 0
for word in words:
    counter[word] += 1
print(dict(counter))  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Примеры с разными фабриками:
# --- int ? 0 ---
counts = defaultdict(int)
counts["a"] += 1
print(counts["missing"])  # 0

# --- list ? [] ---
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
groups["vegs"].append("carrot")
print(dict(groups))
# {'fruits': ['apple', 'banana'], 'vegs': ['carrot']}

# --- set ? set() ---
tags = defaultdict(set)
tags["python"].add("backend")
tags["python"].add("testing")
print(dict(tags))  # {'python': {'backend', 'testing'}}

# --- dict ? {} ---
nested = defaultdict(dict)
nested["user"]["name"] = "Alice"
print(dict(nested))  # {'user': {'name': 'Alice'}}

# --- lambda ? своё значение ---
defaults = defaultdict(lambda: "не указано")
print(defaults["missing"])  # "не указано"

# Когда использовать:
# ? Группировка элементов (list)
# ? Подсчёт (int)
# ? Уникальные значения (set)
# ? Вложенные структуры (dict)
# ? Избежать KeyError


# ============================================
# 4. COUNTER — СЛОВАРЬ ДЛЯ ПОДСЧЁТА
# ============================================

"""
Counter — подкласс dict для подсчёта хешируемых объектов.
Автоматически считает частоту элементов.
"""

from collections import Counter

# Подсчёт символов:
text = "hello world"
counter = Counter(text)
print(counter)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Подсчёт слов:
words = "the cat and the dog and the bird".split()
word_count = Counter(words)
print(word_count)
# Counter({'the': 3, 'and': 2, 'cat': 1, 'dog': 1, 'bird': 1})

# --- Основные методы ---

# most_common(n) — топ n элементов:
print(word_count.most_common(2))
# [('the', 3), ('and', 2)]

# elements() — итератор по элементам:
counter = Counter(a=3, b=1)
print(list(counter.elements()))  # ['a', 'a', 'a', 'b']

# total() — сумма всех счётчиков (Python 3.10+):
print(Counter(a=3, b=2).total())  # 5

# --- Арифметика с Counter ---

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

# Сложение:
print(c1 + c2)  # Counter({'a': 4, 'b': 3})

# Вычитание (только положительные):
print(c1 - c2)  # Counter({'a': 2})

# Пересечение (минимум):
print(c1 & c2)  # Counter({'a': 1, 'b': 1})

# Объединение (максимум):
print(c1 | c2)  # Counter({'a': 3, 'b': 2})

# --- Практические примеры ---

# Топ-5 слов в тексте:
text = "the cat and the dog and the bird and the fish"
top_words = Counter(text.split()).most_common(3)
print(top_words)  # [('the', 4), ('and', 3), ('cat', 1)]


# Проверка анаграмм:
def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


print(is_anagram("listen", "silent"))  # True

# Когда использовать:
# ? Подсчёт частоты элементов
# ? Поиск топ-N
# ? Сравнение мультимножеств
# ? Анализ текста


# ============================================
# 5. CHAINMAP — ОБЪЕДИНЕНИЕ СЛОВАРЕЙ
# ============================================

"""
ChainMap объединяет несколько словарей в одно представление.
Поиск идёт по цепочке — слева направо.
"""

from collections import ChainMap

# --- Объединение без копирования ---
defaults = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark"}
cli_args = {"debug": True}

config = ChainMap(cli_args, user_prefs, defaults)

print(config["theme"])  # dark   ? из user_prefs
print(config["lang"])  # en     ? из defaults
print(config["debug"])  # True   ? из cli_args

# Все ключи:
print(list(config.keys()))
# ['debug', 'theme', 'lang']

# Изменение — затрагивает первый словарь:
config["lang"] = "ru"
print(cli_args)  # {'debug': True, 'lang': 'ru'}

# --- Приоритеты (важно!) ---
# Приоритет: первый словарь > второй > третий
priority = ChainMap(
    {"a": 1},  # высший приоритет
    {"a": 2, "b": 2},
    {"a": 3, "b": 3, "c": 3},
)
print(priority["a"])  # 1
print(priority["b"])  # 2
print(priority["c"])  # 3

# --- Добавление нового словаря ---
config = ChainMap({"theme": "dark"})
config = config.new_child({"theme": "light"})
print(config["theme"])  # light


# --- Практический пример: конфигурация ---
def get_config(**overrides):
    """Конфигурация с приоритетами"""
    defaults = {"host": "localhost", "port": 5432, "debug": False}
    env = {"host": "prod.server", "debug": True}

    return ChainMap(overrides, env, defaults)


config = get_config(port=3306)
print(config["host"])  # prod.server
print(config["port"])  # 3306
print(config["debug"])  # True

# Когда использовать:
# ? Приоритеты конфигурации
# ? Объединение без копирования
# ? Поиск по нескольким словарям
# ? Динамическое добавление слоёв


# ============================================
# 6. MAPPINGPROXYTYPE — НЕИЗМЕНЯЕМЫЙ СЛОВАРЬ
# ============================================

"""
MappingProxyType — read-only представление словаря.
Изменения оригинального dict видны, но через proxy — нет.
"""

from types import MappingProxyType

# Создание:
original = {"name": "Alice", "age": 30}
readonly = MappingProxyType(original)

print(readonly["name"])  # Alice
print(readonly["age"])  # 30

# ? Изменение через proxy запрещено:
# readonly["age"] = 31  # TypeError: 'mappingproxy' object does not support item assignment

# ? Но изменения оригинала видны:
original["age"] = 31
print(readonly["age"])  # 31


# --- Практический пример: защита конфигурации ---
class Config:
    """Конфигурация с защитой от изменений"""

    def __init__(self):
        self._settings = {"debug": False, "port": 8080}
        self.settings = MappingProxyType(self._settings)

    def update(self, **kwargs):
        """Обновление через метод"""
        self._settings.update(kwargs)


config = Config()
print(config.settings["port"])  # 8080

# ? Нельзя изменить напрямую:
# config.settings["port"] = 9090  # TypeError

# ? Только через метод:
config.update(port=9090)
print(config.settings["port"])  # 9090

# Когда использовать:
# ? Защита конфигурации от изменений
# ? Read-only API
# ? Безопасная передача настроек


# ============================================
# 7. TYPEDDICT — ТИПИЗИРОВАННЫЙ СЛОВАРЬ
# ============================================

"""
TypedDict — способ описать структуру словаря через type hints.
Проверяется mypy/pyright, но НЕ работает в runtime.
"""

from typing import TypedDict


class UserDict(TypedDict):
    """Структура пользователя"""
    name: str
    age: int
    email: str


# Создание:
user: UserDict = {
    "name": "Alice",
    "age": 30,
    "email": "alice@mail.com",
}

# ?? В runtime ошибки не будет:
wrong: UserDict = {"name": "Bob"}  # type checker пожалуется, но Python — нет


# --- Обязательные и необязательные поля ---
class PartialUser(TypedDict, total=False):
    """Все поля необязательные"""
    name: str
    age: int


class MixedUser(TypedDict):
    """Обязательные + необязательные"""
    name: str  # обязательно
    age: int  # обязательно


class MixedUserWithOptional(TypedDict, total=False):
    name: str  # обязательно (переопределено)
    age: int  # необязательно


# --- Наследование ---
class BaseUser(TypedDict):
    name: str
    age: int


class AdminUser(BaseUser):
    role: str


admin: AdminUser = {"name": "Alice", "age": 30, "role": "admin"}


# --- Практический пример: API-ответ ---
class ApiResponse(TypedDict):
    status: str
    data: dict
    error: str | None


def parse_response(response: dict) -> ApiResponse:
    return {
        "status": response.get("status", "unknown"),
        "data": response.get("data", {}),
        "error": response.get("error"),
    }


# Когда использовать:
# ? Type hints для словарей
# ? Документирование структуры
# ? Проверка mypy/pyright
# ? НЕ для runtime-проверки


# ============================================
# 8. USERDICT — ОБЁРТКА ДЛЯ НАСЛЕДОВАНИЯ
# ============================================

"""
UserDict — обёртка над dict для удобного наследования.
В отличие от dict, self — это словарь с атрибутом data.
"""

from collections import UserDict


class CaseInsensitiveDict(UserDict):
    """Словарь без учёта регистра ключей"""

    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __contains__(self, key):
        return super().__contains__(key.lower())


# Использование:
d = CaseInsensitiveDict()
d["Name"] = "Alice"
print(d["name"])  # Alice
print(d["NAME"])  # Alice
print("nAmE" in d)  # True


# --- Почему не наследовать от dict? ---
# dict реализован на C — некоторые методы игнорируют переопределения.
# UserDict — чистый Python, всё работает предсказуемо.

class LoggingDict(UserDict):
    """Словарь с логированием доступа"""

    def __getitem__(self, key):
        print(f"? Чтение ключа: {key}")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print(f"??  Запись: {key} = {value}")
        super().__setitem__(key, value)


log_dict = LoggingDict()
log_dict["a"] = 1
# ??  Запись: a = 1
print(log_dict["a"])
# ? Чтение ключа: a
# 1

# Когда использовать:
# ? Наследование от dict
# ? Переопределение методов
# ? Логирование доступа


# ============================================
# 9. СРАВНИТЕЛЬНАЯ ТАБЛИЦА
# ============================================

"""
????????????????????????????????????????????????????????????????????????
?  Тип                ?  Модуль  ?  Изменяемый? ?  Особенность         ?
????????????????????????????????????????????????????????????????????????
?  dict               ?  builtin ?  Да          ?  Стандарт            ?
?  OrderedDict        ?  coll.   ?  Да          ?  move_to_end()       ?
?  defaultdict        ?  coll.   ?  Да          ?  Авто-значение       ?
?  Counter            ?  coll.   ?  Да          ?  Подсчёт             ?
?  ChainMap           ?  coll.   ?  Частично    ?  Объединение         ?
?  MappingProxyType   ?  types   ?  Нет         ?  Read-only           ?
?  TypedDict          ?  typing  ?  Да          ?  Type hints          ?
?  UserDict           ?  coll.   ?  Да          ?  Наследование        ?
????????????????????????????????????????????????????????????????????????
"""

# ============================================
# 10. ЧТО ВЫБРАТЬ
# ============================================

"""
? Обычные задачи ? dict
   Хранение данных, доступ по ключу

? Подсчёт частоты ? Counter
   Слова, символы, теги

? Группировка ? defaultdict(list)
   Категории, теги, вложенные структуры

? Подсчёт с авто-инкрементом ? defaultdict(int)
   Счётчики, рейтинги

? Приоритеты конфигурации ? ChainMap
   Настройки по умолчанию + пользовательские

? Read-only конфигурация ? MappingProxyType
   Защита от случайных изменений

? Type hints ? TypedDict
   Документирование структуры

? Наследование ? UserDict
   Кастомное поведение

? Порядок + move_to_end ? OrderedDict
   LRU-кэш, очереди
"""

# ============================================
# 11. ПРАКТИЧЕСКИЙ ПРИМЕР: ВСЁ ВМЕСТЕ
# ============================================

from collections import Counter, defaultdict, ChainMap
from types import MappingProxyType
from typing import TypedDict


class LogEntry(TypedDict):
    """Запись лога"""
    level: str
    message: str
    timestamp: str


class LogAnalyzer:
    """Анализ логов с разными типами словарей"""

    def __init__(self):
        # Counter — подсчёт уровней
        self.level_counts = Counter()

        # defaultdict(list) — группировка по уровню
        self.by_level = defaultdict(list)

        # defaultdict(int) — подсчёт по часам
        self.hourly = defaultdict(int)

        # MappingProxyType — защита конфигурации
        self._config = {"max_entries": 1000, "truncate": True}
        self.config = MappingProxyType(self._config)

    def add(self, entry: LogEntry) -> None:
        """Добавить запись"""
        self.level_counts[entry["level"]] += 1
        self.by_level[entry["level"]].append(entry["message"])
        hour = entry["timestamp"][11:13]
        self.hourly[hour] += 1

    def summary(self) -> dict:
        """Сводка"""
        return {
            "levels": dict(self.level_counts),
            "top_level": self.level_counts.most_common(1),
            "hourly": dict(self.hourly),
        }


# Использование:
analyzer = LogAnalyzer()
analyzer.add({"level": "INFO", "message": "started", "timestamp": "2024-01-15T10:30:00"})
analyzer.add({"level": "ERROR", "message": "failed", "timestamp": "2024-01-15T10:31:00"})
analyzer.add({"level": "INFO", "message": "retry", "timestamp": "2024-01-15T11:00:00"})

print(analyzer.summary())
# {'levels': {'INFO': 2, 'ERROR': 1},
#  'top_level': [('INFO', 2)],
#  'hourly': {'10': 2, '11': 1}}

print(analyzer.config["max_entries"])  # 1000
# analyzer.config["max_entries"] = 999  # TypeError
