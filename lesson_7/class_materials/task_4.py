# soft-assert множественная проверка, ошибки выдает в конце кода
import requests

api_token = 'de081f2ad84af3ccd0e1714937f56bad'
url = 'https://api.openweathermap.org/data/2.5/weather'
city = 'Minsk'

params = {'q': city, 'appid': api_token}
response = requests.get(url=url, params=params)
print(response.status_code)
print(response.headers)

info = response.json()
print(info)

# temp_min, temp_max, speed, country, name
assert 'temp_min' in info['main'], f'Ключ "temp_min" не найден, Полученные данные: {info}'
assert isinstance(info['main']['temp_max'], (int, float)), (f'"temp_max" должен быть числом, Полученное значение: '
                                                            f'{info['main']['temp_max']}')
assert info['wind']['speed'] is not None, (f'"speed" не может быть пустым, Полученное значение: '
                                           f'{info['wind']['speed']}')

print(response.json()['main']['temp_min'])
print(response.json()['main']['temp_max'])
print(response.json()['wind']['speed'])
print(response.json()['sys']['country'])
print(response.json()['name'])
