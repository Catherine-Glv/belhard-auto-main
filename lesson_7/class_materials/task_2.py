import requests
"""
Статус коды

1хх - служебные (информационные)
2хх - успех, 200 - ОК
3хх - переадресация
4хх - ошибка, по вине пользователя 404 - page not found
5хх - ошибка, по вине сервера

"""

response = requests.get(url='https://www.google.by/')
print(response)
print(response.status_code)
print(response.headers) # заголовки ответа

with open(file='google_page.html', mode='w') as file:
    file.write(response.text)
