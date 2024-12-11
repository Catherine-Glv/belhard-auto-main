# Множество

set1 = {1, 2, 3, 4, 11, 15, 80, 23, 25, 90}
print(set1)

set2 = {1, 2, 3, 1, 2, 3}
print(set2)

set3 = {'cat', 'dog', 'bird', 'snake'}
print(set3)

set4 = set() # пустое множество
print(type(set4))

# print(set4 + set3) - + нет у множеств
# print(set4 * 4) - + нет у множеств

print(len(set3))

# add
set4.add(3)
set4.add(4)
set4.add(5)
print(set4)

# удаление remove, discard, pop
set4.remove(3)
print(set4)

set4.discard(10)
print(set4)

set4.pop() # удаляет первый элемент множества
print(set4)

# union
set5 = set4.union(set2)
print(set5)

# update
set4.update({10, 12})
print(set4)

x_set = {1, 2, 7, 8}
y_set = {3, 4, 5, 6}
print(x_set.intersection(y_set))
print(x_set.isdisjoint(y_set))
