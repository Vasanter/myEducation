"""
ДЕКОРАТОР @RETRY — ПОВТОРНЫЕ ПОПЫТКИ ПРИ ОШИБКАХ
==================================================
Декоратор с параметрами, который повторяет вызов функции
при возникновении исключения.

Применение:
- Сетевые запросы (нестабильное соединение)
- Работа с API (временные сбои)
- Файловые операции (блокировки)
- Базы данных (временная недоступность)

Синтаксис:
    @retry(retries=3, delay=1)
    def my_function(): ...
"""

import time
from functools import wraps
from typing import Callable, Any
from time import sleep


# ============================================
# 1. ДЕКОРАТОР С ПАРАМЕТРАМИ
# ============================================

def retry(retries: int = 3, delay: float = 1) -> Callable:
    """
    Декоратор для повторного вызова функции при ошибке.

    Args:
        retries: Максимальное количество попыток (>= 1).
        delay: Задержка между попытками в секундах (> 0).

    Returns:
        Декоратор, оборачивающий функцию.

    Raises:
        ValueError: Если retries < 1 или delay <= 0.

    Examples:
        >>> @retry(retries=3, delay=1)
        ... def unstable():
        ...     ...
    """

    # Валидация параметров:
    if retries < 1:
        raise ValueError(f'retries must be >= 1, got {retries}')
    if delay <= 0:
        raise ValueError(f'delay must be > 0, got {delay}')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None

            for attempt in range(1, retries + 1):
                try:
                    print(f'??  Попытка {attempt}/{retries}: {func.__name__}()')
                    return func(*args, **kwargs)

                except Exception as e:
                    last_exception = e

                    # Последняя попытка — пробрасываем исключение:
                    if attempt == retries:
                        print(f'? Ошибка: {repr(e)}')
                        print(f'? "{func.__name__}()" не удалась после {retries} попыток')
                        raise  # ? лучше пробросить, чем "break"

                    # Промежуточная попытка — ждём и повторяем:
                    print(f'??  Ошибка: {repr(e)} ? повтор через {delay} сек...')
                    sleep(delay)

            # Сюда не должны дойти, но на всякий случай:
            raise last_exception

        return wrapper

    return decorator


# ============================================
# 2. ПРИМЕР ИСПОЛЬЗОВАНИЯ
# ============================================

@retry(retries=3, delay=1)
def connect() -> None:
    """Имитация подключения к интернету"""
    time.sleep(1)
    raise Exception('Could not connect to internet...')


def main() -> None:
    try:
        connect()
    except Exception as e:
        print(f'\n? Программа завершилась с ошибкой: {e}')


if __name__ == '__main__':
    main()