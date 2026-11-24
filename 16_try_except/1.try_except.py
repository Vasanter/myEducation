"""
ОБРАБОТКА ИСКЛЮЧЕНИЙ: TRY-EXCEPT-FINALLY
===========================================
Конструкция try-except-finally — «подушка безопасности» вашего кода.
Позволяет обрабатывать ошибки, не прерывая выполнение программы.

Как это работает:
- try:     код, который может вызвать ошибку
- except:  срабатывает, если в try произошла ошибка
- else:    выполняется, если ошибки НЕ было
- finally: выполняется ВСЕГДА (для «уборки»: закрытие файлов и т.д.)
"""

# ============================================
# 1. БАЗОВЫЙ СИНТАКСИС
# ============================================

# Простейший случай: try + except
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b, " - calculation completed!")
except ZeroDivisionError:
    print("You can't divide by zero!")


# ============================================
# 2. НЕСКОЛЬКО EXCEPT-БЛОКОВ
# ============================================

# Каждый except — для своего типа ошибки
try:
    a = int(input("Введите число: "))
    b = int(input("Введите другое число: "))
    print(a / b, " - расчёт выполнен!")
except ValueError as err:
    # Сработает, если введено не число
    print("Введите целое число!", err)
except ZeroDivisionError as err:
    # Сработает при делении на ноль
    print("Делить на ноль нельзя!", err)
else:
    # Выполнится, только если ОШИБКИ НЕ БЫЛО
    print("ПОКА!")


# ============================================
# 3. КОНСТРУКЦИЯ ELSE
# ============================================

"""
Порядок выполнения:
1. try       — всегда
2. except    — только при ошибке
3. else      — только если ошибки НЕ было
4. finally   — всегда (даже после return!)
"""

try:
    number = int("42")  # успешно
except ValueError:
    print("Ошибка преобразования")
else:
    print("Всё прошло успешно!")  # сработает
finally:
    print("Завершение блока")


# ============================================
# 4. ЯВНОЕ ВЫЗОВО ВЫЗОВА ИСКЛЮЧЕНИЯ — RAISE
# ============================================

# raise используется для принудительного вызова исключения
age = int(input("Введите ваш возраст: "))

if age < 0:
    raise ValueError("Возраст не может быть отрицательным!")

print("Ваш возраст", age)


# ============================================
# 5. ЦИКЛ С ОБРАБОТКОЙ ОШИБОК
# ============================================

y = 0

