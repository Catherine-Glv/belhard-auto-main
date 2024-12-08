# Коллекции

"""
list, tuple, dict, set, frozenset, str
"""

list1 = list()
print(list1)

list2 = []
print(list2)

number1 = [1, 2, 3, 4, 5, 6, 7]
print(number1)

# Индексация как и у строк

print(number1[-1], number1[0])
print(number1[2:5])
print(number1[::-1])

# Вложенные списки

new_list = [1, 2, [5, 6, 7]]
print(new_list[2][1])

# Базовые операции со списками

list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)
print(list2 * 5)

list1[0] = 10 # Изменение данных в списке
print(list1)