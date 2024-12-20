# переменная состоит из: латинские буквы, цифры и _
# переменная не может начинаться с цифры: 1num
# в названии переменной нельзя использовать спецсимволы
# переменная может начинаться с _: _num
# если переменная названа с большой буквы - КОНСТАНТА
# переменные не называем уже существующими именами внутренних функций
# создавать человеко-подобные переменные (понятные названия)
# закомментировать часть кода - выделить код и нажать ctrl + / (на латинице)
# в числах с точкой используется точка

# Основные типы данных
# int - целое число
# float - дробные числа, числа с плавающей точкой (3.14)
# str - строковое значение '', "", """"""
# bool - True, False

num1 = 4
num2 = 3.14
name = 'Katya'
color = "Green"
text = """hello world"""
is_true = True
is_false = False

print(num1, num2, name, color, text, is_false, is_true)  # print - функция для вывода информации на экран


# Базовые операции с числами

number1 = 5
number2 = 3

print(number1 + number2)
print(number1 - number2)
print(number1 / number2)  # возвращает тип данных float
print(number1 * number2)
# целочисленное деление
print(number1 // number2)
# нахождение остатка от деления
print(number1 % number2)
# возведение в степень
print(number1 ** number2)

# Приоритеты математических операций: **, * / // % + -

print(2 * 3 ** 3)

# изменение значения переменной

x = 4

# 1 способ
x = x + 2
print(x)

# 2 способ
x += 6
print(x)

x -= 6
print(x)
x *= 6
print(x)
x /= 6
print(x)

# Отображение ошибок

print(5 / 0)