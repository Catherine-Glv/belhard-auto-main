"""
try:
    код, где ожидаем получить ошибку
except <класс ошибки>
    код, выполнил действие, если ошибка
else:
    код, если нет ошибки
finally:
    код, который будет выполняться ВСЕГДА
"""

try:
    x = 2
    y = 2
    print(x / y)
except ZeroDivisionError:
    print('Ошибка деления на 0')
else:
    print('Ошибок нет')
finally:
    print('Конец программы')

try:
    data = {'a1': 'b1'}
    value = int(input('Число: '))
    print(data['a2'])
except KeyError:
    print('Ключ не найден')
except ValueError:
    print('Введено не число')

try:
    x = int(input('Введите число: '))
except ValueError:
    print('Значение не найдено')