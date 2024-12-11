# args - неограниченное число аргументов, kwargs - ключей

def print_tuple_of_numbers(*args):
    return args

print(print_tuple_of_numbers(1, 2, 3 ,4 ,5 ,6 ,7 ,8, 9)) # кортеж


def print_dict_elements(**kwargs):
    return kwargs

print(print_dict_elements(name='katya', color='green')) # словарь


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, 4, 5, name='katya')
