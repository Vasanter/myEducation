"""ПРЕОБРАЗОВАНИЕ ТИПА ДАННЫХ"""
# my_int = 1
# my_float = float(my_int)  # преобразуем int в float
# print(my_float)  # 1.0


# my_float = 1.9999
# my_int = int(my_float)  # преобразуем float в int
# print(my_int)  # 1


# nonsense = True
# print(int(nonsense))  # 1
# print(float(nonsense))  # 1.0
# print(str(nonsense))  # True | <class 'str'>


"""ПРИМЕРЫ ОКРУГЛЕНИЯ И РАЗДЕЛЕНИЯ ЧИСЕЛ"""
# my_float = 1.9999
# my_int = round(my_float)  # функция round() используется для округления чисел
# print(my_int)  # 2


# my_float = 1.4999
# my_int = round(my_float)
# print(my_int)  # 1


# print(math.pi)  # 3.141592653589793
# print(f'{math.pi:.2f}')  # 3.14


# large_number = 123456789
# print(f'{large_number:,}')  # 123,456,789


"""МОДУЛЬ ЧИСЛА"""
# x = -425
# print(abs(x))  # 425


"""ГЕНЕРИРУЕМ ПОСЛЕДОВАТЕЛЬНОСТЬ ЧИСЕЛ В ЗАДАННОМ ДИАПАЗОНЕ"""
# numbers = list(range(1, 20, 3))  # [1, 4, 7, 10, 13, 16, 19]
# print(numbers)
