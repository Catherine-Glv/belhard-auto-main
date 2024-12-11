# Функция без параметров

def say_hello():
    print('hello')

say_hello()

# Функция с параметрами

def print_max_number(first_number, second_number): # first_number, second_number - параметры
    if first_number > second_number:
        print(f'Число first_number={first_number} больше чем second_number={second_number}')
    elif first_number == second_number:
        print(f'Переданные числа равны')
    else:
        print(f'Число second_number={second_number} больше чем first_number={first_number}')

print_max_number(first_number=4, second_number=5) # 4, 5 - аргументы функции
print_max_number(first_number=6, second_number=2)
print_max_number(first_number=4, second_number=4)

def print_max_number(first_number, second_number): # first_number, second_number - параметры
    if first_number > second_number:
        return f'Число first_number={first_number} больше чем second_number={second_number}'
    elif first_number == second_number:
        return f'Переданные числа равны'
    else:
        return f'Число second_number={second_number} больше чем first_number={first_number}'

print(print_max_number(first_number=4, second_number=5)) # 4, 5 - аргументы функции
print(print_max_number(first_number=6, second_number=2))
print(print_max_number(first_number=4, second_number=4))

x = print_max_number(first_number=7, second_number=1)
print(x)