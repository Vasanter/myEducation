"""
ПРОГРАММА "СПИСОК ПОКУПОК"
===========================
Демонстрация работы с циклом while, условиями и списками.
"""


# ============================================
# ПРИВЕТСТВИЕ И ИНСТРУКЦИЯ
# ============================================

def show_menu():
    """Показать меню программы"""
    print("\n" + "=" * 40)
    print("🛒 ДОБРО ПОЖАЛОВАТЬ В СПИСОК ПОКУПОК!")
    print("=" * 40)
    print("Введите команду для действия:")
    print("  +  — добавить продукт")
    print("  -  — удалить продукт")
    print("  *  — просмотреть список покупок")
    print("  /  — завершить работу программы")
    print("=" * 40)


# ============================================
# ФУНКЦИИ ДЛЯ КАЖДОЙ КОМАНДЫ
# ============================================

def add_item(shopping_list):
    """Добавить продукт в список"""
    item = input("Введите название продукта: ").strip().lower()

    if not item:
        print("❌ Название не может быть пустым!")
        return

    if item not in shopping_list:
        shopping_list.append(item)
        print(f"✅ {item.title()} добавлен в список покупок!")
    else:
        print(f"⚠️ {item.title()} уже есть в списке покупок!")


def remove_item(shopping_list):
    """Удалить продукт из списка"""
    item = input("Введите название продукта для удаления: ").strip().lower()

    if item in shopping_list:
        shopping_list.remove(item)
        print(f"🗑️ {item.title()} удалён из списка!")
    else:
        print(f"❌ Такого продукта нет в списке!")


def show_list(shopping_list):
    """Показать список покупок"""
    if shopping_list:
        print("\n📋 СПИСОК ПОКУПОК:")
        print("-" * 30)
        for i, item in enumerate(shopping_list, start=1):
            print(f"  {i}. {item.title()}")
        print("-" * 30)
        print(f"Всего позиций: {len(shopping_list)}")
    else:
        print("📭 Список покупок пуст!")


# ============================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================

def main():
    """Главная функция программы"""
    shopping_list = []
    show_menu()

    # Словарь команд (более гибко, чем if-elif)
    commands = {
        "+": add_item,
        "-": remove_item,
        "*": show_list,
    }

    while True:
        command = input("\nВведите команду: ").strip()

        if command == "/":
            print("👋 Выходим из программы... До свидания!")
            break

        elif command in commands:
            commands[command](shopping_list)

        else:
            print("❓ Неизвестная команда! Попробуйте ещё раз.")
            print("Доступные команды: +, -, *, /")


# ============================================
# ЗАПУСК ПРОГРАММЫ
# ============================================

if __name__ == "__main__":
    main()