"""
ФИКСТУРЫ (FIXTURES) В PYTEST
===============================
Фикстура — это функция, которая подготавливает и предоставляет
тестам всё необходимое: данные, соединения, временные файлы, окружение.

Основные возможности:
- Подготовка (setup) и очистка (teardown)
- Переиспользование между тестами
- Управление областью видимости (scope)
- Параметризация
- Автоприменение (autouse)
- Зависимости между фикстурами

?? Для работы нужен pytest:
   pip install pytest
"""

import pytest


# ============================================
# 1. ПРОСТАЯ ФИКСТУРА
# ============================================

"""
Фикстура объявляется декоратором @pytest.fixture.
Тест запрашивает её по имени — указывает в параметрах.
"""


@pytest.fixture
def sample_data():
    """Возвращает тестовые данные"""
    return {"name": "Alice", "age": 30}


def test_user_name(sample_data):
    """Тест использует фикстуру sample_data"""
    assert sample_data["name"] == "Alice"


def test_user_age(sample_data):
    """Другая фикстура — те же данные"""
    assert sample_data["age"] == 30


# ============================================
# 2. SETUP И TEARDOWN (YIELD)
# ============================================

"""
Код ДО yield — setup (подготовка).
Код ПОСЛЕ yield — teardown (очистка).
Teardown выполняется даже при падении теста.
"""


@pytest.fixture
def database_connection():
    """Фикстура с подготовкой и очисткой"""
    # --- SETUP ---
    print("\n? Подключение к базе данных...")
    connection = {"status": "connected", "data": []}

    yield connection  # ? возвращаем объект в тест

    # --- TEARDOWN ---
    print("? Закрытие соединения...")
    connection["status"] = "closed"


def test_insert(database_connection):
    """Тест использует соединение"""
    database_connection["data"].append("item")
    assert database_connection["status"] == "connected"


# ============================================
# 3. ОБЛАСТИ ВИДИМОСТИ (SCOPE)
# ============================================

"""
?????????????????????????????????????????????????????????????????????????
?  Scope     ?  Когда создаётся                   ?  Типичное применение?
?????????????????????????????????????????????????????????????????????????
?  function  ?  Для каждого теста (по умолчанию)  ?  Изменяемые данные  ?
?  class     ?  Один раз на класс                 ?  Группа тестов      ?
?  module    ?  Один раз на модуль (.py)          ?  Дорогое подключение?
?  package   ?  Один раз на пакет                 ?  Настройка пакета   ?
?  session   ?  Один раз за весь запуск pytest    ?  Браузер, БД        ?
?????????????????????????????????????????????????????????????????????????
"""


@pytest.fixture(scope="module")
def api_client():
    """Создаётся один раз для всего модуля"""
    print("\n? Создание API-клиента (один раз на модуль)")
    client = {"base_url": "https://api.example.com"}
    yield client
    print("? Закрытие API-клиента")


@pytest.fixture(scope="session")
def browser():
    """Создаётся один раз за весь запуск pytest"""
    print("\n? Запуск браузера (один раз на сессию)")
    browser_instance = {"name": "chrome", "running": True}
    yield browser_instance
    print("? Закрытие браузера")


# ============================================
# 4. CONFTEST.PY — ОБЩИЕ ФИКСТУРЫ
# ============================================

"""
Если фикстура нужна в нескольких файлах — поместите её
в conftest.py. Pytest найдёт её автоматически.

Структура проекта:
    project/
    ??? conftest.py          ? общие фикстуры
    ??? test_users.py
    ??? tests/
        ??? conftest.py      ? фикстуры для tests/
        ??? test_api.py

Пример conftest.py:
"""

