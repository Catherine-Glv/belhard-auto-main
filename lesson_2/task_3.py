list1 = [1, 2, 3, 4, 5]

# Добавление в конец списка элементов
list1.append(10)
print(list1)

# Подставить значение на выбранную позицию
list1.insert(0, 9)
print(list1)

# Удаление элемента из списка по его значению
# list1.remove(3)
# print(list1)

# Удаление элемента из списка по индексу + возвращение этого элемента
# print(list1.pop(0))
# print(list1)

# Очистка списка
# list1.clear()
# print(list1)

# Найти количество повторений определенного элемента
print(list1.count(10))

# Определить индекс элемента
print(list1.index(4))

# Скопировать список
list2 = list1.copy()
print(list2)

# Сортировка списка
# list1.sort() # сортировка в порядке возрастания
list1.sort(reverse=True)
print(list1)

# Перевернуть список
list1.reverse()
print(list1)
