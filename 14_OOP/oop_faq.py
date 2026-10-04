"""
ТРИ СТОЛПА ООП В PYTHON
=========================
1. Инкапсуляция — сокрытие внутренней реализации
2. Наследование — переиспользование кода через иерархию классов
3. Полиморфизм — один интерфейс, много реализаций
"""


# ============================================
# 1. ИНКАПСУЛЯЦИЯ
# ============================================

"""
Инкапсуляция — это сокрытие внутренних данных и деталей реализации
от внешнего мира. Доступ предоставляется только через публичные методы.

В Python нет строгих модификаторов доступа, но есть соглашения:
- public:    name        — доступен везде
- protected: _name       — «не трогать» (для внутреннего использования)
- private:   __name      — name mangling (Python «прячет» атрибут)
"""


class BankAccount:
    """Банковский счёт с инкапсуляцией"""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner              # публичный
        self._balance = balance         # защищённый
        self.__pin = "1234"             # приватный (name mangling)

    # --- Публичные методы для работы с балансом ---
    def deposit(self, amount: float) -> None:
        """Пополнить счёт"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        print(f"✅ Пополнено на {amount}. Баланс: {self._balance}")

    def withdraw(self, amount: float) -> None:
        """Снять деньги"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        print(f"✅ Снято {amount}. Баланс: {self._balance}")

    def get_balance(self) -> float:
        """Получить баланс (read-only)"""
        return self._balance

    # --- Приватный метод ---
    def __verify_pin(self, pin: str) -> bool:
        """Проверка PIN (приватный)"""
        return pin == self.__pin


# Использование:
account = BankAccount("Alice", 1000)

account.deposit(500)          # ✅ Пополнено на 500. Баланс: 1500
account.withdraw(200)         # ✅ Снято 200. Баланс: 1300
print(account.get_balance())  # 1300

# Прямой доступ к _balance — «не рекомендуется»
print(account._balance)       # 1300 (работает, но нарушает соглашение)

# Прямой доступ к __pin — НЕ работает:
# print(account.__pin)        # AttributeError: 'BankAccount' object has no attribute '__pin'

# Но через name mangling всё равно можно:
print(account._BankAccount__pin)  # 1234 ⚠️ (для знания, не для использования)


