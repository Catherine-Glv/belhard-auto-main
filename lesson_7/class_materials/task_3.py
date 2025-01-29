import requests

params = {'q': 'python'}
url = 'https://www.google.by/search'
response = requests.get(url=url, params='python')
print(response.status_code)

with open(file='google_python_page.html', mode='w') as file:
    file.write(response.text)
