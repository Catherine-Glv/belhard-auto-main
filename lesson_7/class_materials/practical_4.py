"""
В списке, содержащем положительные и отрицательные целые числа, вычислите сумму чётных положительных элементов.
"""

def summ(lst):

    assert isinstance(lst, list), f'Проверка не пройдена - ожидается список, получено {type(lst)}'
    assert all(isinstance(x, int) for x in lst), 'Проверка не пройдена - все элементы списка должны быть целыми числами'

    total = sum(x for x in lst if x > 0 and x % 2 == 0)
    return total

def print_result(lst):

    result = summ(lst)
    print(f'Сумма чисел: {result}')

print_result([])
print_result([2, 4, 6])
