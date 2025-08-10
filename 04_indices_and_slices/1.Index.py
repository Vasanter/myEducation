"""ИНДЕКСЫ"""
# В Python индексы - это числовые значения, указывающие на позицию элемента в последовательности, такой как список,
# строка или кортеж. Индексация в Python начинается с 0, то есть первый элемент имеет индекс 0, второй - 1 и так далее.

#  0   1   2   3   4
#  H   e   l   l   o
# -5  -4  -3  -2  -1


fruits = ['apple', 'banana', 'cherry', 'watermelon']
# print(fruits[0])  # Output: 'apple'
# print(fruits[-3])  # Output: 'apple'
# print(fruits[3])  # Output: 'watermelon'
# print(fruits[4])  # Output: IndexError: list index out of range
# print(fruits[-5]) # Output: IndexError: list index out of range
#
# fruits[0] = 'pineapple'  # замена первого элемента списка
# print(fruits)  #  Output: ['pineapple', 'banana', 'cherry', 'watermelon']


# fruits = ['apple', 'banana', 'cherry', 'watermelon']
# fruits[0], fruits[3] = fruits[3], fruits[0]  # смена первого и последнего элемента в списке
# print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'apple']
