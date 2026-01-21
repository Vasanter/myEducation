from copy import copy, deepcopy

# fruits = ['apple', 'banana', 'cherry']
# fruits.append('watermelon')  # добавляем новый объект в список.
# print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'watermelon'] - изменяется первоначальный объект!


# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, 'watermelon')  # добавляем новый объект по индексу
# print(fruits)  # ['apple', 'watermelon', 'banana', 'cherry']


# my_string = "Hello, world! "
# new_string = my_string.replace("world", "Python")
# print(my_string)  # Hello, world! -первоначальная переменная осталась низменной!
# print(new_string)  # Hello, Python! - новая переменная!


# fruits = ['apple', 'banana', 'cherry']
# fruit = fruits.pop()
# print(fruit)  # cherry - строка 'cherry' присвоена переменной
# print(fruits)  # ['apple', 'banana'] - из первоначального списка удаляется последний объект


# fruits = ['apple', 'banana', 'cherry']
# fruit = fruits.pop(1)
# print(fruit)  # banana
# print(fruits)  # ['apple', 'cherry']


# fruits = ['apple', 'banana', 'cherry']
# fruits2 = ['fig', 'grape']
# fruits.extend(fruits2)  # добавляем элементы из одного списка в другой
# print(fruits)  # ['apple', 'banana', 'cherry', 'watermelon', 'fig', 'grape']


# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()  # изменяем порядок элементов в списке на противоположный
# print(fruits)  # ['cherry', 'banana', 'apple']


# my_list = [5, 4, 8, 10, 1, 2, 14, 4]
# my_list.sort() - сортируем по возрастанию
# print(my_list)  # [1, 2, 4, 4, 5, 8, 10, 14]
#
# my_list.sort(reverse=True) - сортируем по убыванию
# print(my_list)  # [14, 10, 8, 5, 4, 4, 2, 1]


# my_string = "My name is Alex"
# print(my_string.split(' '))  # ['My', 'name', 'is', 'Alex'] - разделение строки на несколько частей


# my_list = ["My", "name", "is", "Alex"]
# joined_string = "+".join(my_list)  # объединяем список из строк в одну строку с использованием указанного разделителя
# print(joined_string)  # My+name+is+Alex


# my_list = [5, 4, 8, 10, 1, 2, 14, 4]
# print(max(my_list))  # 14
# print(min(my_list))  # 1
# print(sum(my_list))  # 48
# print(sum(my_list) / len(my_list))  # 6.0 - среднее значение


# my_list = [5, 4, 8, 10, 1, 2, 14, "word"]
# print(sum(my_list))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# nums = [1, 5, 8, 2, 9, 3, 4, 7, 5, 6, 2, 9, 1, 8, 4, 3, 8]
# unique_nums = []  # пустой список, в который будут добавляться только уникальные значения из nums
#
# for i in nums:
#     if not (i in unique_nums):  # если элемента i в unique_nums нет ...
#         unique_nums.append(i)  # то он добавляется в unique_nums
#
# print(unique_nums)  # [1, 5, 2, 9, 3, 4, 7, 6, 8] - уникальные элементы
# print(sorted(unique_nums))  # [1, 2, 3, 4, 5, 6, 7, 8, 9] - сортируем по возрастанию


# test = list(map(int, input("Введите числа через пробел: ").split())) - генерируем список вручную
# print(test)


# Функция deepcopy из модуля copy создаёт полную независимую копию объекта, включая все вложенные изменяемые элементы,
# рекурсивно копируя каждый из них. В отличие от поверхностного копирования (copy.copy), которое копирует только
# верхний уровень контейнера и сохраняет ссылки на вложенные объекты, deepcopy создаёт новые копии всех уровней
# вложенности, предотвращая взаимосвязь между оригиналом и копией.
#
# Оригинал со вложенным изменяемым объектом
# original = [[1, 2], [3, 4]]
#
# # Поверхностная копия
# shallow = copy(original)
# shallow[0][0] = 99
# print(original[0][0])  # 99 (изменился оригинал!)
#
# # Глубокая копия
# deep = deepcopy(original)
# deep[0][0] = 88
# print(original[0][0])  # 99 (оригинал не изменился)
# print(deep[0][0])      # 88
