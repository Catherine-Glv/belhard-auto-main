import requests
from transliterate import translit

def test_title_response_shazam_search():
    url = "https://shazam.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": "77eca07f5cmsh7fb074980e7c507p1b9034jsn8fc24c744b6e",
        "x-rapidapi-host": "shazam.p.rapidapi.com"
    }

    params = {'term': 'Зеленоглазое такси', 'locale': 'ru'}
    response = requests.get(url=url, headers=headers, params=params)
    json_data = response.json()
    for index_track in [0, 2, 3, 4]:
        title_from_resp = json_data['tracks']['hits'][0][index_track]['title'].lower()
    # title_from_resp = 'hello'
        expected_title = params.get('term').lower()
        assert expected_title in title_from_resp, f'Ожидали {expected_title}, но вернулось {title_from_resp}'

    # title_from_resp_second = json_data['tracks']['hits'][2]['track']['title'].lower()
    # expected_title = params.get('term').lower()
    # assert expected_title in title_from_resp_second, f'Ожидали {expected_title}, но вернулось {title_from_resp}'
    #
    # title_from_resp_third = json_data['tracks']['hits'][3]['track']['title'].lower()
    # expected_title = params.get('term').lower()
    # assert expected_title in title_from_resp_third, f'Ожидали {expected_title}, но вернулось {title_from_resp}'
    #
    # title_from_resp_fourth = json_data['tracks']['hits'][4]['track']['title'].lower()
    # expected_title = params.get('term').lower()
    # assert expected_title in title_from_resp_fourth, f'Ожидали {expected_title}, но вернулось {title_from_resp}'


def test_title_response_shazam_search_second_case():
    url = "https://shazam.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": "77eca07f5cmsh7fb074980e7c507p1b9034jsn8fc24c744b6e",
        "x-rapidapi-host": "shazam.p.rapidapi.com"
    }

    params = {'term': 'Зеленоглазое такси', 'locale': 'ru'}
    response = requests.get(url=url, headers=headers, params=params)
    json_data = response.json()
    title_from_resp = json_data['tracks']['hits'][0]['track']['title'].lower()
    text = 'Zelenoglazoe Taxi'
    ru_text = translit(text, 'ru')
    expected_title = params.get('term').lower()
    assert expected_title in title_from_resp, f'Ожидали {expected_title}, но вернулось {title_from_resp}'