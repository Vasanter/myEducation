"""СЛОЖЕНИЕ СТРОК / КОНКАТЕНАЦИЯ"""
# Это операция объединения двух или более строк в одну новую строку.
# print('Hello ' + 'World!', 'My name is ' + 'John ))')  # Output: Hello World. My name is John!


"""Метод format (устаревший)"""
# name = input("Как тебя зовут?: ")
# age = int(input("Сколько тебе лет?: "))
#
# print('Вас зовут {} и вам {}!'.format(name, age))


"""F-СТРОКИ (с версии 3.6)"""
# name = input("Введите ваше имя: \n")
# surname = input("Введите вашу фамилию: \n")
# print(f"Приветствую тебя, {name} {surname}!")


# print(f"Результат: {2*37}")  # Output: Результат: 74


# Можно вызывать методы!
# value = 'СтРоЧка'
# print(f"Вы ввели: {value.lower()}")  # Output: Вы ввели: строчка


# import datetime
#
# today = datetime.datetime.today()
# print(f"Текущее время: {today:%H:%M:%S %d-%m-%Y }")  # Output: Текущее время: 12:57:57 05-12-2024
# print(f"Текущий год: {today:%Y}-ый")  # Output: Текущий год: 2025-ый


"""СЫРЫЕ СТРОКИ"""
# print(r"Как пройти в \"библиотеку?\"")  # Output: Как пройти в \"библиотеку?\""сырые" строки - подавляют экранирование
