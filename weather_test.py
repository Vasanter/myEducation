import requests

lat = input('Введите широту: ')  # 55.628028 // 55.688358
long = input('Введите долготу: ')  # 37.595152 // 37.282246


def intro(func):
    def wrapper(*args, **kwargs):
        print('Генерирую  данные...')
        return func(*args, **kwargs)

    return wrapper


class Weather:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.long = longitude
        self.data = self.get_weather()
        self.temperature = self.data['current_weather']['temperature']

    @intro
    def get_weather(self):
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.long}&current_weather=true")
        return response.json()

    @intro
    def warm_or_cold(self):
        if self.temperature > 25:
            return 'жарко'
        elif 18 < self.temperature < 25:
            return 'комфортно'
        else:
            return 'холодно'


weather = Weather(lat, long)
print('Текущая температура:', weather.temperature)
print('Сегодня -', weather.warm_or_cold())

# print('Список ключей: ')
for key in weather.data:
    print(key)
