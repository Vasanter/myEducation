"""ЦИКЛ while"""
# Цикл for в Python используется для перебора (итерации) элементов какой-либо последовательности: списка, строки,
# кортежа, множества, словаря или результата функции range().

# for i in 'Нидерланды':  # будут вертикально выведены символы из строки
#     print(i)


# file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
# for file_name in file_names:
#     print(file_name)  # выводим весь список


# for i in range(1, 20, 3):  # перебор цифр от 1 до 20 с шагом 3
#     print(i, end=' ')  # 1 4 7 10 13 16 19, добавляем end чтобы вывести цифры горизонтально


# k = 0  # будет использоваться для подсчёта количества чисел, удовлетворяющих определённому условию
# for i in range(100):  # запускается цикл, который последовательно перебирает числа от 0 до 99 включительно
#     if i % 2 == 0:  # выбираем все четные числа (т.е. если остаток от деления числа i на 2 равен 0)
#         k += 1  # если число i чётное, то увеличиваем счётчик k на 1.
# print(k)  # 50 - количество четных чисел


# students = ["Alice", "Bob", "Charlie", "David"]
# for student in students:
#     print(student)
#     for char in student:  # вложенный цикл. Не рекомендуется делать много (> 1) вложенного цикла
#         print(char)


# greeting = 'Hello, World!'
# count_o = 0  # счетчик для символа 'o'
# for char in greeting:
#     if char == 'o':
#         count_o += 1
#         print(char)  # наглядно проверяем кол-во 'o' в строке
# print(count_o)  # 2 - количество 'о' в строке Hello, World!


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in numbers:
#     if num % 2 != 0:  # если число не четное, то ...
#         continue  # мы его пропускаем и ...
#     print(num)  # выводим только четные числа


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in numbers:
#     if num == 10:  # если число равно 10 ...
#         break  # -> разрываем цикл
#     print(num)


# генерация списка из целых чисел
# a = []
# for i in range(10):  # указываем кол-во чисел, которое будет в нашем списке
#     a.append(int(input()))
#     print(a)


# s = 0
# for x in range(10):
#     if x % 2 == 0:  # если x четный (т.е. 0, 2, 4, 6, 8), то ...
#         s += x  # складываем эти числа
# print(s)  # 20


# s = 0
# for x in [12, 15, 18, 7, 20, 11]:
#     if x % 2 == 0:  # если число из списка четное, то ...
#         s += x  # складываем эти числа
# print(s)  # 50


# k = 0
# for i in range(100):
#     if i > 70:
#         k += 1
# print(k)  # 29 - это кол-во цифр от 70 до 100 (не включительно), т.е 70, 71, 72 ... 98, 99


# m = -1000000000
# for x in [11, 13, 18, 24, 7, 10]:
#     if x % 2 == 0: # выбираем четные числа
#         if x > m:
#             m = x
# print(m)  # 24 - наибольшее из четных чисел


# a = []
# n = int(input('Сколько чисел в списке?: '))  # устанавливаем кол-во чисел в списке
# for i in range(n):
#     a.append(int(input("Введите число: \n")))
# print('Количество чисел:', len(a))
# print('Сумма чисел:', sum(a))
# print('Наибольшее из чисел:', max(a))
# print('Наименьшее из чисел:', min(a))


# Расчет среднего бала за контрольную среди n учеников
# n = int(input())  # считываем количество учеников
#
# total_score = 0
# for _ in range(n):
#     score = int(input())  # считываем оценку каждого ученика
#     total_score += score
#
# average_score = total_score / n  # рассчитываем средний балл
# print(average_score)


# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in num_list:
#     print(f'{num} - is a number!')


# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in num_list:
#     if num % 2 == 0:  # вывод четных чисел из списка
#         print(f'{num} - четное!')
#     else:
#         print(f'{num} - нечетное!')


# for letter in 'Hello Python!':
#     print('One more letter!')  # текст One more letter будет выводиться столько раз, сколько количество букв в строке


# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
#
# for letter_1, letter_2 in tuple_list:
#     print(letter_1, letter_2)


# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# for item in dictionary:
#     print(item)
#
# for item in dictionary.items():  # получаем пары ключ/значение
#     print(item)
#
# for item in dictionary.keys():  # получаем ключи
#     print(item)
#
# for item in dictionary.values():  # получаем значения
#     print(item)
#
# for i in range(5):
#     print(i)
#
# for i in range(3, 11, 2):  # диапазон (от 3 до 11) и шаг
#     print(i)
# print(range(1, 5))  # range(1, 5)
# print(list(range(1, 5)))  # [1, 2, 3, 4]
# print(set(range(1, 5)))  # {1, 2, 3, 4}
# print(tuple(range(1, 5)))  # (1, 2, 3, 4)
