with open(file='test_file2.txt', mode='r') as file:
    info = file.readline().strip()

info = info.replace("_", " ")
elements = info.split()

total = sum(int(x) for x in elements if x.isdigit())

print('Сумма чисел:', total)
