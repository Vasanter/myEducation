# В Python функция - это именованный блок кода, который выполняет определенную задачу. Он может принимать входные данные
# (аргументы), выполнять операции над ними и возвращать результат. Функции позволяют структурировать код, делая его
# более читаемым и многократно используемым.


# ПРИМЕР 1:
# numbers_1 = [1, 2, 3, 4, 5]
# average_1 = sum(numbers_1) / len(numbers_1)  # делим сумму чисел из списка на кол-во элементов из списка
# print(average_1)  # Output: 3.0 - среднее значение
#
# numbers_2 = [6, 7, 8, 9, 10]
# average_2 = sum(numbers_2) / len(numbers_2)
# print(average_2)  # Output: 8.0 - среднее значение


# Блоки кода одинаковы, отличие имеют только элементы списка. Выше написанный код можно оптимизировать создав функцию:
# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [6, 7, 8, 9, 10]
#
#
# def find_average(numbers):  # название функции => find_average
#     average = sum(numbers) / len(numbers)  # находим среднее значение
#     return average
#
#
# average_1 = find_average(numbers_1)
# average_2 = find_average(numbers_2)
# print(average_1, average_2, sep=' / ')  # Output: 3.0 / 8.0


# ПРИМЕР 2. Подсчет гласных букв в строке:
# def count_vowels(string):
#     vowels = 'аяуюоеёэиыАЯУЮОЕЁЭИЫ'  # гласные
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
#
#
# print(count_vowels("Привет Антон!"))  # Outputs: 4
# print(count_vowels("Простое предложение — это основная структурная единица синтаксиса, которая выражает законченную \
# мысль и содержит подлежащее и сказуемое."))  # Outputs: 55


# ПРИМЕР 3. Указываем аргументы функции:
# def welcome_message(name, age, location):  # название функции => welcome_message. Аргументы => name, age, location
#     print(f"Shalom, {name}. You are {age} and from {location}!")
#
#
# welcome_message('Valdo', 37, 'Belgium')  # Output: Shalom, Valdo. You are 37 years old!
# welcome_message('Ted', 30, 'Turkey')  # Output: Shalom, Ted. You are 30 and from Turkey!


# ПЛОХОЙ ПРИМЕР! - перепутали данные (день - месяц)
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

# ПРИМЕР 4. Явно указываем аргументы функции:
# def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
#     return f"{greeting}, {name}!"
#
#
# print(custom_greeting(name="John"))  # Hello, John!
# print(custom_greeting(name="John", greeting="Good morning"))  # Outputs: Good morning, John!
