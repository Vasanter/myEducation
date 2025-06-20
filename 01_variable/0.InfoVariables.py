"""Информация о переменных"""

# Переменная — это именованная ссылка на объект в памяти, у которой есть имя, тип и значение.
# Структурно она состоит из трёх частей:
# 1. Имя, или идентификатор — это название, придуманное программистом, чтобы обращаться к переменной. Например:
my_age = 25  # Здесь my_age - имя переменной, 25 - значение (тип - целое число)
# 2. Значение — это информация, которая хранится в памяти компьютера и с которой работает программа.
# Оно всегда принадлежит к какому-либо типу данных. Например:
myName = 'Vladimir'
print(type(myName))  # Output: <class 'str'> - строчный тип данных
# 3. Идентификатор — это номер ячейки памяти, в которой хранится значение переменной. Например:
print(id(myName))

# Стили именования:
# 1. snake_case - имена переменных, функций, методов, модулей
# 2. CamelCase - имена классов
# 3. yet-another-package - названия пакетов
# 4. CONSTANT - константы


# Правилам именования:
# 1. Первый символ должен быть заглавной или строчной латинской буквой или нижним подчёркиванием _ ;
# 2. Остальные символы могут быть заглавными или строчными латинскими буквами, нижними подчёркиваниями и цифрами;
# 3. Нельзя использовать пробелы;
# 4. Нельзя использовать ключевые слова для именования переменных (см. help('keywords'))

"""ПРИМЕР"""
# name = "Alice"
# years_old = 25
# print(name, years_old)  # Alice 25
# print(id(name))  # id объекта в памяти системы

"""ПРИМЕР ОШИБОК ПРИ ИСПОЛЬЗВАНИИ КЛЮЧЕВОГО СЛОВА В ОБОЗНАЧЕНИИ ПРЕМЕННОЙ"""
# print = 1
# print(1)  # TypeError: 'int' object is not callable

# while = 'string'
# print(while)  # SyntaxError: invalid syntax
