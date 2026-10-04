from pywinauto.application import Application

# 1. Запускаем Блокнот (для Windows 11 лучше использовать backend="uia")
app = Application(backend="uia").start("notepad.exe")

# 2. Подключаемся к главному окну (ищем по заголовку или классу)
# Название окна в Windows 11 может отличаться, например, "Блокнот"
main_window = app.window(title_re=".*Блокнот.*")

# 3. Находим поле для ввода и пишем текст
# type_keys вводит текст со скоростью печати человека
main_window.type_keys("Привет из PyWinAuto!", with_spaces=True)

# 4. Закрываем приложение
main_window.close()

# 5. Если выскочит окно "Сохранить изменения?", отказываемся
# (код ниже сработает, если появится диалоговое окно)
if app.window(title_re=".*Сохранить.*").exists():
    app.window(title_re=".*Сохранить.*").child_window(title="Не сохранять").click()
