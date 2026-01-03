print("Добро пожаловать в список покупок!\n"
      "Введите команду для действия:\n"
      "+ для того чтобы добавить продукт!\n"
      "- для того чтобы удалить продукт\n"
      "* для просмотра списка покупок\n"
      "/ для завершения работы программы")

shopping_list = []

while True:
    command = input("Введите команду: ")
    if command == "+":
        item = input("Введите название продукта: ")
        if item not in shopping_list:
            shopping_list.append(item)
            print(f"{item.title()} добавлен в список покупок!")
        else:
            if item in shopping_list:
                print(f"{item.title()} уже есть в списке покупок!")

    elif command == "-":
        item = input("Введите звание продукта, который хотите удалить: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item.title()} удален из списка!")
        else:
            print("Такого продукта нет в списке!")

    elif command == "*":
        if len(shopping_list) > 0:
            print("Список покупок: ")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i} - {item.title()}")
        else:
            print("Список покупок пуст!")

    elif command == "/":
        print("Выходим из программы...")
        break
    else:
        print("Неизвестная программа!")
