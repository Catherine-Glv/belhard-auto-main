# равно - ==
# print(5 == 5)
# print(5 != 4)
#
# print(4 > 2)
# print(6 < 5)
#
# print(2 <= 4)
# print(4 >= 3)

"""
if условие(True):
    код

Если условие False - то код не выполнится
"""

x = 3
if x == 5:
    print(f'Выполнен блок if')

"""
if условие:
    код
else:
"""

if x == 5:
    print(f'Выполнен блок if')
else:
    print('Выполнен блок else')

"""
if условие:
    код
elif условие:
    код
......... - выполнение неограниченное число раз
else:
"""

if x == 5:
    print(f'Выполнен блок if')
elif x == 3:
    print('Выполнен блок elif')
else:
    print('Выполнен блок else')