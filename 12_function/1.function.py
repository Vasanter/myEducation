# В Python функция - это именованный блок кода, который выполняет определенную задачу. Он может принимать входные данные
# (аргументы), выполнять операции над ними и возвращать результат. Функции позволяют структурировать код, делая его
# более читаемым и многократно используемым.


# def connect():
#     """В случае есть функция еще не реализована вместо pass лучше писать саму причину"""
#     raise NotImplemented("Функция connect() не содержит кода")
#
#
# connect()


# ПРОСТЫЕ ПРИМЕРЫ
# 1. Объявление функции
# def greet(name):
#     """Эта функция приветствует пользователя"""
#     print(f"Привет, {name}!")
#
#
# # Вызов функции
# greet("Анна")  # Привет, Анна!


# 2. Аргументы по умолчанию
# def power(base, exponent=2):
#     return base ** exponent
#
#
# power(3)  # 9 (3 во 2 степени)
# power(3, 3)  # 27 (3 в 3 степени)


# 3.  Переменное количество аргументов
# def sum_all(*args):
#     return sum(args)
#
#
# sum_all(1, 2, 3)  # 6


# 4. Именованные аргументы с ** kwargs
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_info(name="Анна", age=25)
# Выведет: name: Анна
#           age: 25


# 5. Возврат нескольких значений (кортеж)
# def min_max(numbers):
#     return min(numbers), max(numbers)
#
#
# minimum, maximum = min_max([12, 3, 11, 5, 2, 16, 11, 10, 8, 4, 9])
# print(f"Наименьшее число => {minimum}. \nНаибольшее число => {maximum}.")


# ПРИМЕР 1.
# def some(number):
#     if number % 2 == 0:
#         return f'Число {number} - четное!'
#     else:
#         return f'Число {number} - не четное!'
#
#
# print(some(int(input("Enter a number: "))))


# ПРИМЕР 2. ПОДСЧЕТ СРЕДНЕГО ЗНАЧЕНИЯ
# numbers_1 = [1, 2, 3, 4, 5]
# average_1 = sum(numbers_1) / len(numbers_1)  # делим сумму чисел из списка на кол-во элементов из списка
# print("Среднее значение цифр из списка равно: ", average_1)  # 3.0
#
# numbers_2 = [6, 7, 8, 9, 10]
# average_2 = sum(numbers_2) / len(numbers_2)
# print("Среднее значение цифр из списка равно: ", average_2)  # 8.0


# # Т.к. блоки кода одинаковы, а отличие имеют только элементы списка, выше написанный код можно оптимизировать создав
# # функцию:
# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [6, 7, 8, 9, 10]
#
#
# def find_average(numbers):  # название функции => find_average
#     average = sum(numbers) / len(numbers)  # находим среднее значение
#     return average
#
#
# average_1 = find_average(numbers_1)  # вызываем функцию find_average с аргументом numbers_1
# average_2 = find_average(numbers_2)
#
# print(average_1, average_2, sep=' / ')  # 3.0 / 8.0


# ПРИМЕР 3. Подсчет гласных букв в строке
# def count_vowels(string):
#     vowels = 'аяуюоеёэиыАЯУЮОЕЁЭИЫ'  # гласные
#     count = 0  # переменная для подсчета гласных
#     for char in string:  # перебираем каждый символ (char) в строке string:
#         if char in vowels:  # если символ char находится в строке vowels
#             count += 1  # если условие истинно (символ является гласной), увеличиваем счетчик count на 1.
#     return count
#
#
# print(count_vowels("Привет Антон!"))  # 4
# print(count_vowels("Простое предложение — это основная структурная единица синтаксиса, которая выражает законченную \
# мысль и содержит подлежащее и сказуемое."))  # 55


# ПРИМЕР 4. Указываем аргументы функции
# def welcome_message(name, age, location):  # название функции => welcome_message. Параметры => name, age, location
#     print(f"Shalom, {name}. You are {age} and from {location}!")
#
#
# welcome_message('Valdo', 37, 'Belgium')  # Shalom, Valdo. You are 37 years old!
# welcome_message('Ted', 30, 'Turkey')  # Shalom, Ted. You are 30 and from Turkey!


# ПЛОХОЙ ПРИМЕР! - перепутали параметры (день - месяц)
# def format_date(day, month):
#     return f"The date is {day} of {month}."
#
#
# # При вызове функции, перепутали местами день и месяц!
# print(format_date(15, "October"))  # The date is 15 of October.
# print(format_date("January", 1))  # "The date is January of 1."


# ЧТОБЫ ПРЕДВИДЕТЬ ОШИБКУ МЫ МОЖЕМ ЯВНО ПРОПИСАТЬ ТИПЫ АРГУМЕНТОВ ФУНКЦИИ
# def format_date(*, day: int, month: str) -> str:  # * - используется для указания, что все последующие аргументы \
#     # должны быть переданы как именованные. Это означает, что мы не можем передавать значения для этих аргументов\
#     # по позиции, и должны использовать их имена при вызове функции. !!! -> str => означает тип возвращаемого значения
#     return f"The date is {day} of {month}."
#
#
# print(format_date(day=15, month="October"))  # The date is 15 of October.

# ПРИМЕР 5. Явно указываем аргументы функции
# * — специальный синтаксис, который означает что все параметры после * должны передаваться только
# как keyword-аргументы(по имени). Нельзя передать их как позиционные аргументы
# def custom_greeting(*, name: str, greeting: str = "Hello") -> str:  # -> str: функция возвращает значение типа str
#     return f"{greeting}, {name}!"
#
#
# print(custom_greeting(name="John"))  # Hello, John!
# print(custom_greeting(name="John", greeting="Good morning"))  # Good morning, John!


# ПРИМЕР 6. Конвертер валют
# def to_euro(amount):
#     rate = 92.09
#     return amount * rate
#
#
# def to_usd(amount):
#     rate = 78.23
#     return amount * rate
#
#
# print("Конвертер валют\n"
#       "1 - пара: EURO -> RUB\n"
#       "2 - пара: USD -> RUB")
#
# money = float(input("Введите сумму: "))
# choice = int(input("Выберите пару: "))
#
# if choice == 1:
#     print("При пересчете в рубли:", round(to_euro(money), 2))
# elif choice == 2:
#     print("При пересчете в рубли:", round(to_usd(money), 2))
# else:
#     print("Такой пары нет!")
