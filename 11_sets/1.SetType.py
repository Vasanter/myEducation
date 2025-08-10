# Множество — это изменяемая структура данных, которая содержит уникальные и неупорядоченные элементы. Множества
# полезны в случаях, когда нужно быстро проверить наличие элемента или удалить дубликаты из больших объёмов данных.

# my_set = {1, 2, 3, 4, 5}
# print(type(my_set))
# print(my_set)  # Output: {1, 2, 3, 4, 5}


# my_set = set()
# for i in range(5):
#     my_set.add(i)
# print(my_set)  # {1, 2, 3, 4, 5}


# my_set = {0, 1, 2, 3, 4}
# my_set.add(2)  # добавляем 2
# print(my_set)  # {0, 1, 2, 3, 4}


# set1 = {1, 2, 4, 8, 7}
# set2 = {3, 4, 5, 1, 9}
#
# print(set1.union(set2))  # {1, 2, 3, 4, 5, 9} - объединяем списки
# print(set1.intersection(set2))  # {1, 4} - повторяющиеся элементы
#
# united_set = set1.union(set2)
# print(len(united_set))  # 8 - элементов в объединенном списке
# print(set1.difference(set2))  # {8, 2, 7} - возвращает множество, полученное из элементов, по которым первое
# # множество отличается от второго


# squares = {x ** 2 for x in range(10)}
# print(squares)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


# print({1, 2, 3} == {3, 2, 1})  # True
# my_set = {1, 2, 3}


# numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
# unique_numbers = set(numbers)
# print(unique_numbers)  # {1, 2, 3, 4, 5, 6, 7}
# unique_numbers = list(unique_numbers)
# print(unique_numbers)  # [1, 2, 3, 4, 5, 6, 7]
