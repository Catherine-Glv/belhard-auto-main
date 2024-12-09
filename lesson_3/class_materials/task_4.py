my_dict = {'cat': 'кот', 'dog': 'собака', 'bird': 'птица'}

# for key in my_dict.keys():
#     print(key)
#
# for key in my_dict:
#     print(key)
#
# for value in my_dict.values():
#     print(value)
    
for key, value in my_dict.items():
    print(f'ключ - {key}, его значение - {value}')
