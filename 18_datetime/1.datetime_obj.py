"""
РАБОТА С ДАТОЙ И ВРЕМЕНЕМ В PYTHON
=====================================
Модули datetime и time для работы с датами, временем и интервалами.
"""

import datetime
import time

# ============================================
# 1. ПОЛУЧЕНИЕ ТЕКУЩЕГО ВРЕМЕНИ
# ============================================

# --- UTC (рекомендуется для серверов) ---
utc_time = datetime.datetime.now(datetime.UTC)
print(f"UTC (рекомендуется для серверов): {utc_time}")  # 2024-01-15 10:30:45.123456+00:00

# --- Локальное время ---
current_datetime = datetime.datetime.now()
print(f'Локальное время: {current_datetime}')  # 2024-01-15 13:30:45.123456

# --- Текущая дата ---
current_date = datetime.date.today()
print(f'Текущая дата: {current_datetime}')  # 2024-01-15

# ============================================
# 2. КОМПОНЕНТЫ ДАТЫ И ВРЕМЕНИ
# ============================================

current_datetime = datetime.datetime.now()

print(f"Год:         {current_datetime.year}")  # 2024
print(f"Месяц:       {current_datetime.month}")  # 1
print(f"День:        {current_datetime.day}")  # 15
print(f"Час:         {current_datetime.hour}")  # 13
print(f"Минута:      {current_datetime.minute}")  # 30
print(f"Секунда:     {current_datetime.second}")  # 45
print(f"Микросекунда:{current_datetime.microsecond}")  # 123456

# День недели (1 = понедельник, 7 = воскресенье):
print(f"День недели: {current_datetime.weekday() + 1} - {current_datetime.strftime("%A")}")  # 1 - Monday


# Номер дня в году:
print(f"День года:   {current_datetime.timetuple().tm_yday}")

# ============================================
# 3. СОЗДАНИЕ ДАТЫ ВРУЧНУЮ
# ============================================

some_datetime = datetime.datetime(
    year=2021, month=5, day=1,
    hour=12, minute=30, second=15,
    microsecond=123456
)
print(some_datetime)  # 2021-05-01 12:30:15.123456

# Только дата:
some_date = datetime.date(2021, 5, 1)
print(f"Только дата: {some_date}")  # 2021-05-01

# Только время:
some_time = datetime.time(12, 30, 15)
print(f"Только время: {some_time}")  # 12:30:15

# ============================================
# 4. ФОРМАТИРОВАНИЕ (STRFTIME)
# ============================================

current_datetime = datetime.datetime.now()

# ISO-формат:
print(f"ISO-формат: {current_datetime.isoformat()}")
# 2024-01-15T13:30:45.123456

# Пользовательский формат:
print(f"Пользовательский формат: {current_datetime.strftime("%A, %d %B %Y")}")  # Monday, 15 January 2024

print(current_datetime.strftime("%d.%m.%Y %H:%M"))  # 15.01.2024 13:30

print(current_datetime.strftime("%Y-%m-%d"))  # 2024-01-15

# Основные коды формата:
"""
┌──────┬──────────────────────────────────────┬────────────────────┐
│ Код  │ Значение                             │ Пример             │
├──────┼──────────────────────────────────────┼────────────────────┤
│ %Y   │ Год (4 цифры)                        │ 2024               │
│ %m   │ Месяц (01-12)                        │ 01                 │
│ %d   │ День (01-31)                         │ 15                 │
│ %H   │ Час (00-23)                          │ 13                 │
│ %M   │ Минута (00-59)                       │ 30                 │
│ %S   │ Секунда (00-59)                      │ 45                 │
│ %f   │ Микросекунда                         │ 123456             │
│ %A   │ День недели (полное)                 │ Monday             │
│ %a   │ День недели (кратко)                 │ Mon                │
│ %B   │ Месяц (полное название)              │ January            │
│ %b   │ Месяц (кратко)                       │ Jan                │
│ %j   │ День года (001-366)                  │ 015                │
│ %p   │ AM/PM                                │ PM                 │
│ %%   │ Символ %                             │ %                  │
└──────┴──────────────────────────────────────┴────────────────────┘
"""

# ============================================
# 5. ПАРСИНГ (STRPTIME / FROMISOFORMAT)
# ============================================

# --- Из ISO-формата ---
iso_format = "2023-08-07T20:15:30.384294"
my_datetime = datetime.datetime.fromisoformat(iso_format)
print(type(my_datetime))  # <class 'datetime.datetime'>
print(my_datetime)  # 2023-08-07 20:15:30.384294

