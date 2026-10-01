"""
ATEXIT + SQLITE — ГАРАНТИРОВАННОЕ ЗАКРЫТИЕ БАЗЫ ДАННЫХ
==========================================================
Пример использования atexit для гарантированного сохранения
и закрытия соединения с базой данных при завершении программы.
"""

import atexit
import sqlite3
import logging

# Настройка логирования:
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================
# 1. ПОДКЛЮЧЕНИЕ К БД
# ============================================

# Соединение создаётся на уровне модуля:
cxn = sqlite3.connect("db.sqlite3")
logger.info("Database connected!")


# ============================================
# 2. ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ
# ============================================

def init_db() -> None:
    """Создаёт таблицу memes, если она не существует"""
    cxn.execute(
        "CREATE TABLE IF NOT EXISTS memes "
        "(id INTEGER PRIMARY KEY, meme TEXT)"
    )
    cxn.commit()
    logger.info("Database initialised!")


# ============================================
# 3. ОБРАБОТЧИК ЗАВЕРШЕНИЯ
# ============================================

@atexit.register
def exit_handler() -> None:
    """
    Гарантированно:
    1. Сохраняет изменения (commit)
    2. Закрывает соединение (close)

    Вызывается при нормальном завершении программы,
    даже если было необработанное исключение.
    """
    try:
        cxn.commit()
        logger.info("Changes committed!")
    except sqlite3.Error as e:
        logger.error(f"Commit failed: {e}")
    finally:
        cxn.close()
        logger.info("Database closed!")


# ============================================
# 4. ОСНОВНАЯ ПРОГРАММА
# ============================================

if __name__ == "__main__":
    init_db()

    # ?? Исключение — программа упадёт, но exit_handler сработает!
    1 / 0

    # Эта строка НЕ выполнится:
    print("This will never print")