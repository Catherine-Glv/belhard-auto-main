import os
from os import remove

# получение пути
print(f'{os.getcwd()}, начальная директория')

# os.mkdir('first_folder')

os.chdir('first_folder/')

print(f'{os.getcwd()}, новая директория')

with open(file='new_file.txt', mode='w') as file:  # запись файла, создание файла
    print(file)

# os.makedirs('folder1/folder2/folder3')

# os.rmdir('folder1/folder2/folder3') # удаление 1 папки

# os.removedirs('folder1/folder2') # удаление всего содержимого в папках

remove('new_file.txt') # удаление файла

os.chdir('..')
print(f'{os.getcwd()}, новая директория назад')

os.rmdir('first_folder/')
