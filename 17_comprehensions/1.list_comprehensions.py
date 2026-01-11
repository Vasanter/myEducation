# Списковые включения (list comprehensions) — это компактный и элегантный способ создания списков в Python.
# Они нужны для замены циклов for и map() при создании новых списков.


# squares = [x ** 2 for x in range(20)]
# print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]


# even_squares = [x ** 2 for x in range(30) if x % 2 == 0]
# print(even_squares)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]


# square_dict = {x: x ** 2 for x in range(11)}
# print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
# print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
