# ============================================
# 1. Инкапсуляция
# ============================================

"""
Инкапсуляция — это принцип объединения данных и методов работы
с ними внутри класса, а также скрытие внутренней реализации
от внешнего мира. Доступ осуществляется только через публичные методы.

В Python нет строгих модификаторов доступа, но есть соглашения:
- public:    name        — публичный атрибут
- protected: _name       — для потомков (для внутреннего использования)
- private:   __name      — name mangling (Python искажает название)
"""


class BankAccount:
    """Банковский счет с инкапсуляцией"""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner  # публичный
        self._balance = balance  # защищенный
        self.__pin = "1234"  # приватный (name mangling)

    # --- Публичные методы для работы с балансом ---
    def deposit(self, amount: float) -> None:
        """Пополнение счета"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        print(f"✅ Пополнено на {amount}. Баланс: {self._balance}")

    def withdraw(self, amount: float) -> None:
        """Снятие средств"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        print(f"✅ Снято {amount}. Баланс: {self._balance}")

    def get_balance(self) -> float:
        """Получение баланса (read-only)"""
        return self._balance

    # --- Приватный метод ---
    def __verify_pin(self, pin: str) -> bool:
        """Проверка PIN (приватный)"""
        return pin == self.__pin


# Использование:
account = BankAccount("Alice", 1000)

account.deposit(500)  # ✅ Пополнено на 500. Баланс: 1500
account.withdraw(200)  # ✅ Снято 200. Баланс: 1300
print(account.get_balance())  # 1300

# Прямой доступ к _balance — не рекомендуется
print(account._balance)  # 1300 (работает, но нарушает соглашение)

# Прямой доступ к __pin — не работает:
# print(account.__pin)        # AttributeError: 'BankAccount' object has no attribute '__pin'

# Но через name mangling все равно можно:
print(account._BankAccount__pin)  # 1234 ⚠️ (так делать не рекомендуется)


# --- Инкапсуляция через @property ---
class Temperature:
    """Управление температурой с валидацией"""

    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Получение температуры в °C"""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Установка температуры с валидацией"""
        if value < -273.15:
            raise ValueError("Температура ниже абсолютного нуля!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Только чтение — вычисляемое свойство"""
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius)  # 25
print(t.fahrenheit)  # 77.0

t.celsius = 30  # через setter
print(t.celsius)  # 30

# t.celsius = -300    # ValueError: Температура ниже абсолютного нуля!
