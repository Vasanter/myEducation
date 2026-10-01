"""
ДЕКОРАТОР @DEPRECATED — ПОМЕТКА УСТАРЕВШИХ ФУНКЦИЙ
=====================================================
PEP 702 добавляет декоратор @warnings.deprecated(), который помечает
класс или функцию как устаревшую.

Что это даёт:
- Статические анализаторы (mypy, pyright) предупреждают при использовании
- IDE показывает предупреждение прямо в редакторе
- Во время выполнения выдаётся DeprecationWarning
- Пользователь заранее узнаёт о необходимости миграции

?? Статус PEP 702:
- Final (принят 07-Nov-2023)
- Python 3.13+
- Для старых версий: pip install typing-extensions
"""

# ============================================
# 1. ВАРИАНТ С typing_extensions (рекомендуется)
# ============================================

# Работает на Python 3.8+:
# pip install typing-extensions

from typing_extensions import deprecated


@deprecated("Используйте new_add() вместо add()")
def add(x: int, y: int) -> int:
    """Устаревшая функция сложения"""
    return x + y


def new_add(x: int, y: int) -> int:
    """Новая функция сложения"""
    return x + y


if __name__ == "__main__":
    print(new_add(5, 7))  # ? 12 — без предупреждений

    print(add(5, 7))      # ?? DeprecationWarning + результат 12


# ============================================
# 2. ВАРИАНТ С warnings (Python 3.13+)
# ============================================

# В Python 3.13+ декоратор доступен в стандартном модуле warnings:

# from warnings import deprecated
#
# @deprecated("Use new_add instead")
# def add(x: int, y: int) -> int:
#     return x + y


# ============================================
# 3. ПАРАМЕТРЫ ДЕКОРАТОРА
# ============================================

"""
@deprecated(
    message,               # обязательный — сообщение о причине
    *,
    category=DeprecationWarning,  # класс предупреждения
    stacklevel=1,          # сколько кадров пропустить
)
"""

# --- Кастомный тип предупреждения ---
import warnings

class MyDeprecationWarning(DeprecationWarning):
    pass

# @deprecated("Устарело", category=MyDeprecationWarning)
# def old_func(): ...


# --- Без runtime-предупреждения (только для type checker) ---
# @deprecated("Устарело", category=None)
# def old_func(): ...
# Внимание: анализатор всё равно покажет предупреждение,
# но во время выполнения его НЕ будет.


# ============================================
# 4. ЧТО МОЖНО ПОМЕЧАТЬ
# ============================================

"""
? Поддерживается:
- Функции
- Методы классов
- Классы (при создании экземпляра)
- Свойства (property) и их сеттеры
- Перегрузки (overload)
- TypedDict, NamedTuple

? Не поддерживается:
- Модули целиком
- Отдельные атрибуты/константы
- Параметры функций (частично — через overload)
"""


# --- Пример: устаревший класс ---
@deprecated("Класс Ham устарел, используйте Spam")
class Ham:
    pass


class Spam:
    """Актуальная замена"""


# --- Пример: устаревший метод ---
class User:
    def get_name(self) -> str:
        return "Alice"

    @deprecated("Используйте get_name()")
    def get_username(self) -> str:
        return "alice"


# --- Пример: устаревшее свойство ---
class Config:
    @property
    @deprecated("Используйте settings")
    def config(self) -> dict:
        return {}

    @property
    def settings(self) -> dict:
        return {}


# ============================================
# 5. РАБОТА С ПЕРЕГРУЗКАМИ (OVERLOAD)
# ============================================

from typing import overload


@overload
@deprecated("Больше не принимает int, используйте str")
def process(x: int) -> str: ...


@overload
def process(x: str) -> str: ...


def process(x):
    return str(x)


# process(42)     # ?? предупреждение
# process("abc")  # ? без предупреждения


# ============================================
# 6. КАК ЭТО РАБОТАЕТ ПОД КАПОТОМ
# ============================================

"""
Декоратор @deprecated:

1. Устанавливает атрибут __deprecated__ с сообщением:
   func.__deprecated__ == "Используйте new_add() вместо add()"

2. Для функций — возвращает обёртку, которая вызывает
   warnings.warn() при вызове.

3. Для классов — оборачивает __new__, чтобы предупреждение
   появлялось при создании экземпляра.

4. Для property — оборачивает getter/setter.

Проверка вручную:
"""

from typing_extensions import deprecated as deprecated_ext

@deprecated_ext("Эта функция устарела")
def old_function():
    return 42

print(getattr(old_function, "__deprecated__", None))
# "Эта функция устарела"


