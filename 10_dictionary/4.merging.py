# назедхмемхе якнбюпеи

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
add_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person.update(add_person_info)
print(person)  # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}

dct_join = {**person, **add_person_info}
print(dct_join)  # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}

# *
person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
add_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person = person | add_person_info
print(person)  # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
