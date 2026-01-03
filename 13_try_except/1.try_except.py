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
...
