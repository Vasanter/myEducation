f = open(r"C:\Automation\myEducation\files\my_file.txt", "w")  # 'w': Запись (создает, если нет; удаляет старое
# содержимое, если есть)

f.write("World\n")
f.write("END\n")
f.close()
