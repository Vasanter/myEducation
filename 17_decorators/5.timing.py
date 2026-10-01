"""
ДЕКОРАТОР @GET_TIME — ИЗМЕРЕНИЕ ВРЕМЕНИ ВЫПОЛНЕНИЯ
=====================================================
Декоратор для измерения времени выполнения функции.

?? Важно: одноразовое измерение ненадёжно.
   Для точных бенчмарков используйте модуль timeit.
"""

import time
from time import perf_counter, sleep
from functools import wraps
from typing import Callable, Any


# ============================================
# 1. ДЕКОРАТОР
# ============================================

def get_time(func: Callable) -> Callable:
    """
    Измеряет время выполнения декорированной функции.

    Использует perf_counter() — наиболее точный таймер
    с наивысшим доступным разрешением.

    Args:
        func: Функция для измерения.

    Returns:
        Обёртка, выводящая время выполнения.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # perf_counter() точнее time.time()
        start_time: float = perf_counter()

        try:
            result: Any = func(*args, **kwargs)
            return result
        finally:
            end_time: float = perf_counter()
            elapsed = end_time - start_time
            print(
                f'??  "{func.__name__}()" took '
                f'{elapsed:.3f} seconds to execute'
            )

    return wrapper


# ============================================
# 2. ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# ============================================

@get_time
def connect() -> None:
    """Имитация подключения"""
    print('Connecting...')
    sleep(2)
    print('Connected!')


@get_time
def fifty_million_loops() -> None:
    """Имитация тяжёлых вычислений"""
    fifty_million: int = int(5e7)

    print('Looping...')
    for _ in range(fifty_million):
        pass

    print('Done looping!')


def main() -> None:
    fifty_million_loops()
    connect()


if __name__ == '__main__':
    main()