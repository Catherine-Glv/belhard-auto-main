# Вычислить сумму цифр случайного трёхзначного числа.(прочитать про модуль math и random)

import random
import math

number = random.randint(100, 999)

sum_digits = math.fsum([int(digit) for digit in str(number)])

print(f"Сгенерированное трёхзначное число: {number}")
print(f"Сумма цифр числа: {sum_digits}")