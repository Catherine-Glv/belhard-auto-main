# file = open(file='test_file.txt', mode='r')  # encoding='utf-8' - для кириллицы
# print(file)
#print(*file)  # Распаковка файла
# x = file.read().replace('\n', ' ')
# print(x)

# print(file.readline())
# print(file.readline())
# print(file.readline()) # построчно строки
#
# print(file.readlines()) # вывод всех строк

# try:
#         lines = file.readlines()
#         print(lines[4])
#         print(lines[7])
# except IndexError:
#     print("Ошибка")
# finally:
#     file.close()
#
# with open(file='test_file.txt', mode='r') as file: # автоматически закроется файл с данной конструкцией with
#     print(file.read())

with open(file='test_file.txt', mode='w') as file:  # запись файла, перезапись файла
    print(file.write('hello from code')) # write перезаписывает файл

with open(file='test_file.txt', mode='a') as file:  # запись файла, добавление в файл
    print(file.write('hello from code'))

with open(file='test_file2.txt', mode='w') as file:  # если не находит файл - то создает его
    print(file.write('hello'))

with open(file=r'/Users/catherine/PycharmProjects/belhard-auto-main/lesson_4/text_file.txt', mode='r') as file:
    print(file.read())
