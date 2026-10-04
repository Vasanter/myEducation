"""
constructions.py

Конспект статьи «Полезные конструкции Python, которые упростят работу с данными»
(https://habr.com/ru/companies/netologyru/articles/940890/)

Все примеры сгруппированы по уровням: базовый, средний, продвинутый.
"""

# ============================================================
# БАЗОВЫЕ ПРИЁМЫ
# ============================================================

# ------------------------------------------------------------
# 1. zip() — параллельный перебор коллекций
# ------------------------------------------------------------

# Пример 1. Параллельный перебор списков
players = ["Сергей", "Антон", "Михаил"]
teams = ["Волки", "Тигры", "Ястребы"]
scores = [15, 20, 17]

for player, team, score in zip(players, teams, scores):
    print(f"{player} ({team}) — {score} очков")

# Пример 2. Объединение строки и диапазона
letters = "Python"
positions = range(1, 7)

for letter, pos in zip(letters, positions):
    print(f"{pos}: {letter}")

# Пример 3. Создание словаря из двух списков
dates = ["2025-08-01", "2025-08-02", "2025-08-03"]
viewers = [1200, 980, 1430]

attendance = dict(zip(dates, viewers))
print(attendance)

# Пример 4. «Обратная» операция — разделение списка кортежей
points = [(2, 5), (4, 8), (1, 3)]
x_coords, y_coords = zip(*points)

print(x_coords)  # (2, 4, 1)
print(y_coords)  # (5, 8, 3)


# ------------------------------------------------------------
# 2. enumerate() — перебор с индексами
# ------------------------------------------------------------

# Пример 1. Нумерация строк в логе для поиска ошибок
log = [
    "INFO: старт системы",
    "WARNING: низкий заряд батареи",
    "ERROR: модуль датчика недоступен",
    "INFO: перезапуск",
    "ERROR: превышен лимит памяти",
]

for line_num, entry in enumerate(log, start=1):
    if entry.startswith("ERROR"):
        print(f"Строка {line_num}: {entry}")

# Пример 2. Сохранение исходного порядка при сортировке
products = ["Хлеб", "Сыр", "Молоко", "Шоколад"]
prices = [50, 320, 90, 150]

indexed_prices = list(enumerate(prices))
indexed_prices.sort(key=lambda x: x[1], reverse=True)

for index, price in indexed_prices:
    print(f"{products[index]} (позиция {index + 1}): {price} ?")

# Пример 3. Обновление элементов списка на месте
prices = [50, 120, 80, 200, 90]

for i, price in enumerate(prices):
    if price < 100:
        prices[i] = round(price * 1.1, 2)

print(prices)


# ------------------------------------------------------------
# 3. Списковые включения (list comprehension)
# ------------------------------------------------------------

# Пример 1. Преобразование цен
prices_rub = [1200, 850, 3100]
prices_usd = [round(price / 90, 2) for price in prices_rub]
print(prices_usd)

# Пример 2. Фильтрация с одновременным преобразованием
prices_rub = [1200, 850, 3100]
high_prices_usd = [round(p / 90, 2) for p in prices_rub if p > 1000]
print(high_prices_usd)

# Пример 3. Генерация списка по формуле
squares = [n ** 2 for n in range(1, 11)]
print(squares)

# Пример 4. Вложенные циклы
coords = [(x, y) for x in range(1, 3) for y in range(1, 4)]
print(coords)


# ------------------------------------------------------------
# 4. map() и filter() — преобразование и фильтрация
# ------------------------------------------------------------

# Пример 1. Перевод температур
temps_c = [0, 12, 24, 30]
temps_f = list(map(lambda t: round(t * 9 / 5 + 32, 1), temps_c))
print(temps_f)

# Пример 2. Фильтрация положительных чисел
numbers = [-5, 0, 7, -2, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)


# ============================================================
# СИНТАКСИЧЕСКИЕ СОКРАЩЕНИЯ
# ============================================================

# ------------------------------------------------------------
# 5. lambda — анонимные функции
# ------------------------------------------------------------

# Пример 1. Сортировка книг по длине названия
books = ["Война и мир", "Мастер и Маргарита", "Тихий Дон"]
sorted_books = sorted(books, key=lambda title: len(title))
print(sorted_books)

