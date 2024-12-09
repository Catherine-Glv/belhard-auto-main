"""
Есть список [1,1,2,2,3,3]. Необходимо из данного списка убрать все дубликаты. Результатом должен стать список [1, 2, 3].
Примечание: просто удалить элементы мы не можем)
"""

list_2 = [1, 1, 2, 2, 3, 3]
new_list = [i for index, i in enumerate(list_2) if i not in list_2[:index]]
print(new_list)
# for i in list_2:
#     new_list.append(i)
# print(new_list)

# my_list = [i for i in range(10) if i % 2 == 0]
# print(my_list)