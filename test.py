# import random
#
# secret_number = random.randint(1, 100)
# counter = 0
#
# print("Угадай число от 1 до 100!")
#
# while True:
#     user_input = input("Введите число: ")
#
#     if not user_input.isdigit():
#         print("Введите только числа!")
#         continue
#
#     guess = int(user_input)
#     counter += 1
#
#     if guess < secret_number:
#         print("Ваше число больше!")
#     elif guess > secret_number:
#         print("Ваше число меньше!")
#     else:
#         print(f"ПОЗДРАВЛЯЕМ! Вы угадали число за {counter} попыток.")
#         break

n = int(input("Введите число N: "))
total = 0

for i in range(1, 1 + n):
    total += i

print(f"Сумма чисел от 1 до {n} равна {total}!")