# conftest.py
import pytest


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL — доступен во всех тестах"""
    return "https://myapp.com"


@pytest.fixture
def auth_headers():
    """Заголовки авторизации"""
    return {"Authorization": "Bearer token123"}


# ============================================
# 5. ПАРАМЕТРИЗАЦИЯ ФИКСТУР
# ============================================

"""
params= позволяет запустить один тест несколько раз
с разными значениями. Доступ через request.param.
"""


@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser_name(request):
    """Параметризованная фикстура — 3 запуска теста"""
    return request.param


def test_browser_supported(browser_name):
    """Тест выполнится 3 раза: для chrome, firefox, safari"""
    assert browser_name in ["chrome", "firefox", "safari"]


# С идентификаторами для наглядности:
@pytest.fixture(params=[
    pytest.param("chrome", id="Chrome"),
    pytest.param("firefox", id="Firefox"),
    pytest.param("safari", id="Safari"),
])
def browser_with_id(request):
    return request.param


def test_browser_ids(browser_with_id):
    print(f"Тестируем: {browser_with_id}")


# ============================================
# 6. AUTouse — АВТОПРИМЕНЕНИЕ
# ============================================

"""
autouse=True — фикстура применяется ко ВСЕМ тестам
автоматически, без явного указания.
"""


@pytest.fixture(autouse=True)
def setup_environment():
    """Выполняется перед каждым тестом в модуле"""
    print("\n??  [Setup] Подготовка окружения...")
    yield
    print("? [Teardown] Очистка окружения...")


def test_one():
    """Фикстура применится автоматически"""
    assert True


def test_two():
    """И здесь тоже"""
    assert True


# ============================================
# 7. ЗАВИСИМОСТИ МЕЖДУ ФИКСТУРАМИ
# ============================================

"""
Одна фикстура может запрашивать другую.
Pytest гарантирует правильный порядок выполнения.
"""


@pytest.fixture
def db():
    """Настройка БД"""
    print("\n? Настройка базы данных")
    return {"connection": "active", "users": []}


@pytest.fixture
def user(db):  # ? зависит от db
    """Создание пользователя (требует db)"""
    print("? Создание пользователя в БД")
    user_data = {"name": "test_user", "id": 1}
    db["users"].append(user_data)
    return user_data


def test_user_created(user, db):
    """Тест использует обе фикстуры"""
    assert user["name"] == "test_user"
    assert len(db["users"]) == 1


# ============================================
# 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================

# --- 1. Временные файлы ---
@pytest.fixture
def temp_file(tmp_path):
    """
    tmp_path — встроенная фикстура pytest.
    Создаёт уникальную временную директорию для теста.
    """
    file_path = tmp_path / "log_path.log"
    file_path.write_text("Hello, World!", encoding="utf-8")
    return file_path


def test_read_temp_file(temp_file):
    content = temp_file.read_text(encoding="utf-8")
    assert content == "Hello, World!"


# --- 2. Мок-объект (заглушка) ---
from unittest.mock import MagicMock


@pytest.fixture
def mock_api():
    """Мок API-клиента"""
    mock = MagicMock()
    mock.get_user.return_value = {"id": 1, "name": "Alice"}
    mock.get_user.side_effect = None
    return mock


def test_mock_api(mock_api):
    result = mock_api.get_user(1)
    assert result["name"] == "Alice"
    mock_api.get_user.assert_called_once_with(1)


# --- 3. Временная база данных ---
import sqlite3


@pytest.fixture
def temp_db(tmp_path):
    """Временная БД с таблицей"""
    db_file = tmp_path / "test.db"
    conn = sqlite3.connect(db_file)
    conn.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"
    )
    conn.commit()

    yield conn

    conn.close()


def test_db_insert(temp_db):
    temp_db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    temp_db.commit()

    result = temp_db.execute("SELECT name FROM users").fetchone()
    assert result[0] == "Alice"


# --- 4. Фикстура с логином ---
@pytest.fixture
def logged_in_user(auth_headers):
    """Имитация авторизованного пользователя"""
    return {
        "id": 1,
        "name": "Alice",
        "headers": auth_headers,
    }


def test_user_profile(logged_in_user):
    assert logged_in_user["name"] == "Alice"
    assert "Authorization" in logged_in_user["headers"]


# --- 5. Фикстура для API-запросов (requests + моки) ---
from unittest.mock import patch


@pytest.fixture
def mock_requests():
    """Мок для requests.get"""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"price": "50000"}
        mock_get.return_value = mock_response
        yield mock_get


def test_fetch_price(mock_requests):
    import requests
    response = requests.get("https://api.example.com/price")
    assert response.json()["price"] == "50000"
    mock_requests.assert_called_once()


# ============================================
# 9. ПОИСК ДОСТУПНЫХ ФИКСТУР
# ============================================

"""
Встроенные фикстуры pytest (не нужно создавать):

???????????????????????????????????????????????????????????????????
?  Фикстура            ?  Назначение                              ?
???????????????????????????????????????????????????????????????????
?  tmp_path            ?  Временная директория (pathlib.Path)     ?
?  tmp_path_factory    ?  Фабрика временных директорий            ?
?  capsys              ?  Захват stdout/stderr                    ?
?  capfd               ?  Захват файловых дескрипторов            ?
?  monkeypatch         ?  Мокирование атрибутов/окружения         ?
?  request             ?  Информация о текущем тесте              ?
?  caplog              ?  Захват логов                            ?
?  recwarn             ?  Захват предупреждений                   ?
???????????????????????????????????????????????????????????????????

Посмотреть все доступные фикстуры:
    pytest --fixtures test_file.py
"""


# --- Пример использования monkeypatch ---
import os


@pytest.fixture
def fake_env(monkeypatch):
    """Устанавливает переменную окружения на время теста"""
    monkeypatch.setenv("API_KEY", "test_key_123")
    return os.getenv("API_KEY")


def test_env_variable(fake_env):
    assert fake_env == "test_key_123"


# --- Пример использования capsys ---
def test_print_output(capsys):
    """Захват вывода print()"""
    print("Hello, pytest!")

    captured = capsys.readouterr()
    assert "Hello, pytest!" in captured.out


# ============================================
# 10. ПОЛНЫЙ ПРИМЕР: ТЕСТИРОВАНИЕ API
# ============================================

import requests
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str


@pytest.fixture(scope="session")
def api_session():
    """Сессия requests — одна на все тесты"""
    session = requests.Session()
    session.headers.update({"User-Agent": "Test/1.0"})
    yield session
    session.close()


@pytest.fixture
def api_url():
    """Базовый URL API"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def user_data():
    """Тестовые данные пользователя"""
    return {"name": "Alice", "email": "alice@example.com"}


