"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

array = [randint(-10,10) for _ in range(30)]
print(array)

sum_elem = 0
for i in array:
