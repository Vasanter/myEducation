# Словарь(dictionary или dict) - это изменяемая структура данных, которая хранит элементы в виде пар "ключ-значение".
# Каждый ключ в словаре должен быть уникальным, и он используется для доступа к соответствующему значению. Словари часто
# называют ассоциативными массивами или отображениями.

# ПРИМЕР 1.
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
#
# print(person["name"])  # 'John'
# print(person.get("name"))  # 'John'
# print(person.get("country"))  # None - в случае если объекта нет в списке
# print(person.get("country", "USA"))  # USA - создаем значение по умолчанию
# print(person.get("name", "Donny"))  # John


# ПРИМЕР 2.
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(person)  # {'name': 'John', 'age': 30, 'city': 'New York'}
# person["job"] = "Engineer"  # добавится новое ключ-значение в конец списка =>
# print(person)  # {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}


# ПРИМЕР 3.
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
#
# for key, value in person.items():
#     print(key, value)  # выводим ключ и значение из словаря
