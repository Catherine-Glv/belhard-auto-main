"""
Задан список - [1, 2, 5, 6, 7, 8]. Необходимо вывести его сумму и произведение.
"""
numbers = [1, 2, 5, 6, 7, 8]

sum_of_numbers = 0
product_of_numbers = 1

for number in numbers:
    sum_of_numbers += number
    product_of_numbers *= number

print("Сумма:", sum_of_numbers)
print("Произведение:", product_of_numbers)