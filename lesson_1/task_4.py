name = 'Артем'
age = 20
color = 'Blue'

print('Имя', name, 'возраст', age, 'цвет глаз', color)  # не красиво и дольше

print(f'Имя - {name}, возраст человека {age}, цвет его глаз {color}')  # вывод через f - строки

text = 'Hello world my name is'
list_text = text.split(' ')  # split - метод вывода списка элементов строки
print(list_text)

new_text = ";".join(list_text)  # join - получает новую строку элементов
print(new_text)

numbers = '123456789'
print(numbers.isdigit())  # методы is - показывают True False


# Логические операторы

# and - логическое сложение
# or - логическое умножение
# not - отрицание

print(f'Результат True и True -> {True and True}')
print(f'Результат True и False -> {True and False}')
print(f'Результат False и False -> {False and True}')

print(f'Результат True или True -> {True or True}')
print(f'Результат True или False -> {True or False}')
print(f'Результат False или False -> {False or True}')

print(f'Результат не True -> {not True}')
print(f'Результат не False -> {not False}')

