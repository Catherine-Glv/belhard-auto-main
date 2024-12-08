# Преобразование числа в строку

x = 1
x_str = str(x)
print(x_str)
print(type(x))

# Базовые операции со строками: 1) сложение - конкатенация строки, 2) умножение строки - дублирование

text1 = 'Hello '
text2 = 'world'
text3 = text1 + text2
print(text3)
print('1' + '1')

print('name ' * 5)

# len() - нахождение длины строки

len_of_string = len('hello world')
print(len_of_string)

# Индексы строки

# 0 1 2 3   0-П, 1-е, 2-т, 3-я
# отрицательная индексация -1 -2 -3 -4
# -1-я, -2-т, -3-е, -4-П

name = 'Петя'
print(name[-1])
print(name[0], name[1], name[2], name[3])

# Индекс с 2-мя параметрами - срез с двумя параметрами
# [start:stop]

print(name[0:2])  # последний индекс не включен
print(name[:2])

# Срез с тремя параметрами
# [start:stop:step]

print(name[::2])  # вывод Пт (пропуск - е)
print(name[::-1]) # вывод ятеП


print('ll' in 'hello')  # in проверка на нахождение подстроки или элемента в данной строке