@pytest.fixture
def created_user(api_session, api_url, user_data):
    """Создаёт пользователя и удаляет после теста"""
    response = api_session.post(f"{api_url}/users", json=user_data)
    user = response.json()

    yield user

    # Очистка: удалить созданного пользователя
    api_session.delete(f"{api_url}/users/{user.get('id', 1)}")


def test_create_user(created_user, user_data):
    """Тест создания пользователя"""
    assert created_user["name"] == user_data["name"]
    assert "id" in created_user


# ============================================
# 11. ШПАРГАЛКА
# ============================================

"""
????????????????????????????????????????????????????????????
?  FIXTURES В PYTEST — ШПАРГАЛКА                           ?
????????????????????????????????????????????????????????????
?  СОЗДАНИЕ:                                               ?
?  @pytest.fixture                                         ?
?  def my_fixture():                                       ?
?      return value                                        ?
????????????????????????????????????????????????????????????
?  С ОЧИСТКОЙ:                                             ?
?  @pytest.fixture                                         ?
?  def my_fixture():                                       ?
?      # setup                                             ?
?      yield value                                         ?
?      # teardown                                          ?
????????????????????????????????????????????????????????????
?  ИСПОЛЬЗОВАНИЕ В ТЕСТЕ:                                  ?
?  def test_something(my_fixture):                         ?
?      assert my_fixture == value                          ?
????????????????????????????????????????????????????????????
?  SCOPE:                                                  ?
?  @pytest.fixture(scope="function")  — по умолчанию       ?
?  @pytest.fixture(scope="class")                          ?
?  @pytest.fixture(scope="module")                         ?
?  @pytest.fixture(scope="session")                        ?
????????????????????????????????????????????????????????????
?  ПАРАМЕТРИЗАЦИЯ:                                         ?
?  @pytest.fixture(params=[1, 2, 3])                       ?
?  def f(request): return request.param                    ?
????????????????????????????????????????????????????????????
?  AUTOUSE:                                                ?
?  @pytest.fixture(autouse=True)                           ?
????????????????????????????????????????????????????????????
?  CONFTEST.PY:                                            ?
?  Общие фикстуры — доступны без импорта                   ?
????????????????????????????????????????????????????????????
?  ВСТРОЕННЫЕ:                                             ?
?  tmp_path, capsys, monkeypatch, request, caplog          ?
????????????????????????????????????????????????????????????
?  КОМАНДЫ:                                                ?
?  pytest --fixtures          — список фикстур             ?
?  pytest --setup-show        — порядок setup/teardown     ?
????????????????????????????????????????????????????????????
"""


# ============================================
# 12. ЧАСТЫЕ ОШИБКИ
# ============================================

# ? Ошибка 1: Забыли yield для teardown
@pytest.fixture
def bad_db():
    conn = sqlite3.connect(":memory:")
    return conn   # ? соединение не закроется!

# ? Решение:
@pytest.fixture
def good_db():
    conn = sqlite3.connect(":memory:")
    yield conn    # ? отдаём в тест
    conn.close()  # ? закрываем после


# ? Ошибка 2: Изменяемые данные на scope="session"
@pytest.fixture(scope="session")
def bad_list():
    return []   # ? список разделяется между всеми тестами!

def test_a(bad_list):
    bad_list.append(1)

def test_b(bad_list):
    assert bad_list == []   # ? упадёт, там [1]

# ? Решение: scope="function" для изменяемых данных
@pytest.fixture  # scope="function" по умолчанию
def good_list():
    return []


# ? Ошибка 3: Тест зависит от порядка других тестов
@pytest.fixture(scope="session")
def counter():
    return {"value": 0}

def test_increment(counter):
    counter["value"] += 1

def test_check(counter):
    assert counter["value"] == 0   # ? зависит от порядка!

# ? Решение: изолированные фикстуры


# ? Ошибка 4: Слишком широкая фикстура
@pytest.fixture
def everything():
    """Создаёт БД, браузер, API, файлы — всё сразу"""
    ...

# ? Решение: разделяйте на мелкие фикстуры


# ? Ошибка 5: Фикстура возвращает None
@pytest.fixture
def bad_fixture():
    print("Setup")   # ? нет return/yield!

def test_x(bad_fixture):
    assert bad_fixture is None   # ? всегда None

# ? Решение:
@pytest.fixture
def good_fixture():
    print("Setup")
    return "value"


# ? Ошибка 6: Импорт conftest.py
# from conftest import base_url   # ? не нужно!

# ? Решение: просто используйте как параметр
def test_something(base_url):   # ? pytest найдёт сам
    assert base_url


# ============================================
# 13. ЗАПУСК ТЕСТОВ
# ============================================

"""
# Запустить все тесты:
pytest

# Конкретный файл:
pytest test_users.py

# Конкретный тест:
pytest test_users.py::test_user_name

# С выводом print():
pytest -s

# Подробный вывод:
pytest -v

# Показать порядок setup/teardown:
pytest --setup-show

# Список доступных фикстур:
pytest --fixtures
"""