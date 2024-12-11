# Применение оператора global

x = 50

def func():
    global x
    print(f'х равен {x}')
    x = 2
    print(f'Замена глобального значения х на {x}')

func()
print(f'Значение х = {x}')