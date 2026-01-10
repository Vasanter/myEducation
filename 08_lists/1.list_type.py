"""Список (list)"""
# Это упорядоченная изменяемая коллекция элементов, которые могут быть любого типа: числа, строки, объекты, другие
# списки и т.д.

# Основные свойства списков:
# Упорядоченность: Элементы хранятся в определённом порядке, индексация начинается с 0.
# Изменяемость: Можно изменять элементы, добавлять и удалять их.
# Гибкость: В одном списке могут быть элементы разных типов, включая вложенные списки (НО ЛУЧШЕ ТАК НЕ ДЕЛАТЬ!)


# my_list = list()
# print(my_list)  # [] - пустой список


# word = "Hello"
# my_list = list(word)
# print(my_list)  # ['H', 'e', 'l', 'l', 'o'] - выводим символы из строки "Hello" как отдельный элемент списка


# print(bool([]))  # False
# print(bool([0]))  # True


# my_list = [1, "apple", True, 1.5, [1, 2, 3]]
# print(my_list)  # [1, "apple", True, 1.5, [1, 2, 3] - списки могут содержать элементы любого типа
# print(1.5 in my_list)  # True --проверяем что элемент есть списке
# print("banana" in my_list)  # False


# list_1 = [1, 2, 3]
# list_2 = [1, 3, 2]
# list_3 = [1, 2, 3]
# print(list_1 == list_2)  # False
# print(list_1 == list_3)  # True


# my_list = ['apple', 'banana', 'cherry']
# print('banana' in my_list)  # True - с помощью in проверяем есть ли слово в списке
# print('watermelon' in my_list)  # False


# element_1 = "apple"
# element_2 = "banana"
# element_3 = "cherry"
# my_list = [element_1, element_2, element_3]
# print(my_list)  # ['apple', 'banana', 'cherry']


# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = list_1 + list_2
# print(list_3)  # [1, 2, 3, 4, 5, 6]


# squares = [x**2 for x in range(5)]  # генерируем список из чисел от 0 до 4 и возводим их во вторую степень
# print(squares)  # [0, 1, 4, 9, 16]