# Пример 2. Применение в map()
books = ["война и мир", "мастер и маргарита", "тихий дон"]
titles = list(map(lambda name: name.title(), books))
print(titles)

# Пример 3. Фильтрация с filter()
reviews = [
    "Отличная книга!",
    "Читал взахлёб, потрясающая история.",
    "Неплохо, но местами скучно.",
    "Самая сильная книга автора, советую.",
]

long_reviews = list(filter(lambda r: len(r) > 30, reviews))
print(long_reviews)

# Пример 4. Сортировка словарей по полю
authors = [
    {"name": "Лев Толстой", "sold": 5000000},
    {"name": "Михаил Шолохов", "sold": 3200000},
    {"name": "Михаил Булгаков", "sold": 4100000},
]

sorted_authors = sorted(authors, key=lambda a: a["sold"], reverse=True)
print(sorted_authors)


# ------------------------------------------------------------
# 6. Тернарный оператор (x if ... else y)
# ------------------------------------------------------------

# Пример 1. Прогноз погоды
temperature = -5
weather = "мороз" if temperature < 0 else "плюс"
print(weather)

# Пример 2. Статус бронирования
confirmed = False
status = "Подтверждено" if confirmed else "Ожидает подтверждения"
print(status)

# Пример 3. Расчёт стоимости доставки
order_total = 2800
delivery_cost = 0 if order_total > 3000 else 250
print(delivery_cost)


# ------------------------------------------------------------
# 7. Множественное присваивание
# ------------------------------------------------------------

# Пример 1. Распаковка данных из списка
courier_location = [55.7522, 37.6156]
lat, lon = courier_location
print(lat, lon)

# Пример 2. Обмен значений без временной переменной
first = "взрослый"
second = "ребёнок"
first, second = second, first
print(first, second)

# Пример 3. Перебор кортежей в цикле
orders = [
    ("Пицца Маргарита", "Анна"),
    ("Суши с лососем", "Игорь"),
    ("Шаверма", "Марина"),
]

for dish, client in orders:
    print(f"{client} заказал(а) {dish}")

# Пример 4. Игнорирование ненужных данных с _
order = ("Пицца Маргарита", "Анна", 650)
dish, client, _ = order
print(f"{client} заказал(а) {dish}")


# ============================================================
# СРЕДНИЙ УРОВЕНЬ
# ============================================================

# ------------------------------------------------------------
# 8. zip(*temps) — транспонирование таблицы
# ------------------------------------------------------------

temps = [
    [20, 21, 19],  # Москва, СПб, Казань
    [18, 20, 17],
    [22, 23, 21],
]

transposed = list(zip(*temps))
for row in transposed:
    print(row)


# ------------------------------------------------------------
# 9. Генераторы — экономия памяти
# ------------------------------------------------------------

# Пример 1. Генераторное выражение
books = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита"]
title_lengths = (len(title) for title in books)

for length in title_lengths:
    print(length)


# Пример 2. Функция-генератор с yield
def seat_numbers(rows, seats_per_row):
    for row in range(1, rows + 1):
        for seat in range(1, seats_per_row + 1):
            yield f"Ряд {row}, место {seat}"


for place in seat_numbers(2, 3):
    print(place)


