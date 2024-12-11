# Проверить, есть ли у последовательности дубликаты?

# def has_duplicates(seq):
#     return len(seq) != len(set(seq))
#
# print(has_duplicates([1, 2, 3, 2]))
#
# # Напишите программу, которая создает пустое множество и заполняет его 10 случайными целыми числами от 1 до 20.
# # Затем выведите это множество на экран.
#
# import random
#
# numbers = set()
#
# while len(numbers) < 10:
#     numbers.add(random.randint(1, 20))
#
# print(numbers)

# Необходимо создать 2 множества, а затем из двух этих множеств получить третье множество таким образом,
# чтобы новое множество содержало только те элементы, которые есть в обоих исходных множествах

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# set3 = set1.intersection(set2)
# print(set3)

# Напишите программу, которая проверяет, является ли одно множество подмножеством другого множества

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
#
# print(f'Является ли множество set1 подмножеством set2?:', set1 <= set2)

# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе

# def year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# print(year_leap(2024))
# print(year_leap(1997))
# print(year_leap(2022))
# print(year_leap(2001))

# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры

# def square(side):
#     return 4 * side, side * side, side * (2 ** 0.5)
#
# side_length = float(input('Введите длину стороны квадрата: '))
#
# perimeter, area, diagonal = square(side_length)
# print(f"Периметр: {perimeter}")
# print(f"Площадь: {area}")
# print(f"Диагональ: {diagonal}")

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень). Номер месяца вводить с клавиатуры

def season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"

month_number = int(input(f'Введите номер месяца: '))

print(season(month_number))
