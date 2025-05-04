# Из булевых операторов, not имеет самый высокий приоритет, а or самый низкий!


# AND - возвращает True, если оба условия истинны, иначе возвращает False
# age = 22
# weight = 58
# result = age > 21 and weight == 58
# print(result)  # True

# OR - возвращает False, если оба условия ложны, иначе возвращает True;
# age = 22
# isMarried = False
# result = age > 21 or isMarried
# print(result)  # True, так как выражение age > 21 равно True


# IN - возвращает True, если в некотором наборе значений есть определенное значение
# message = "hello world!"
# print("hello" in message)  # True - т.к. подстрока hello есть в строке "hello world!"
# print("gold" in message)  # False - т.к. подстроки "gold" нет в строке "hello world!"


# my_list = [1, 2, 3, 4]
# print(3 in my_list)  # True


# NOT — логическое «НЕ» для одного условия. Возвращает False для истинного условия, и наоборот.
# message = "hello world!"
# print("gold" not in message)  # True - т.к. подстроки "gold" нет в строке "hello world!"
