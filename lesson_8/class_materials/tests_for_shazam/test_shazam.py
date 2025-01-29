import requests

def test_title_response_shazam_search():
    url = "https://shazam.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": "77eca07f5cmsh7fb074980e7c507p1b9034jsn8fc24c744b6e",
        "x-rapidapi-host": "shazam.p.rapidapi.com"
    }

    params = {'term': 'Зеленоглазое такси', 'locale': 'ru'}
    response = requests.get(url=url, headers=headers, params=params)
    json_data = response.json()
    title_from_resp = json_data['tracks']['hits'][0]['track']['title'].lower()
    # title_from_resp = 'hello'
    expected_title = params.get('term').lower()
    assert expected_title in title_from_resp, f'Ожидали {expected_title}, но вернулось {title_from_resp}'