# --- Из произвольного формата ---
date_string = "15.01.2024 13:30"
parsed = datetime.datetime.strptime(date_string, "%d.%m.%Y %H:%M")
print(parsed)  # 2024-01-15 13:30:00

# --- Только дата ---
date_string = "2024-01-15"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print(parsed_date)  # 2024-01-15

# ============================================
# 6. АРИФМЕТИКА ДАТ (TIMEDELTA)
# ============================================

current_datetime = datetime.datetime.now()

# --- Вычитание ---
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)  # 2024-01-14 13:30:45.123456

week_ago = current_datetime - datetime.timedelta(weeks=1)
month_later = current_datetime + datetime.timedelta(days=30)
hours_later = current_datetime + datetime.timedelta(hours=5)

# --- Комбинирование ---
complex_delta = datetime.timedelta(days=1, hours=2, minutes=30)
result = current_datetime + complex_delta

# --- Разница между датами ---
start = datetime.datetime(2024, 1, 1)
end = datetime.datetime(2024, 1, 15)
diff = end - start

print(diff.days)  # 14
print(diff.total_seconds())  # 1209600.0

# --- Параметры timedelta ---
"""
datetime.timedelta(
    days=0,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0,
)
"""

# ============================================
# 7. ЗАМЕР ВРЕМЕНИ (TIME)
# ============================================

# --- time.monotonic() — монотонный таймер (не зависит от системного времени) ---
start_time = time.monotonic()
time.sleep(1)
elapsed = time.monotonic() - start_time
print(f"Time taken: {elapsed:.3f} seconds")
# Time taken: 1.001 seconds


# --- time.perf_counter() — самый точный таймер ---
start = time.perf_counter()
time.sleep(0.5)
elapsed = time.perf_counter() - start
print(f"Perf: {elapsed:.6f}")
# Perf: 0.501234


# ============================================
# 8. СРАВНЕНИЕ ТАЙМЕРОВ
# ============================================

"""
┌────────────────────────┬──────────────────────────────────────────┐
│  Функция               │  Назначение                              │
├────────────────────────┼──────────────────────────────────────────┤
│  time.time()           │  Системное время (может измениться NTP)  │
│  time.monotonic()      │  Монотонный таймер (только вперёд)       │
│  time.perf_counter()   │  Наивысшая точность для бенчмарков       │
│  time.process_time()   │  Время CPU процесса                      │
│  time.thread_time()    │  Время CPU текущего потока               │
└────────────────────────┴──────────────────────────────────────────┘

Для измерения интервалов:
✅ time.monotonic()
✅ time.perf_counter()

Для получения текущего времени:
✅ datetime.datetime.now()
✅ time.time()
"""

# ============================================
# 9. ЧАСОВЫЕ ПОЯСА
# ============================================

# --- UTC ---
utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)  # 2024-01-15 10:30:45.123456+00:00

# --- С часовым поясом ---
from datetime import timezone, timedelta

moscow_tz = timezone(timedelta(hours=3))
moscow_time = datetime.datetime.now(moscow_tz)
print(moscow_time)  # 2024-01-15 13:30:45.123456+03:00

# --- Конвертация между поясами ---
utc = datetime.datetime.now(datetime.UTC)
moscow = utc.astimezone(moscow_tz)
print(f"UTC:    {utc}")
print(f"Москва: {moscow}")


# ============================================
# 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# --- 1. Бенчмарк функции ---
def benchmark(func, *args, **kwargs):
    """Измеряет время выполнения функции"""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"⏱️  {func.__name__}: {elapsed * 1000:.3f} мс")
    return result


benchmark(sum, range(1_000_000))


# --- 2. Форматирование "сколько прошло" ---
def time_ago(dt: datetime.datetime) -> str:
    """Возвращает человекочитаемое 'сколько прошло'"""
    now = datetime.datetime.now(datetime.UTC)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.UTC)

    delta = now - dt
    seconds = delta.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} секунд назад"
    elif seconds < 3600:
        return f"{int(seconds / 60)} минут назад"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} часов назад"
    elif seconds < 604800:
        return f"{int(seconds / 86400)} дней назад"
    else:
        return dt.strftime("%d.%m.%Y")


now = datetime.datetime.now(datetime.UTC)
print(time_ago(now - datetime.timedelta(seconds=30)))  # 30 секунд назад
print(time_ago(now - datetime.timedelta(minutes=5)))  # 5 минут назад
print(time_ago(now - datetime.timedelta(hours=3)))  # 3 часов назад
print(time_ago(now - datetime.timedelta(days=2)))  # 2 дней назад

