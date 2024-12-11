def say(message, times=1):
    return message * times

print(say(message='hello'))
print(say('hello', 6))

# Не можем передавать пустую функцию или с большим кол-вом значений
# print(say())
# print(say('gas', 4, 1))