# Пример 3. Чтение большого файла построчно
def read_orders(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


# Пример использования (раскомментируйте при наличии файла):
# for order in read_orders("orders_2025_08_09.txt"):
#     if "кофемашина" in order.lower():
#         print(f"Нашли заказ: {order}")


# ------------------------------------------------------------
# 10. Множества (set)
# ------------------------------------------------------------

# Пример 1. Удаление дубликатов
coffee_buyers = {"Анна", "Игорь", "Марина", "Олег", "Анна"}
print(coffee_buyers)

# Пример 2. Пересечение множеств
coffee_buyers = {"Анна", "Игорь", "Марина", "Олег"}
toaster_buyers = {"Марина", "Дмитрий", "Олег"}

both = coffee_buyers & toaster_buyers
print(both)

# Пример 3. Разность множеств
only_coffee = coffee_buyers - toaster_buyers
print(only_coffee)

# Пример 4. Объединение множеств
all_buyers = coffee_buyers | toaster_buyers
print(all_buyers)

# Пример 5. Проверка вхождения
if "Анна" in coffee_buyers:
    print("Анна покупала кофемашину")


# ------------------------------------------------------------
# 11. collections.Counter — подсчёт элементов
# ------------------------------------------------------------

from collections import Counter

# Пример 1. Подсчёт товаров в корзине
cart_items = [
    "кофемашина", "чайник", "кофемашина", "тостер",
    "чайник", "чайник", "кофемашина",
]

item_counts = Counter(cart_items)
print(item_counts)

top_items = item_counts.most_common(2)
print(top_items)

# Пример 2. Анализ слов в отзывах
reviews_text = """
Кофемашина отличная, работает тихо.
Чайник хороший, но кофемашина лучше.
Кофемашина выглядит стильно и варит вкусный кофе.
"""

words = reviews_text.lower().replace(".", "").split()
word_counts = Counter(words)
print(word_counts.most_common(3))


# ------------------------------------------------------------
# 12. collections.defaultdict — словарь со значением по умолчанию
# ------------------------------------------------------------

from collections import defaultdict

messages = [
    ("2025-08-08", "Встречаемся в 14:00"),
    ("2025-08-08", "Не забудь документы"),
    ("2025-08-09", "Презентация готова?"),
    ("2025-08-09", "Проверь почту"),
    ("2025-08-10", "Отправил отчёт"),
]

messages_by_date = defaultdict(list)

for date, text in messages:
    messages_by_date[date].append(text)

for date, texts in messages_by_date.items():
    print(date)
    for msg in texts:
        print(f"  - {msg}")


# ------------------------------------------------------------
# 13. Распаковка списков
# ------------------------------------------------------------

# Пример 1. Простая распаковка
pair = ["Москва", "Россия"]
city, country = pair
print(f"Город: {city}")
print(f"Страна: {country}")

# Пример 2. Расширенная распаковка с *
orders = ["Заказ #101", "Заказ #102", "Заказ #103", "Заказ #104"]

first, *rest = orders
print(f"Первый заказ: {first}")
print(f"Остальные заказы: {rest}")

# Пример 3. Распаковка в цикле (словарь)
capitals = {"Россия": "Москва", "Франция": "Париж"}

for country, capital in capitals.items():
    print(f"{capital} — столица {country}")

# Пример 4. Распаковка в цикле (zip)
students = ["Аня", "Борис", "Сергей"]
scores = [85, 92, 78]

for name, score in zip(students, scores):
    print(f"{name} — {score} баллов")


# ------------------------------------------------------------
# 14. *args и **kwargs
# ------------------------------------------------------------

# Пример 1. *args — произвольное количество позиционных аргументов
def total_score(*args):
    return sum(args)


print(total_score(5, 10, 15))   # три раунда
print(total_score(3, 7))        # два раунда


# Пример 2. **kwargs — произвольное количество именованных аргументов
def show_profile(name, **kwargs):
    print(f"Имя: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


show_profile("Анна", age=28, city="Москва", hobby="чтение")


# Пример 3. Комбинирование *args и **kwargs
def send_notifications(*args, **kwargs):
    for message in args:
        print(f"Отправка: {message}")
    print("Параметры доставки:", kwargs)


send_notifications(
    "Сервер перезапущен",
    "Новая версия задеплоена",
    channel="dev-team",
    priority="high",
    author="CI/CD бот",
)


# ============================================================
# ПРОДВИНУТЫЙ УРОВЕНЬ
# ============================================================

# ------------------------------------------------------------
# 15. Комбинация zip() и enumerate()
# ------------------------------------------------------------

players = ["Сергей", "Антон", "Михаил"]
teams = ["Волки", "Тигры", "Ястребы"]
scores = [15, 8, 17]

report = [
    f"{i}. {player} ({team}) — {score} очков"
    for i, (player, team, score) in enumerate(zip(players, teams, scores), start=1)
    if score > 10
]

for line in report:
    print(line)


# ------------------------------------------------------------
# 16. Комбинация map() и filter()
# ------------------------------------------------------------

# Пример 1. Цепочка обработки данных
raw_data = ["10", "15", "", "22", "9"]

result = list(
    filter(lambda x: x % 2 == 0,
           map(int, filter(None, raw_data)))
)

print(result)

# Пример 2. Обработка данных из CSV
orders = [
    {"name": "Анна", "amount": 1250},
    {"name": "Иван", "amount": 980},
    {"name": "Мария", "amount": 1430},
]

big_orders = list(
    map(lambda o: o["name"],
        filter(lambda o: o["amount"] > 1000, orders))
)

print(big_orders)


# ------------------------------------------------------------
# 17. with — управление ресурсами
# ------------------------------------------------------------

# Пример 1. Чтение файла
# with open("users.txt", encoding="utf-8") as file:
#     data = file.read()

# Пример 2. Запись покупок в файл
purchases = ["Ноутбук", "Беспроводная мышь", "Рюкзак для ноутбука"]

with open("last_purchases.txt", "w", encoding="utf-8") as file:
    for item in purchases:
        file.write(item + "\n")


# ------------------------------------------------------------
# 18. dataclasses — описание структур данных
# ------------------------------------------------------------

from dataclasses import dataclass


@dataclass(order=True)
class Runner:
    time: int
    name: str
    city: str


runners = [
    Runner(245, "Анна", "Москва"),
    Runner(230, "Игорь", "Казань"),
    Runner(260, "Марина", "СПб"),
]

print(sorted(runners))


# ------------------------------------------------------------
# 19. functools.partial — «заготовки» функций
# ------------------------------------------------------------

from functools import partial


# Пример 1. Отправка уведомлений
def send_notification(channel, message, user):
    print(f"[{channel}] {user}: {message}")


email_notify = partial(send_notification, "email")

email_notify("Ваш заказ готов", "Анна")
email_notify("Пароль успешно изменён", "Игорь")


# Пример 2. Форматирование даты
from datetime import datetime


def format_date(date_obj, fmt):
    return date_obj.strftime(fmt)


format_russian = partial(format_date, fmt="%d.%m.%Y")

today = datetime(2025, 8, 12)
print(format_russian(today))


# ------------------------------------------------------------
# 20. itertools — инструменты для итераторов
# ------------------------------------------------------------

from itertools import (
    chain,
    groupby,
    islice,
    accumulate,
    takewhile,
    zip_longest,
)
from operator import itemgetter

# Пример 1. chain — объединение последовательностей
orders_moscow = ["Заказ 101", "Заказ 102"]
orders_spb = ["Заказ 201", "Заказ 202"]

for order in chain(orders_moscow, orders_spb):
    print(f"Обрабатываем {order}")

# Пример 2. groupby — группировка данных
orders = [
    {"date": "2025-08-10", "order_id": 1, "amount": 1200},
    {"date": "2025-08-10", "order_id": 2, "amount": 800},
    {"date": "2025-08-11", "order_id": 3, "amount": 1500},
    {"date": "2025-08-11", "order_id": 4, "amount": 500},
    {"date": "2025-08-12", "order_id": 5, "amount": 2000},
]

orders.sort(key=itemgetter("date"))

for date, group in groupby(orders, key=itemgetter("date")):
    total_amount = sum(order["amount"] for order in group)
    print(f"{date}: всего заказов на {total_amount} руб.")

# Пример 3. islice — срез на итераторах
# with open("big_log.txt", encoding="utf-8") as f:
#     for line in islice(f, 5):
#         print(line.strip())

# Пример 4. accumulate — накопление промежуточных значений
sales = [1000, 2000, 1500, 3000]
cumulative = list(accumulate(sales))
print(cumulative)

# Пример 5. takewhile — отбор до первого несоответствия
temps = [
    (6, -3), (7, -1), (8, 0),
    (9, 2), (10, 4), (11, 5),
    (12, 5), (13, 4), (14, 3),
    (15, 2), (16, 1), (17, 0),
    (18, -1), (19, -2), (20, -3),
]

warm_hours = list(takewhile(lambda t: t[1] > 0, temps))
print(warm_hours)

# Пример 6. zip_longest — объединение с заполнением пропусков
authors = ["Анна", "Игорь", "Марина", "Дмитрий"]
articles = ["Python и данные", "Асинхронка в реальной жизни"]

for author, article in zip_longest(authors, articles, fillvalue="— нет статьи —"):
    print(f"{author}: {article}")