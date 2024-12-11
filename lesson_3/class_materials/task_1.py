"""
Словарь

ключ:значение
"""

my_dict = {}
print(type(my_dict), my_dict)

my_dict_1 = dict()
print(type(my_dict_1), my_dict_1)

my_dict_2 = {'cat': 'кот', 'dog': 'собака', 'bird': 'птица'}
print(my_dict_2)

print(len(my_dict_2))

# x = [['a', 'b'],['c', 'd']]
# print(dict(x))

info = dict(
    cat='кошка',
    dog='собака',
    bird='птица'
)
print(info)

# получить значение словаря по ключу
print(info['dog'])

# добавить новую пару
info['animals'] = 'животные'
print(info)

# изменение значения по ключу
info['cat'] = 'котик'
print(info)

print('cat' in info) # поиск только по ключу

# метод: get - получение значения по ключу, если нет ключа - None (либо можно указать своё)
print(info.get('dog'))
print(info.get('dogg')) # None
print(info.get('dogg', 'Нет такого ключа'))

# update - обновление текущего словаря (добавление новых пар ключ: значение)
info.update({'snake': 'змея'})
print(info)

# keys - получение объекта ключей
print(info.keys(), type(info.keys()))

list_keys = list(info.keys())
print(list_keys)
list_keys.append('fish')
print(list_keys)

# values - получение объекта значений
print(info.values(), type(info.values()))

# items - получение объекта пар ключ, значение
print(info.items(), type(info.items()))
