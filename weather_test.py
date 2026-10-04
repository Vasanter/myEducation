import time

import requests

lat = input('Введите широту: ')  # 55.628028 // 55.688358
long = input('Введите долготу: ')  # 37.595152 // 37.282246


def intro(func):
    """Объявление функции-декоратора с именем intro.
    Она принимает другую функцию (func) в качестве аргумента, чтобы расширить её поведение"""

    def wrapper(*args, **kwargs):
        """Объявление внутренней функции wrapper (обёртки).
        Звёздочки позволяют ей принимать любые позиционные и именованные аргументы, которые были у исходной функции"""
        print('Генерирую  данные...')
        time.sleep(3)  # задержка выполнения программы ровно на 3 секунды (имитация процесса загрузки)
        return func(*args, **kwargs)  # вызывает ориг-ую функцию func с перед-ми аргументами и возвращает её результат

    return wrapper  # возвращает саму функцию-обёртку, завершая работу декоратора


class Weather:
    """Объявление класса Weather, который будет отвечать за логику работы с погодой"""

    def __init__(self, latitude, longitude):
        """Конструктор класса (магический метод). Вызывается авто-ки при создании нового объекта (экземпляра) класса"""
        self.lat = latitude  # сохраняет переданную широту внутри объекта в атрибут self.lat
        self.long = longitude  # сохраняет переданную долготу внутри объекта в атрибут self.long
        self.data = self.get_weather()  # вызывает метод get_weather прямо при создании объекта и сохраняет весь
        # полученный JSON-ответ (в виде словаря Python) в атрибут self.data
        self.temperature = self.data['current_weather']['temperature']  # извлекает из словаря self.data значение
        # текущей температуры (по ключам 'current_weather' -> 'temperature') и сохраняет в атрибут self.temperature

    @intro  # Применение созданного ранее декоратора к методу get_weather.
    # Теперь при каждом его вызове сначала будет писаться текст и срабатывать пауза в 3 секунды.
    def get_weather(self) -> dict:
        """Отправляет запрос к API и возвращает JSON-ответ."""
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.long,
            "current_weather": "true"
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # Вызовет ошибку при статус-коде 4xx, 5xx
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return {}

    def warm_or_cold(self):  # метод, который анализирует сохраненную температуру
        if self.temperature > 25:
            return 'жарко'
        elif 18 <= self.temperature <= 25:
            return 'комфортно'
        else:
            return 'холодно'


weather = Weather(lat, long)  # Создает объект weather класса Weather, передавая туда координаты со входа.
# В этот момент срабатывает первая задержка на 3 секунды (из-за авто-вызова get_weather в конструкторе).
print('Текущая температура:', weather.temperature)  # Выводит на экран значение температуры, которое уже было
# сохранено в объекте.
print('Сегодня -', weather.warm_or_cold())  # Вызывает метод warm_or_cold().
# Из-за декоратора срабатывает вторая задержка на 3 секунды, после чего выводится вердикт о погоде.

# print('Список ключей: ')
# for key in weather.data:
#     print(key)
