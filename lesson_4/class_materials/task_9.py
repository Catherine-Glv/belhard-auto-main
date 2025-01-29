result = lambda x: x + 2
print(result(6))

result = lambda x, y: x + y
print(result(6, 6))

# filter

my_liSt = [1, 3, 4, 6, 10, 12, 15]
news_list = list(filter(lambda x: x % 2 == 0, my_liSt))
print(news_list)

# map

my_liSt = [1, 3, 4, 6, 10, 12, 15]
new_list = list(map(lambda x: x * 2, my_liSt))
print(new_list)
