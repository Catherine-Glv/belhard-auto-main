try:
    with open(file='test_file3.txt', mode='r') as file:
        lines = file.readlines()

    if not lines:
        print('Файл пуст')
    else:
        print(f'Количество строк: {len(lines)}')
finally:
    print(f'Конец')
