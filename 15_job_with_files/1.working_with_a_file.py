# Для работы с файлами в Python используются функция open() для открытия, методы .read()/.write() для операций и метод
# .close() для закрытия, при этом лучший способ — использовать with open(...) as f:, который автоматически управляет
# закрытием, а основные режимы: 'r' (чтение), 'w' (запись, перезаписывает), 'a' (добавление). Модули os и shutil
# позволяют удалять, переименовывать и перемещать файлы, а with с encoding='utf-8' важен для кириллицы.

# ОСНОВНЫЕ ШАГИ:
# Открытие файла: open('filename.txt', 'режим').
# Операции: Чтение (.read(), .readline(), .readlines()) или запись (.write()).
# Закрытие: .close().

# Режимы работы с файлами
# 'r': Чтение (по умолчанию).
# 'w': Запись (создает, если нет; удаляет старое содержимое, если есть).
# 'a': Добавление (append) в конец файла.
# 'x': Создание нового файла, ошибка, если существует.
# 'b': Бинарный режим (для изображений и т.д.).
# '+': Чтение и запись.


# 1. Сначала создаем файл записью (если его нет)
with open('persons.csv', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!\n")
    f.write("Это новая строка.")

# 2. Добавляем еще текст
with open('persons.csv', 'a', encoding='utf-8') as f:
    f.write("\nДобавлено позже.")

# 3. Теперь читаем (файл уже существует)
with open('persons.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Содержимое файла:")
    print(content)

# Дополнительные действия с файлами (модуль os):
# - проверка существования: os.path.exists('file.txt').
# - удаление: os.remove('file.txt').
# - переименование: os.rename('old_name.txt', 'new_name.txt').
# - перемещение (модуль shutil): shutil.move('src', 'dst').


# file = open(file='message.txt', mode='r')  # чтение файла
# print(file.read())  # считывает файл полностью
# print(file.readline())  # считывает первую строку


# file = open(file='message.txt', mode='w')  # перезапись данных в файле
# file.write('Hello World Man')
# file.close()
#
# file = open(file='message.txt', mode='a')  # добавление данных в конце файла
# file.write('\nAPPEND TEXT')
# file.close()


# ЗАДАНИЕ 1:
# Создайте текстовый файл с именем data.txt и наполните его несколькими строками текста.
# Напишите программу, которая открывает файл, читает его построчно и выводит каждую строку.

with open('data.txt', 'w') as file:
    line1 = file.write("Милан\n")
    line2 = file.write("Интер\n")
    line3 = file.write("Лацио")

with open('data.txt', 'r') as file:
    for line in enumerate(file):
        print(line.strip())


# ЗАДАНИЕ 2:
# Напишите скрипт, который запрашивает у пользователя его имя и возраст, а затем записывает эту информацию в файл
# userinfo.txt. Каждая запись должна быть отдельной строкой в файле.
while True:
    name = input("Enter your name: ")
    if name == 'stop':
        break
    age = input("Enter your age: ")
    user_info = f'{name}: {age}\n'
    with open('userinfo.txt', 'a') as file:
        file.write(user_info)


# ЗАДАНИЕ 3:
# Создайте original.txt и запишите в него любую информацию.
# Напишите программу, которая копирует все содержимое файла original.txt в copy.txt.
with open('original.txt', 'w') as file:
    file.write('Это содержимое исходного файла.\nЗдесь что-то написано.')

# Открываем оба файла сразу
with open('original.txt', 'r') as src, open('copy.txt', 'w') as dst:
    content = src.read()  # Читаем всё из первого
    dst.write(content)    # Записываем во второй

print("Файл успешно скопирован!")
