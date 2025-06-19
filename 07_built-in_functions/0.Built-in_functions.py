"""ФУНКЦИИ ДЛЯ РАБОТЫ С ДАННЫМИ"""
'''int(), float(), str(), bool() – преобразование типов'''
# my_float = 1.9999
# my_int = int(my_float)  # преобразуем float в int
# print(my_int)  # 1


# my_int = 1
# my_float = float(my_int)  # преобразуем int в float
# print(my_float)  # 1.0


# nonsense = True
# print(int(nonsense))  # 1
# print(float(nonsense))  # 1.0
# print(str(nonsense))  # True | <class 'str'>


'''Математические функции'''
# print(abs(-5))   # 5, abs() –- модуль числа


# print(pow(2, 3))  # 8, pow() -- используется для возведения в степень


# my_float = 1.9999
# my_int = round(my_float)  #  round() используется для округления чисел
# print(my_int)  # 2


# my_float = 2.5
# my_int = round(my_float)
# print(my_int)  # 2


# min(), max(), sum() – минимум, максимум, сумма
# nums = [4, 2, 9, 5]
# print(min(nums))  # 2
# print(max(nums))  # 9
# print(sum(nums))  # 20


'''Работа с коллекциями'''
# print(len("Python"))  # 6 -- len используется для определения длины объекта (строка, список, словарь)
# print(len([1, 25, 39]))  # 3


# print(sorted([3, 1, 4]))  # [1, 3, 4], sorted() – сортировка
# print(sorted("hello", reverse=True))  # ['o', 'l', 'l', 'e', 'h'] -- reverse=True - для сортировки в обратном порядке


# names = ["Alice", "Bob"]
# ages = [25, 30]
# print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30)] -- zip() – объединение коллекций


'''Проверка условий'''
# nums = [2, 4, 6, 8]
# print(all(n % 2 == 0 for n in nums))  # True (все чётные) -- all(), any() – проверка условий для коллекций
# print(any(n > 5 for n in nums))  # True (есть числа > 5)


# x = 10
# print(isinstance(x, int))  # True -- isinstance() – проверка типа


'''Другие полезные функции'''
# print(list(range(5)))  # [0, 1, 2, 3, 4] -- range() – генерация последовательности чисел
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]


# help(print)  # покажет документацию для print()


# print(dir(str))  # все методы строки


# example = '5 + 2 * 8 ** 2'
# print(eval(example))  # 133 -- функция eval выполняет строку, переданную ему в качестве аргумента,
# как выражение на языке Python и возвращает результат выполнения.


# print(math.pi)  # 3.141592653589793
# print(f'{math.pi:.2f}')  # 3.14 -- округление


# large_number = 123456789
# print(f'{large_number:,}')  # 123,456,789 -- разделение

