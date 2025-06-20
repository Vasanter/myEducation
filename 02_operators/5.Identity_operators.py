"""ОПЕРАТОРЫ ТОЖДЕСТВЕННОСТИ"""
# Если операторы сравнения позволяют выяснить, равны ли значения двух переменных, то с помощью операторов
# тождественности можно проверить, ссылаются ли они на один и тот же объект.
# В отличие от операторов равенства операторы тождественности можно использовать для сравнения разнотипных объектов —
# это не вызовет ошибку typeError.

# Оператор is возвращает True, если оба операнда указывают на один и тот же объект в памяти, иначе возвращает False:
a = [1, 2, 3]
b = a  # 'b' теперь ссылается на тот же объект, что и 'a'
c = [1, 2, 3]

print(a is b)  # Вернёт: True
print(a is c)  # Вернёт: False, хотя 'a' и 'c' имеют одно и то же значение
# В этом примере выражение a is c возвращает False. Несмотря на то что переменные имеют одинаковое значение, они
# ссылаются на разные объекты в памяти.


# Оператор is not - возвращает True, если оба операнда указывают на разные объекты, иначе возвращает False:
a = [1, 2, 3]
b = a  # 'b' теперь ссылается на тот же объект, что и 'a'
c = [1, 2, 3]

print(a is not b)  # Вернёт: False
print(a is not c)  # Вернёт: True