while y == 0:
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x / y)
    except ValueError:
        print("This is not an integer!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    finally:
        # Выполняется после каждой итерации — даже если была ошибка
        print("DONE")


# ============================================
# 6. ПРАКТИЧЕСКИЙ ПРИМЕР: ПОИСК СРЕДНЕГО
# ============================================

def find_average(*, numbers: list) -> float:
    """Находит среднее значение списка"""
    return sum(numbers) / len(numbers)


print(find_average(numbers=[1, 2, 3, 4, 5]))  # 3.0

# Пустой список вызовет ZeroDivisionError:
# print(find_average(numbers=[]))

# Обработка ошибки:
try:
    find_average(numbers=[])
except ZeroDivisionError:
    print("The list is empty")  # The list is empty


# ============================================
# 7. БЕЗОПАСНОЕ ДЕЛЕНИЕ
# ============================================

def safe_division(a: int, b: int) -> float | None:
    """
    Безопасное деление с обработкой ошибок.

    Returns:
        Результат деления или None при ошибке.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f'Ошибка: деление на ноль -> {e}')
        return None


print(safe_division(52, 0))   # Ошибка: деление на ноль -> division by zero
                               # None
print(safe_division(52, 20))  # 2.6


# ============================================
# 8. ОСНОВНЫЕ ТИПЫ ИСКЛЮЧЕНИЙ
# ============================================

"""
┌────────────────────────┬──────────────────────────────────────────┐
│  Исключение            │  Когда возникает                         │
├────────────────────────┼──────────────────────────────────────────┤
│  ValueError            │  Неверное значение (int("abc"))          │
│  TypeError             │  Неверный тип (1 + "2")                  │
│  ZeroDivisionError     │  Деление на ноль                         │
│  IndexError            │  Индекс вне диапазона ([1,2][5])         │
│  KeyError              │  Ключ не найден (dict["missing"])        │
│  FileNotFoundError     │  Файл не найден                          │
│  AttributeError        │  Атрибут не существует                   │
│  ImportError           │  Модуль не найден                        │
│  KeyboardInterrupt     │  Нажатие Ctrl+C                          │
│  Exception             │  Базовый класс для всех исключений       │
└────────────────────────┴──────────────────────────────────────────┘
"""


# ============================================
# 9. ПЕРЕХВАТ НЕСКОЛЬКИХ ИСКЛЮЧЕНИЙ
# ============================================

# Через кортеж:
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Ошибка: {e}")


# ============================================
# 10. ПОЛУЧЕНИЕ ИНФОРМАЦИИ ОБ ОШИБКЕ
# ============================================

try:
    x = int("abc")
except ValueError as e:
    print(f"Тип: {type(e).__name__}")  # ValueError
    print(f"Сообщение: {e}")           # invalid literal for int()
    print(f"Аргументы: {e.args}")      # ('invalid literal for int()...',)


# ============================================
# 11. ПОЛНЫЙ СИНТАКСИС TRY-EXCEPT-ELSE-FINALLY
# ============================================

def process_file(filename):
    """
    Полный пример с try-except-else-finally.

    Демонстрирует все четыре блока.
    """
    try:
        # Код, который может вызвать ошибку
        print(f"Открываем файл {filename}...")
        file = open(filename, "r")
        content = file.read()

    except FileNotFoundError:
        # Обработка конкретной ошибки
        print(f"Файл {filename} не найден!")

    except Exception as e:
        # Обработка всех остальных ошибок
        print(f"Неожиданная ошибка: {e}")

    else:
        # Выполняется, если ошибки НЕ было
        print(f"Файл прочитан: {len(content)} символов")
        return content

    finally:
        # Выполняется ВСЕГДА
        print("Завершение работы с файлом")
        try:
            file.close()
        except NameError:
            pass  # файл не был открыт


# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Ловить все исключения через голый except
# try:
#     risky_operation()
# except:              # ПЛОХО! Поймает даже Ctrl+C
#     pass

# ✅ Решение: указывать конкретные исключения
try:
    risky_operation()
except (ValueError, KeyError) as e:
    print(f"Ожидаемая ошибка: {e}")


# ❌ Ошибка 2: Использовать except для логики
# try:
#     value = 10 / 0
# except ZeroDivisionError:
#     value = 0  # лучше проверить заранее

# ✅ Решение: проверять условие заранее
b = 0
value = 10 / b if b != 0 else 0


# ❌ Ошибка 3: Игнорировать ошибку через pass
try:
    result = int("abc")
except ValueError:
    pass  # ОПАСНО! Ошибка скрыта

# ✅ Решение: логировать или обрабатывать
import logging
try:
    result = int("abc")
except ValueError as e:
    logging.warning(f"Не удалось преобразовать: {e}")
    result = None


# ❌ Ошибка 4: return в finally перезаписывает результат
def bad_function():
    try:
        return 1
    finally:
        return 2  # ПЛОХО! Вернёт 2, а не 1

print(bad_function())  # 2


# ✅ Решение: не использовать return в finally
def good_function():
    try:
        return 1
    finally:
        print("Уборка")  # без return


print(good_function())  # Уборка / 1


# ============================================
# 13. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  TRY-EXCEPT-FINALLY — ШПАРГАЛКА                          │
├──────────────────────────────────────────────────────────┤
│  СТРУКТУРА:                                              │
│  try:                                                    │
│      # код, который может упасть                         │
│  except SomeError:                                       │
│      # обработка конкретной ошибки                       │
│  except (Err1, Err2) as e:                               │
│      # обработка нескольких ошибок                       │
│  except Exception as e:                                  │
│      # обработка всех остальных                          │
│  else:                                                   │
│      # если ошибки НЕ было                               │
│  finally:                                                │
│      # выполняется ВСЕГДА                                │
├──────────────────────────────────────────────────────────┤
│  ПОРЯДОК ВЫПОЛНЕНИЯ:                                     │
│  1. try       — всегда                                   │
│  2. except    — только при ошибке                        │
│  3. else      — только если ошибки не было               │
│  4. finally   — всегда                                   │
├──────────────────────────────────────────────────────────┤
│  RAISE:                                                  │
│  raise ValueError("сообщение")                           │
│  raise  # повторный вызов текущего исключения            │
├──────────────────────────────────────────────────────────┤
│  ПОЛЕЗНО ЗНАТЬ:                                          │
│  • Ловите КОНКРЕТНЫЕ исключения, а не всё подряд         │
│  • finally выполнится даже после return                  │
│  • else не выполнится, если был return в try             │
│  • Не используйте голый except: без типа                 │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 14. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# 1. Безопасный ввод числа:
def get_integer(prompt: str) -> int | None:
    """Безопасный ввод целого числа"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Это не число! Попробуйте снова.")
        except KeyboardInterrupt:
            print("\nВвод прерван")
            return None


# 2. Безопасная работа с файлом:
def read_file_safe(filename: str) -> str | None:
    """Безопасное чтение файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except PermissionError:
        print(f"Нет доступа к {filename}")
    except UnicodeDecodeError:
        print(f"Ошибка кодировки в {filename}")
    return None


# 3. Валидация данных:
def validate_user_data(data: dict) -> bool:
    """Проверка корректности данных пользователя"""
    try:
        name = data["name"]
        age = int(data["age"])
        email = data["email"]

        if not name:
            raise ValueError("Имя не может быть пустым")
        if not 0 < age < 150:
            raise ValueError(f"Некорректный возраст: {age}")
        if "@" not in email:
            raise ValueError(f"Некорректный email: {email}")

        return True

    except KeyError as e:
        print(f"Отсутствует поле: {e}")
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    return False


print(validate_user_data({"name": "Alice", "age": 30, "email": "a@b.com"}))  # True
print(validate_user_data({"name": "", "age": 30, "email": "a@b.com"}))       # False


# 4. Повторные попытки с задержкой:
import time

def retry_operation(func, max_attempts: int = 3, delay: float = 1.0):
    """Повторяет операцию при ошибке"""
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            print(f"Попытка {attempt}/{max_attempts} неудачна: {e}")
            if attempt < max_attempts:
                time.sleep(delay)
    return None