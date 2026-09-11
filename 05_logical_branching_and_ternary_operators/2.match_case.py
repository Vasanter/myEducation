"""
КОНСТРУКЦИЯ MATCH-CASE В PYTHON (Python 3.10+)
================================================
Конструкция match-case используется для сопоставления шаблонов.
Делает код более понятным и структурированным при работе с множеством условий.

Основные применения:
1. Сопоставление значений — сравнение с конкретными значениями
2. Сопоставление структур данных — работа с кортежами, списками
3. Условия по типу — проверка типов объектов
4. Сопоставление с дополнительными условиями (guards)
"""

# ============================================
# 1. БАЗОВОЕ СОПОСТАВЛЕНИЕ ЗНАЧЕНИЙ
# ============================================

number = int(input("Введите число от 0 до 10: "))

match number:
    case 0:
        print("Ноль")
    case 1 | 2 | 3 | 4 | 5:  # использование | для нескольких значений
        print("Маленькое число")
    case 6 | 7 | 8 | 9:
        print("Большое число")
    case 10:
        print("Максимальное число")
    case _:  # default case (wildcard)
        print("Неопределённое число")


# ============================================
# 2. СОПОСТАВЛЕНИЕ СТРОК
# ============================================

command = input("Введите команду (start/stop/pause): ").lower().strip()

match command:
    case "start":
        print("Запуск программы...")
    case "stop":
        print("Остановка программы...")
    case "pause":
        print("Пауза")
    case "":
        print("Вы ничего не ввели!")
    case _:
        print(f"Неизвестная команда: {command}")


# ============================================
# 3. СОПОСТАВЛЕНИЕ С УСЛОВИЯМИ (GUARDS)
# ============================================

level = int(input("Введите этаж: "))

match level:
    case -1:
        print("Подвал")
    case 0:
        print("Паркинг")
    case 1:
        print("Ресепшн")
    case _ if 2 <= level <= 9:  # условие-ограничитель
        print("Чётный этаж") if level % 2 == 0 else print("Нечётный этаж")
    case 10:
        print("Технический этаж")
    case _:
        print("Такого этажа нет!")


# ============================================
# 4. СОПОСТАВЛЕНИЕ КОРТЕЖЕЙ И СПИСКОВ
# ============================================

# Координаты точки:
point = (0, 5)

match point:
    case (0, 0):
        print("Точка в начале координат")
    case (0, y):
        print(f"Точка на оси Y: {y}")
    case (x, 0):
        print(f"Точка на оси X: {x}")
    case (x, y) if x == y:
        print(f"Точка на диагонали: ({x}, {y})")
    case (x, y):
        print(f"Обычная точка: ({x}, {y})")


# Работа со списками:
numbers = [1, 2, 3]

match numbers:
    case []:
        print("Пустой список")
    case [first]:
        print(f"Список с одним элементом: {first}")
    case [first, second]:
        print(f"Список с двумя элементами: {first}, {second}")
    case [first, *rest]:  # распаковка остальных элементов
        print(f"Первый: {first}, Остальные: {rest}")


# ============================================
# 5. СОПОСТАВЛЕНИЕ СЛОВАРЕЙ
# ============================================

person = {"name": "Alice", "age": 30, "city": "New York"}

match person:
    case {"name": name, "age": age}:
        print(f"Имя: {name}, Возраст: {age}")
    case {"name": name}:
        print(f"Только имя: {name}")
    case _:
        print("Неизвестная структура")


# ============================================
# 6. СОПОСТАВЛЕНИЕ ПО ТИПУ
# ============================================

value = 42

match value:
    case int():
        print("Это целое число")
    case float():
        print("Это число с плавающей точкой")
    case str():
        print("Это строка")
    case bool():
        print("Это булево значение")
    case list():
        print("Это список")
    case _:
        print("Неизвестный тип")


# Сопоставление с проверкой значения:
match value:
    case int() if value > 0:
        print("Положительное целое число")
    case int() if value < 0:
        print("Отрицательное целое число")
    case int():
        print("Ноль")


# ============================================
# 7. КОМПЛЕКСНЫЕ ПРИМЕРЫ
# ============================================