# --- 3. Парсинг логов ---
log_line = "[2024-01-15 13:30:45] ERROR: Something went wrong"
timestamp_str = log_line[1:20]
timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
print(f"Лог записан: {timestamp}")


# --- 4. Генерация диапазона дат ---
def date_range(start: datetime.date, end: datetime.date):
    """Генерирует все даты между start и end"""
    current = start
    while current <= end:
        yield current
        current += datetime.timedelta(days=1)


for d in date_range(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 1, 5)
):
    print(d)


# --- 5. Проверка "сегодня ли" ---
def is_today(dt: datetime.datetime) -> bool:
    """Проверяет, является ли дата сегодняшней"""
    return dt.date() == datetime.date.today()


print(is_today(datetime.datetime.now()))  # True


# --- 6. Возраст по дате рождения ---
def calculate_age(birth_date: datetime.date) -> int:
    """Вычисляет возраст по дате рождения"""
    today = datetime.date.today()
    age = today.year - birth_date.year

    # Ещё не было дня рождения в этом году:
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


print(calculate_age(datetime.date(1990, 5, 15)))  # зависит от текущей даты

# ============================================
# 11. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  ДАТА И ВРЕМЯ — ШПАРГАЛКА                                │
├──────────────────────────────────────────────────────────┤
│  ПОЛУЧЕНИЕ:                                              │
│  datetime.datetime.now()           — локальное время     │
│  datetime.datetime.now(datetime.UTC)— UTC                │
│  datetime.date.today()             — сегодня            │
├──────────────────────────────────────────────────────────┤
│  СОЗДАНИЕ:                                               │
│  datetime.datetime(2024, 1, 15, 13, 30)                  │
│  datetime.timedelta(days=1, hours=2)                     │
├──────────────────────────────────────────────────────────┤
│  ФОРМАТИРОВАНИЕ:                                         │
│  dt.strftime("%d.%m.%Y %H:%M")      — в строку           │
│  datetime.strptime(s, fmt)           — из строки         │
│  dt.isoformat()                      — ISO-формат        │
│  datetime.fromisoformat(s)           — из ISO            │
├──────────────────────────────────────────────────────────┤
│  АРИФМЕТИКА:                                             │
│  dt + timedelta(days=1)   — прибавить                    │
│  dt - timedelta(hours=5)  — отнять                       │
│  dt2 - dt1                — разница (timedelta)          │
│  delta.days               — дней                         │
│  delta.total_seconds()    — секунд                       │
├──────────────────────────────────────────────────────────┤
│  ЗАМЕР ВРЕМЕНИ:                                          │
│  time.monotonic()       — монотонный таймер              │
│  time.perf_counter()    — точный таймер                  │
│  time.process_time()    — CPU процесса                   │
└──────────────────────────────────────────────────────────┘
"""

# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: time.time() для бенчмарков
start = time.time()
time.sleep(1)
print(time.time() - start)  # может «прыгнуть» из-за NTP

# ✅ Решение:
start = time.perf_counter()
time.sleep(1)
print(time.perf_counter() - start)

# ❌ Ошибка 2: naive vs aware datetime
naive = datetime.datetime.now()
aware = datetime.datetime.now(datetime.UTC)
# print(naive - aware)  # TypeError: can't subtract offset-naive and offset-aware

# ✅ Решение: всегда используйте aware с UTC
now = datetime.datetime.now(datetime.UTC)


# ❌ Ошибка 3: timedelta(months=1) не существует
# delta = datetime.timedelta(months=1)  # TypeError!

# ✅ Решение: вручную
def add_months(dt: datetime.datetime, months: int) -> datetime.datetime:
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    day = min(dt.day, 28)  # упрощённо
    return dt.replace(year=year, month=month, day=day)


# ❌ Ошибка 4: Путаница strftime/strptime
# strftime — строка из даты
# strptime — дата из строки

# ✅ Мнемоника:
# strftime = STRing From TIME
# strptime = STRing Parse TIME


# ❌ Ошибка 5: Парсинг без try/except
# datetime.datetime.strptime("invalid", "%Y-%m-%d")  # ValueError

# ✅ Решение:
try:
    dt = datetime.datetime.strptime("invalid", "%Y-%m-%d")
except ValueError as e:
    print(f"Ошибка парсинга: {e}")
