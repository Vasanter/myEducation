"""Кортеж (tuple)"""
# Это неизменяемый (immutable) упорядоченный тип данных, предназначенный для хранения последовательности элементов.
# После создания кортежа его содержимое нельзя изменить: нельзя добавить, удалить или заменить элементы.
# Кортежи поддерживают индексацию, срезы и могут содержать объекты любых типов, включая другие кортежи и списки


user_roles = ("admin", "editor", "viewer")
print(user_roles)  # Outputs: ("admin", "editor", "viewer")

# print(user_roles[1])  # "editor"

# print(user_roles[1]) = "author"  # TypeError: 'tuple' -- НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ!

# print(len(user_roles))  # 3 - кол-во объектов в кортеже

# for role in user_roles:
#     print(role)  #  admin \n editor \n viewer print("admin" in user_roles)  # True
# print("writer" in user_roles)  # False


# not_tuple = ("apple")
# print(type(not_tuple))  # <class 'str'>
#
# my_tuple = ("admin",)  # !!! запятая
# print(type(my_tuple))  # <class 'tuple'>


# user_roles = ("admin", "editor", "viewer")
# role_1, role_2, role_3 = user_roles
# print(role_1)  # "admin"
# print(role_2)  # "editor"
# print(role_3)  # "viewer"


# user_roles = ["admin", "editor", "viewer"]  # with lists it works too
# role_1, role_2, role_3 = user_roles
# print(role_1)  # "admin"
# print(role_2)  # "editor"
# print(role_3)  # "viewer"


# role_1, role_2, _ = user_roles
# print(role_1)  # "admin"
# print(role_2)  # "editor"
