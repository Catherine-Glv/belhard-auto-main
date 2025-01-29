# Замыкание

def main_func():
    def inner_func():
        return 'hello world'

    return inner_func()

print(main_func())

def main_func_2(num1):
    def inner_func(num2):
        return num1 + num2

    return inner_func

print(main_func_2(num1=3)(1))
