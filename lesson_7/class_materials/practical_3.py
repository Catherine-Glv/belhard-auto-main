"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
"""

def key_dict(d):

    assert isinstance(d, dict), 'Проверка не пройдена - ожидается словарь'
    for key in list(d.keys()):
        new_key = key + str(len(key))
        assert len(new_key) == len(key) + len(str(len(key))), (f'Проверка не пройдена - длина ключа {new_key} '
                                                               f'не соответствует ожидаемой длине')
        d[new_key] = d.pop(key)
    return d

d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

result = key_dict(d)
print(result)
