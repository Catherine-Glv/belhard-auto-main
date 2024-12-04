# Ввод значений с клавиатуры

number1 = input('Введите целое число: ')
print(number1)
print(type(number1))

number1 = int(input('Введите целое число: '))  # лучше указать сразу тип переменных
print(number1)
print(type(number1))

name = input('Введите имя: ')  # строчная запись
print(name)

number2 = float(input('Введите вещественное число: '))
print(number2)
print(type(number2))

check_string = bool(input('Введите строку для проверки на True или False'))
print(check_string)

# 0 = False, 1 = True, любое число не равное 0 = True, даже отрицательное

print(bool(-1))
print(bool(0))
print(bool(1))
