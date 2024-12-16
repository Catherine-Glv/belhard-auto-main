with open('test_file.txt', 'r') as file:
    info = file.read().splitlines()

num = sorted(int(x) for x in info if x.isdigit())
words = sorted((x for x in info if not x.isdigit()), key=len)

result = num + words

print('Результат: ', result)
