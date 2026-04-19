# Декораторы — это инструмент для модификации поведения функций или классов без изменения их исходного кода.
# Основная идея: Декоратор "оборачивает" функцию, добавляя к ней дополнительное поведение до или после её выполнения.


# ПРОСТОЙ ПРИМЕР:
import time


def timer(func):  # создаем декоратор. Он принимает саму функцию (func) как объект, чтобы «обернуть» её новой логикой
    def wrapper(*args, **kwargs):  # создаем «матрешку». Звездочки позволяют обертке принимать любые аргументы, которые
        # могут быть у целевой функции.
        time_start = time.time()  # время наала работы функции
        func()  # Самый важный момент! Здесь реально выполняется код вашей функции (func_one или func_two).
        time_end = time.time()  # время окончания работы функции
        return f"Работа функции заняла {(time_end - time_start):.8f} секунд"  # вместо результата самой функции, декоратор
        # возвращает строку с разницей во времени

    return wrapper  # декоратор возвращает готовую «обертку». Теперь, когда вы вызываете func_one, Python на самом
    # деле вызывает wrapper.


@timer
def func_one():
    my_list = [i for i in range(1, 1000000)]


@timer
def func_two():
    my_list = [i for i in range(1, 1000000)]


print(func_one())
print(func_two())

#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# def say_hello():
#     print("Hello!")
#
#
# my_decorator(say_hello)()
#
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
#
# say_hello()
#
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_hello(*, name: str):
#     print(f"Hello, {name}!")
#
#
# say_hello(name="Sasha")
#
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def add_numbers(*, a: int, b: int) -> int:
#     print("Adding numbers...")
#     return a + b
#
#
# result = add_numbers(a=10, b=5)
# print(f"The result is {result}")
