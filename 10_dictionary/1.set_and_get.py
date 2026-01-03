# Словарь(dictionary или dict) - это изменяемая структура данных, которая хранит элементы в виде пар "ключ-значение".
# Каждый ключ в словаре должен быть уникальным, и он используется для доступа к соответствующему значению. Словари часто
# называют ассоциативными массивами или отображениями.


# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
# person["job"] = "Engineer"  # добавится новое ключ-значение в конец списка =>
# print(person)  # {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}


# person = {"name": "John", "age": 30, "city": "New York"}  # or person = dict()
# print(person)  # {'name': 'John', 'age': 30, 'city': 'New York'}


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Output: 'John'
print(person.get("name"))  # Output: 'John'
print(person.get("country"))  # Output: None
print(person.get("country", "USA"))  # Output: USA
print(person.get("name", "Donny"))  # Output: John
