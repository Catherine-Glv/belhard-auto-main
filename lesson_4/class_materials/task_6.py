# Функции высшего порядка

def call_with_five(func):
    return func(5)

def add_one(x):
    return x + 1

print(call_with_five(add_one))
