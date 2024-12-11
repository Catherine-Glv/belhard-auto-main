# Локальная область

x = 50

def func(x):
    print(f'x равен {x}')
    x = 2
    print(f'Замена локального x на {x}')

func(x)
print(f'х по-прежнему {x}')