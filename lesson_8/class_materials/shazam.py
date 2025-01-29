import requests

url = "https://shazam.p.rapidapi.com/search"

headers = {
	"x-rapidapi-key": "77eca07f5cmsh7fb074980e7c507p1b9034jsn8fc24c744b6e",
	"x-rapidapi-host": "shazam.p.rapidapi.com"
}

params = {'term': 'Зеленоглазое такси', 'locale': 'ru'}
response = requests.get(url=url, headers=headers, params=params)
print(response.json())
