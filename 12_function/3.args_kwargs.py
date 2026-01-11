# *args и **kwargs — это специальные параметры в Python, которые позволяют функциям принимать переменное количество
# аргументов. Они очень полезны для создания гибких функций.


# def add_all(*args):  # *args собирает все позиционные аргументы в кортеж (tuple)
#     """Складываем все числа"""
#     summary = 0
#     for num in args:
#         summary += num
#     return summary
#
#
# print(add_all(1, 2, 3))  # 6
# print(add_all(1, 2, 3, 4, 5))  # 15
#
#
# values = [1, 2, 3, 4, 5]
# other_values = [6, 7, 8, 9, 10]
#
# print(add_all(*values))  # 15
# print(add_all(*values, *other_values))  # 55


# def introduce(**kwargs):  # **kwargs собирает все keyword-аргументы (аргументы с именами) в словарь (dict).
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
#
# introduce(name="John", age=30, city="New York")
#
# person = {
#     "city": "New York",
#     "age": 30,
#     "name": "John",
# }
#
# introduce(**person)


# def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
#     print(x, y)
#     print(args)
#     print(value)
#     print(kwargs)
#
#
# address = {
#     "city": "Moscow",
#     "street": "Red place",
#     "house": 12,
# }
#
# func_with_all_arguments(
#     *[3, 4, 5, 6, 7, 8, 9],
#     **address
# )


# def join_text(*strings, sep: str) -> str:
#     return sep.join(strings)
#
#
# def main() -> None:
#     print(join_text('A', 'B', 'C', 'D', sep=' - '))
#     print(join_text('ABC', sep=' '))
#     print(join_text('A', 'B', 'C', sep=' / '))
#
#
# if __name__ == '__main__':
#     main()