# ============================================
# 7. ПОДАВЛЕНИЕ ПРЕДУПРЕЖДЕНИЙ
# ============================================

# --- Фильтр по категории ---
warnings.filterwarnings("ignore", category=DeprecationWarning)

# --- Контекстный менеджер ---
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    add(1, 2)  # без предупреждения


# --- В pytest ---
"""
# pytest.ini или pyproject.toml:
[tool.pytest.ini_options]
filterwarnings = [
    "ignore::DeprecationWarning",
    # или превратить в ошибки:
    "error::DeprecationWarning",
]
"""


# ============================================
# 8. ПОЛНЫЙ ПРИМЕР: МИГРАЦИЯ API
# ============================================

from typing_extensions import deprecated


class Calculator:
    """
    Калькулятор с устаревшими и новыми методами.

    Показывает типичный сценарий миграции API.
    """

    @deprecated("Используйте add() вместо plus()", version="2.0.0")
    def plus(self, a: int, b: int) -> int:
        """Устаревшее сложение"""
        return self.add(a, b)

    def add(self, a: int, b: int) -> int:
        """Актуальное сложение"""
        return a + b

    @deprecated("Используйте multiply() вместо times()")
    def times(self, a: int, b: int) -> int:
        """Устаревшее умножение"""
        return self.multiply(a, b)

    def multiply(self, a: int, b: int) -> int:
        """Актуальное умножение"""
        return a * b


def main():
    calc = Calculator()

    # Новый API — без предупреждений:
    print(f"add: {calc.add(2, 3)}")             # 5
    print(f"multiply: {calc.multiply(2, 3)}")   # 6

    # Старый API — предупреждения:
    print(f"plus: {calc.plus(2, 3)}")           # ?? 5
    print(f"times: {calc.times(2, 3)}")         # ?? 6


if __name__ == "__main__":
    main()


# ============================================
# 9. НАСТРОЙКА TYPE CHECKER
# ============================================

"""
--- mypy (mypy.ini) ---
[mypy]
# Показывать deprecation warnings
enable_error_code = deprecated

--- pyright (pyproject.toml) ---
[tool.pyright]
reportDeprecated = true
"""


# ============================================
# 10. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????????
?  @DEPRECATED (PEP 702) — ШПАРГАЛКА                       ?
????????????????????????????????????????????????????????????
?  ИМПОРТ:                                                 ?
?  Python 3.13+:  from warnings import deprecated          ?
?  Python < 3.13: from typing_extensions import deprecated ?
????????????????????????????????????????????????????????????
?  СИНТАКСИС:                                              ?
?  @deprecated("message")                                  ?
?  @deprecated("message", category=Warning)                ?
?  @deprecated("message", category=None)  # только type    ?
????????????????????????????????????????????????????????????
?  ЧТО ПОМЕЧАЕТ:                                           ?
?  • Функции и методы                                      ?
?  • Классы (при создании экземпляра)                      ?
?  • Свойства и их сеттеры                                 ?
?  • Перегрузки (@overload)                                ?
????????????????????????????????????????????????????????????
?  ПОВЕДЕНИЕ:                                              ?
?  • DeprecationWarning при вызове                         ?
?  • Предупреждение в IDE и mypy/pyright                   ?
?  • Атрибут __deprecated__ = message                      ?
????????????????????????????????????????????????????????????
?  ВАЖНО:                                                  ?
?  • Для старых Python — typing_extensions                 ?
?  • @deprecated идёт ПОСЛЕ @overload,                     ?
?    но ДО @property                                       ?
?  • Не поддерживает модули и константы                    ?
????????????????????????????????????????????????????????????
"""


# ============================================
# 11. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Неверный порядок с @property
# @deprecated("...")
# @property
# def x(self): ...
# # @deprecated должен быть ПОД @property (ближе к def)

# ? Решение:
class Example:
    @property
    @deprecated("Используйте new_x")
    def x(self) -> int:
        return 0


# ? Ошибка 2: Забыть про версию Python
# from warnings import deprecated  # ImportError на Python < 3.13

# ? Решение:
try:
    from warnings import deprecated
except ImportError:
    from typing_extensions import deprecated


# ? Ошибка 3: Использовать для side-effect'ов
# @deprecated("устарело")
# def log_and_return(x):
#     print(x)     # side-effect выполнится и при повторе
#     return x

# ? Решение: deprecated для чистых API-функций


# ? Ошибка 4: Игнорировать предупреждения в тестах
# pytest может проглотить их, и миграция затянется

# ? Решение в pytest.ini:
# filterwarnings = ["error::DeprecationWarning"]