# Калькулятор команд:
def process_command(command):
    match command.split():
        case ["add", a, b]:
            return int(a) + int(b)
        case ["subtract", a, b]:
            return int(a) - int(b)
        case ["multiply", a, b]:
            return int(a) * int(b)
        case ["divide", a, b]:
            return int(a) / int(b) if int(b) != 0 else "Деление на ноль"
        case _:
            return "Неизвестная команда"

print(process_command("add 5 3"))  # 8
print(process_command("subtract 10 4"))  # 6
print(process_command("multiply 3 7"))  # 21
print(process_command("divide 10 2"))  # 5.0
print(process_command("divide 10 0"))  # Деление на ноль
print(process_command("unknown"))  # Неизвестная команда


# Работа с JSON-подобными структурами:
response = {
    "status": "success",
    "data": {"user": "Alice", "id": 123}
}

match response:
    case {"status": "success", "data": {"user": user, "id": user_id}}:
        print(f"Успех! Пользователь: {user}, ID: {user_id}")
    case {"status": "error", "message": msg}:
        print(f"Ошибка: {msg}")
    case _:
        print("Неизвестный ответ")


# ============================================
# 8. ПРАКТИЧЕСКИЙ ПРИМЕР: ОБРАБОТКА ФИГУР
# ============================================

def calculate_area(shape):
    """Вычисление площади фигуры"""
    match shape:
        case {"type": "circle", "radius": r}:
            import math
            return math.pi * r ** 2
        case {"type": "rectangle", "width": w, "height": h}:
            return w * h
        case {"type": "square", "side": s}:
            return s ** 2
        case {"type": "triangle", "base": b, "height": h}:
            return 0.5 * b * h
        case _:
            return "Неизвестная фигура"

# Примеры использования:
print(f"Круг: {calculate_area({'type': 'circle', 'radius': 5}):.2f}")
print(f"Прямоугольник: {calculate_area({'type': 'rectangle', 'width': 10, 'height': 5})}")
print(f"Квадрат: {calculate_area({'type': 'square', 'side': 4})}")
print(f"Треугольник: {calculate_area({'type': 'triangle', 'base': 6, 'height': 8})}")


# ============================================
# 9. СРАВНЕНИЕ IF-ELIF-ELSE И MATCH-CASE
# ============================================

# Традиционный подход (if-elif-else):
def check_status_if(status):
    if status == 200:
        return "OK"
    elif status == 404:
        return "Not Found"
    elif status == 500:
        return "Internal Server Error"
    else:
        return "Unknown"

# Современный подход (match-case):
def check_status_match(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"

print(check_status_if(200))  # OK
print(check_status_match(200))  # OK


# ============================================
# 10. ОСОБЕННОСТИ И ОГРАНИЧЕНИЯ
# ============================================

# 1. Match-case работает только в Python 3.10+
# 2. Шаблоны должны быть литералами или константами
# 3. Каждый case выполняется только один раз (нет "проваливания" как в switch)

# Ошибка: нельзя использовать переменные в шаблонах напрямую:
# target = 5
# match number:
#     case target:  # Это не работает как ожидается!
#         print("Совпадение")

# Правильный способ с guard:
target = 5
match number:
    case _ if number == target:
        print(f"Совпадение с {target}")


# ============================================
# 11. МНОЖЕСТВЕННОЕ СОПОСТАВЛЕНИЕ
# ============================================

# Сопоставление нескольких шаблонов:
value = "hello"

match value:
    case "hello" | "hi" | "hey":
        print("Приветствие")
    case "bye" | "goodbye":
        print("Прощание")
    case str() as s if len(s) > 10:
        print(f"Длинная строка: {len(s)} символов")
    case _:
        print("Что-то другое")


# ============================================
# 12. СОПОСТАВЛЕНИЕ С РАСПАКОВКОЙ
# ============================================

# Распаковка кортежей разной длины:
def process_tuple(data):
    match data:
        case (a, b):
            print(f"Два элемента: {a}, {b}")
        case (a, b, c):
            print(f"Три элемента: {a}, {b}, {c}")
        case (first, *rest, last):
            print(f"Первый: {first}, Последний: {last}, Остальные: {rest}")

process_tuple((1, 2))
process_tuple((1, 2, 3))
process_tuple((1, 2, 3, 4, 5))


# Работа с вложенными структурами:
nested = [1, [2, 3], 4]

match nested:
    case [a, [b, c], d]:
        print(f"Вложенная структура: {a}, [{b}, {c}], {d}")
    case _:
        print("Не соответствует шаблону")