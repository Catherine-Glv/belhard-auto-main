"""
Создайте словарь person, в котором будут присутствовать ключи name, age, city.
Выведите значение возраста из словаря person.
"""

person = dict(
    name='Katya',
    age=31,
    city='Minsk'
)
print(person.get('age'))

"""
№2
"""
marks = dict(
    BMW=['m3', 'x5', 'x6'],
    Tesla=['S', 'X', 'G']
)
print(f'BMW models: {marks.get('BMW')[::2]}. Tesla models: {marks.get('Tesla')[::2]}')

"""
#3
"""

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(d1['b'] == d2['b'])

"""
#4
"""

numbers = dict(
    one=1,
    two=2,
    three=3
)
numbers_product = 1
for num in numbers.values():
    numbers_product += num
print(numbers_product)

"""
#5
"""

keys = [1, 2, 3, 4]
values = ['a', 'b', 'c', 'd']

result_dict = {}

for i in range(len(keys)):
    result_dict[keys[i]] = values[i]
print(result_dict)

result_dict = dict(zip(keys, values))
print(result_dict)

"""
№6
"""

string = 'pythonist'
dict_1 = {}
for char in string:
    dict_1[char] = string.count(char)
print(dict_1)