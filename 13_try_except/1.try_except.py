# Конструкция try except finally — «подушка безопасности» вашего кода. Она позволяет обрабатывать ошибки, не прерывая
# выполнение программы. Как это работает:
# try: Здесь вы пишете код, который может вызвать ошибку (например, деление на ноль или открытие несуществующего файла).
# except: Этот блок сработает, только если внутри try произошел «баг». Здесь вы решаете, что делать с ошибкой.
# finally: Этот блок выполнится в любом случае, была ошибка или нет. Идеально подходит для «уборки»: закрытия файлов или
# сетевых соединений.


# ПРИМЕР 1:
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
#
# try:
#     print(a / b, " - calculation completed!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# ПРИМЕР 2:
# try:
#     a = int(input("Введите число: "))
#     b = int(input("Введите другое число: "))
#     print(a / b, " - расчет выполнен!")
# except ValueError as err:
#     print("Введите целое число!", err)
# except ZeroDivisionError as err:
#     print("Делить на ноль нельзя!", err)
# else:
#     print("ПОКА!")


# ПРИМЕР 3:
# age = int(input("Введите ваш возраст: "))
# if age < 0:
#     raise ValueError("Возраст не может быть отрицательным!")  # используется для принудительного вызова исключения
# print("Ваш возраст", age)


# ПРИМЕР 4:
# y = 0
#
# while y == 0:
#     try:
#         x = int(input("Enter first number: "))
#         y = int(input("Enter second number: "))
#         print(x / y)
#     except ValueError:
#         print("This is not an integer!")
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     finally:
#         print("DONE")
#
#
# def find_average(*, numbers: list) -> float:
#     return sum(numbers) / len(numbers)
#
#
# print(find_average(numbers=[1, 2, 3, 4, 5]))  # Output: 3.0
# # print(find_average([]))  # Output: ZeroDivisionError: division by zero
#
# try:
#     find_average(numbers=[])
# except ZeroDivisionError:
#     print("The list is empty")


# ПРИМЕР 5:
# def safe_division(a: int, b: int) -> float | None:  # аннотация типов
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         print(f'Ошибка: деление на ноль -> {e}')
#         return None
#
#
# print(safe_division(52,  0))
# print(safe_division(52,  20))
