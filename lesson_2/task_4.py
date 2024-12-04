# кортеж - tuple - неизменяемый список

tuple1 = tuple()
print(tuple1)
print(type(tuple1))

tuple2 = ()
print(tuple2)
print(type(tuple2))

tuple3 = (1, 2, 3, 4, 5)
print(tuple3)

tuple4 = (1,)
print(tuple4)

# Базовые операции с tuple
new_tuple1 = (1, 2, 3)
new_tuple2 = (6, 7, 8)
new_tuple3 = new_tuple1 + new_tuple2
print(new_tuple3)

print(new_tuple1 * 4)

print(len(new_tuple1))

print(new_tuple1.index(2))
print(new_tuple1.count(1))

# Изменение списка внутри кортежа
numbers = (1, 2, 3, [7, 8, 9])
print(numbers)
numbers[-1][-1] = 10
print(numbers)