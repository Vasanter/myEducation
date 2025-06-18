"""СРЕЗЫ"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[0:5])  # [0, 1, 2, 3, 4] - диапазон от первого элемента списка до пятого

# print(numbers[0:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - диапазон от 0 до 10
# print(numbers[0:len(numbers)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - полный список
# print(numbers[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - полный список
#
# print(numbers[:5])  # [0, 1, 2, 3, 4] - диапазон от первого элемента списка до пятого
# print(numbers[5:])  # [5, 6, 7, 8, 9] - диапазон от пятого элемента списка до последнего
#
# print(numbers[0:10:2])  # [0, 2, 4, 6, 8] - диапазон от 0 до 10 с шагом 2
# print(numbers[::2])  # [0, 2, 4, 6, 8] - берется полный список с шагом 2
#
# print(numbers[5:2])  # []
# print(numbers[0:20])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - диапазон от 0 до 20 выведет весь список из примера
# print(numbers[-5:-1])  # [5, 6, 7, 8] - для удобства чтения лучше использовать положительные значения!
# print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - элементы списка будут выведены в обратном порядке


# string = "Community university"
# print(string[4])  # u - индекс
# print(string[-2])  # t
# print(string[6:12])  # ity un - диапазон с 6го индекса по 12ый
# print(string[3:18:2])  # mnt nvri - диапазон + шаг
# print(string[::4])  # Cuyis
# print(string[::-1])  # ytisrevinu ytinummoC - строка наоборот


# ТРИ СПОСОБА РАЗВЕРНУТЬ СПИСОК
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1 СПОСОБ:
# new_numbers = num[::-1]
# print(new_numbers)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 2 СПОСОБ:
# num.reverse()
# print(num)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 3 СПОСОБ:
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = reversed(num)
# print(type(new_numbers))  # <class 'list_reverseiterator'>
# print(new_numbers)  # <list_reverseiterator object at 0x7f9b1c1b6a90>
# new_numbers = list(new_numbers)
# print(type(new_numbers))  # <class 'list'>
# print(new_numbers)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
