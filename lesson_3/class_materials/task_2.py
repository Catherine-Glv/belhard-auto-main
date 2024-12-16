"""
цикл for

цикл while

"""

# range - генерирует последовательность чисел - int

# for i in range(10):
#     print(i)
#
# for i in range(5, 8):
#     print(i)
#
# for i in range(10, 30, 5):
#     print(i)

list1 = [1, 2, 3, 4, 5, 6, 7]
# for i in list1:
#     if i % 2 == 0:
#         print(i)

"""
break, continue
"""
for i in list1:
    if i == 5:
        break
    print(i)

for i in list1:
    if i == 5:
        continue
    print(i)