# --- Инкапсуляция через @property ---
class Temperature:
    """Управление температурой с валидацией"""

    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Получить температуру в °C"""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Установить температуру с валидацией"""
        if value < -273.15:
            raise ValueError("Температура ниже абсолютного нуля!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Только чтение — вычисляемое свойство"""
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

t.celsius = 30        # через setter
print(t.celsius)      # 30

# t.celsius = -300    # ValueError: Температура ниже абсолютного нуля!


# ============================================
# 2. НАСЛЕДОВАНИЕ
# ============================================

"""
Наследование — создание нового класса на основе существующего.
Дочерний класс получает все атрибуты и методы родителя,
может их дополнять или переопределять.
"""


# --- Базовый класс (родитель) ---
class Animal:
    """Базовый класс для всех животных"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self) -> None:
        print(f"{self.name} ест")

    def sleep(self) -> None:
        print(f"{self.name} спит")

    def make_sound(self) -> str:
        return "..."

    def info(self) -> str:
        return f"{self.name} ({self.age} лет)"


# --- Дочерний класс (наследник) ---
class Dog(Animal):
    """Собака — наследует Animal"""

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)   # вызов конструктора родителя
        self.breed = breed            # новое поле

    # Переопределение метода (override):
    def make_sound(self) -> str:
        return "Гав-гав!"

    # Новый метод:
    def fetch(self) -> None:
        print(f"{self.name} приносит мяч")

    # Расширение метода родителя:
    def info(self) -> str:
        base_info = super().info()    # вызов родительского метода
        return f"{base_info}, порода: {self.breed}"


class Cat(Animal):
    """Кошка — другой наследник"""

    def make_sound(self) -> str:
        return "Мяу!"

    def scratch(self) -> None:
        print(f"{self.name} точит когти")


# Использование:
dog = Dog("Rex", 3, "Labrador")
cat = Cat("Murka", 2)

dog.eat()             # Rex ест (унаследовано)
dog.make_sound()      # → "Гав-гав!" (переопределено)
dog.fetch()           # Rex приносит мяч (новый метод)
print(dog.info())     # Rex (3 лет), порода: Labrador

cat.eat()             # Murka ест
cat.make_sound()      # → "Мяу!"
cat.scratch()         # Murka точит когти


# --- Множественное наследование ---
class Flyable:
    """Миксин для летающих"""

    def fly(self) -> None:
        print(f"{self.name} летит")


class Swimmable:
    """Миксин для плавающих"""

    def swim(self) -> None:
        print(f"{self.name} плывёт")


class Duck(Animal, Flyable, Swimmable):
    """Утка умеет и летать, и плавать"""

    def make_sound(self) -> str:
        return "Кря-кря!"


duck = Duck("Donald", 1)
duck.eat()          # Donald ест
duck.fly()          # Donald летит
duck.swim()         # Donald плывёт
print(duck.make_sound())  # Кря-кря!


# --- Проверка наследования ---
print(isinstance(dog, Dog))       # True
print(isinstance(dog, Animal))    # True (Dog наследует Animal)
print(issubclass(Dog, Animal))    # True
print(issubclass(Cat, Dog))       # False


# ============================================
# 3. ПОЛИМОРФИЗМ
# ============================================

"""
Полиморфизм — один интерфейс, много реализаций.
Один и тот же вызов метода даёт разный результат
в зависимости от типа объекта.
"""


# --- Полиморфизм через наследование ---
class Shape:
    """Базовый класс фигуры"""

    def area(self) -> float:
        raise NotImplementedError("Подкласс должен реализовать area()")

    def perimeter(self) -> float:
        raise NotImplementedError("Подкласс должен реализовать perimeter()")

    def describe(self) -> str:
        return f"{self.__class__.__name__}: S={self.area():.2f}, P={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        # Формула Герона
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self) -> float:
        return self.a + self.b + self.c


# Полиморфный вызов — один код, разные типы:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
]

for shape in shapes:
    print(shape.describe())
# Circle: S=78.54, P=31.42
# Rectangle: S=24.00, P=20.00
# Triangle: S=6.00, P=12.00


# --- Полиморфизм через утиную типизацию (duck typing) ---
"""
"Если это выглядит как утка, плавает как утка и крякает как утка —
то это утка."

Python не проверяет тип — важно лишь, чтобы объект имел нужный метод.
"""


class File:
    def read(self) -> str:
        return "данные из файла"


class Database:
    def read(self) -> str:
        return "данные из базы"


class API:
    def read(self) -> str:
        return "данные из API"


def load_data(source) -> str:
    """Не важно, что за объект — главное, есть метод read()"""
    return source.read()


# Все три объекта работают одинаково:
print(load_data(File()))      # данные из файла
print(load_data(Database()))  # данные из базы
print(load_data(API()))       # данные из API


# --- Полиморфизм через магические методы ---
class Vector:
    """Вектор с перегрузкой операторов"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """Оператор +"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Оператор -"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        """Оператор *"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        """Оператор =="""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)      # Vector(4, 6)
print(v2 - v1)      # Vector(2, 2)
print(v1 * 3)       # Vector(3, 6)
print(v1 == Vector(1, 2))  # True


# --- Полиморфизм через абстрактные классы ---
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Абстрактный класс — нельзя создать экземпляр"""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Каждый подкласс ОБЯЗАН реализовать"""
        pass

    @abstractmethod
    def refund(self, amount: float) -> None:
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"💳 Оплата картой: {amount} руб.")

    def refund(self, amount: float) -> None:
        print(f"💳 Возврат на карту: {amount} руб.")


class PayPal(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"🅿️ Оплата PayPal: {amount} руб.")

    def refund(self, amount: float) -> None:
        print(f"🅿️ Возврат PayPal: {amount} руб.")


class Crypto(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"₿ Оплата криптой: {amount} руб.")

    def refund(self, amount: float) -> None:
        print(f"₿ Возврат крипты: {amount} руб.")


def process_payment(method: PaymentMethod, amount: float) -> None:
    """Полиморфная функция — работает с любым способом оплаты"""
    method.pay(amount)


# Использование:
methods = [CreditCard(), PayPal(), Crypto()]
for method in methods:
    process_payment(method, 1000)
# 💳 Оплата картой: 1000 руб.
# 🅿️ Оплата PayPal: 1000 руб.
# ₿ Оплата криптой: 1000 руб.

# PaymentMethod()  # TypeError: Can't instantiate abstract class


# ============================================
# 4. ВСЁ ВМЕСТЕ: ПРАКТИЧЕСКИЙ ПРИМЕР
# ============================================

class Employee:
    """Базовый класс сотрудника (инкапсуляция + наследование)"""

    def __init__(self, name: str, base_salary: float):
        self.name = name
        self._base_salary = base_salary   # защищённый

    @property
    def salary(self) -> float:
        """Инкапсуляция: вычисляемое свойство"""
        return self._base_salary

    def work(self) -> str:
        """Полиморфизм: переопределяется в наследниках"""
        return f"{self.name} работает"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.salary})"


class Manager(Employee):
    """Менеджер — надбавка за руководство"""

    def __init__(self, name: str, base_salary: float, team_size: int):
        super().__init__(name, base_salary)
        self.team_size = team_size

    @property
    def salary(self) -> float:
        """Переопределение свойства — бонус за команду"""
        bonus = self.team_size * 5000
        return self._base_salary + bonus

    def work(self) -> str:
        return f"{self.name} управляет командой из {self.team_size} человек"


class Developer(Employee):
    """Разработчик — надбавка за технологии"""

    def __init__(self, name: str, base_salary: float, tech_stack: list):
        super().__init__(name, base_salary)
        self.tech_stack = tech_stack

    @property
    def salary(self) -> float:
        bonus = len(self.tech_stack) * 10000
        return self._base_salary + bonus

    def work(self) -> str:
        tech = ", ".join(self.tech_stack)
        return f"{self.name} пишет код на {tech}"


class Intern(Employee):
    """Стажёр — фиксированная зарплата"""

    def work(self) -> str:
        return f"{self.name} учится и помогает команде"


# Полиморфная обработка:
team = [
    Manager("Alice", 100000, 5),
    Developer("Bob", 80000, ["Python", "Go"]),
    Intern("Charlie", 30000),
]

print("=== Команда ===")
for employee in team:
    print(employee)
    print(f"  Зарплата: {employee.salary} руб.")
    print(f"  {employee.work()}")
    print()

# === Команда ===
# Manager(Alice, 125000)
#   Зарплата: 125000 руб.
#   Alice управляет командой из 5 человек
#
# Developer(Bob, 100000)
#   Зарплата: 100000 руб.
#   Bob пишет код на Python, Go
#
# Intern(Charlie, 30000)
#   Зарплата: 30000 руб.
#   Charlie учится и помогает команде

# Подсчёт общей зарплаты (полиморфизм):
total = sum(emp.salary for emp in team)
print(f"Общий фонд оплаты: {total} руб.")  # 255000


# ============================================
# 5. ШПАРГАЛКА
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│  ТРИ СТОЛПА ООП — ШПАРГАЛКА                              │
├──────────────────────────────────────────────────────────┤
│  ИНКАПСУЛЯЦИЯ:                                           │
│  • public:    self.name                                  │
│  • protected: self._name                                 │
│  • private:   self.__name (name mangling)                │
│  • @property — контроль доступа                          │
├──────────────────────────────────────────────────────────┤
│  НАСЛЕДОВАНИЕ:                                           │
│  • class Child(Parent):                                  │
│  • super().__init__() — вызов родителя                   │
│  • Множественное: class D(A, B, C)                       │
│  • isinstance() — проверка типа                          │
│  • issubclass() — проверка класса                        │
├──────────────────────────────────────────────────────────┤
│  ПОЛИМОРФИЗМ:                                            │
│  • Переопределение методов (override)                    │
│  • Duck typing — важен метод, а не тип                   │
│  • Магические методы (__add__, __eq__)                   │
│  • Абстрактные классы (ABC)                              │
├──────────────────────────────────────────────────────────┤
│  ВМЕСТЕ:                                                 │
│  Инкапсуляция — КАК хранятся данные                      │
│  Наследование — КАК переиспользуется код                 │
│  Полиморфизм  — КАК один код работает с разными типами   │
└──────────────────────────────────────────────────────────┘
"""


# ============================================
# 6. ЧАСТЫЕ ОШИБКИ
# ============================================

# ❌ Ошибка 1: Забыли super().__init__()
class BadDog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed    # name и age не установлены!
        # super().__init__(name, age) — забыли

# ✅ Решение:
class GoodDog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # ✅
        self.breed = breed


# ❌ Ошибка 2: Изменяемые атрибуты класса
class BadTeam:
    members = []   # разделяется между ВСЕМИ экземплярами!

t1 = BadTeam()
t1.members.append("Alice")
t2 = BadTeam()
print(t2.members)  # ['Alice'] — неожиданно!

# ✅ Решение: создавать в __init__
class GoodTeam:
    def __init__(self):
        self.members = []   # ✅ у каждого свой


# ❌ Ошибка 3: Доступ к приватным атрибутам
class User:
    def __init__(self):
        self.__password = "secret"

u = User()
# print(u.__password)  # AttributeError

# ✅ Решение: публичный метод
class User:
    def __init__(self):
        self.__password = "secret"

    def check_password(self, pwd: str) -> bool:
        return pwd == self.__password


# ❌ Ошибка 4: Полиморфизм без общего интерфейса
def bad_process(items):
    for item in items:
        if isinstance(item, Circle):
            item.area()
        elif isinstance(item, Rectangle):   # плохо!
            item.area()

# ✅ Решение: общий базовый класс
def good_process(shapes: list[Shape]):
    for shape in shapes:
        shape.area()   # полиморфно


# ❌ Ошибка 5: Абстрактный класс без реализации
class BadShape(ABC):
    @abstractmethod
    def area(self): ...

class BadCircle(BadShape):
    pass   # TypeError при создании — area не реализован

# ✅ Решение:
class GoodCircle(BadShape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2