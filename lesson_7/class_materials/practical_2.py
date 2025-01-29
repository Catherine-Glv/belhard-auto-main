"""
При заданном целом числе n посчитайте n + nn + nnn.
"""

def calculate(n):

    assert isinstance(n, int), f'Проверка не пройдена - n должно быть целым числом, получено {type(n)}'
    assert n != 0, 'Проверка не пройдена - n не должно быть равно 0'

    n_str = str(n)
    return n + int(n_str * 2) + int(n_str * 3)

print(calculate(5))
