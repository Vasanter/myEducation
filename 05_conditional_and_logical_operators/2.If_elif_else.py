"""УСЛОВНЫЙ ОПЕРАТОР"""
# Условный оператор if-elif-else в Python — это способ написать программный код так, чтобы он выдавал результат в
# зависимости от того, выполняется определенное условие или нет.
# Когда есть несколько условий, можно использовать elif (сокращение от else if — «иначе если»), чтобы проверять их
# поочередно. Если ни одно из условий не истинно, используют блок else, чтобы выполнить код по умолчанию.

# if True:
#     print("Hello, world!")  # Hello, world!


# if False:
#     print("Hello, world!")  # эта строка не будет выполнена


# message = "Hello, world!"  # True т.к. строка не пустая
# if message:
#     print("Сообщение не пустое!")


# x = 10
# y = 20
# if x > 0:
#     if y > 0:  # лучше так не писать, а писать в рамках одного условия, вот так => if x > 0 and y > 0:
#         print("x и y положительные")


# x = int(input("Введите число: "))
# if x > 0:
#     print("Число положительное")
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")


# name = input()
# if name:
#     print('Ты ввел =>', name)
# else:
#     print('Вы ничего не ввели!')


# x = 10
# y = 20
# if x > 0 and y > 0:  # оба условия должны быть выполнены
#     print("x и y положительные!")


# a = int(input("Введите число: "))
# if 10 <= a <= 20:
#     print('Число находиться в диапазоне между 10 и 20!')


# yesterday_temp = int(input())
# today_temp = int(input())
# if today_temp > yesterday_temp:
#     print("Сегодня теплее, чем вчера.")
# elif today_temp < yesterday_temp:
#     print("Сегодня холоднее, чем вчера.")
# else:
#     print("Сегодня такая же температура, как вчера.")


# age = int(input("Введите ваш возраст: "))
# has_licence = False
#
# if age >= 18:
#     if has_licence:
#         print('Вам разрешено водить автомобиль!')
#     else:
#         print('Сдайте на права!')
# else:
#     print('Вам нельзя водить!')


"""ПРИМЕР АВТОРИЗАЦИИ"""
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
#
# if login == 'Lanius' and password == '12345':
#     print(f'Добрый день {login}!')
# elif login != 'Lanius' and password == '12345':
#     print('Вы ввели неправильный логин!')
# elif login == 'Lanius' and password != '12345':
#     print('Вы ввели неправильный пароль!')
# else:
#     print('Неправильный логин и пароль!')
