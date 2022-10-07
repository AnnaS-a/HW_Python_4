# Задача3: Задайте последовательность чисел. Напишите программу, которая
#  выведет список неповторяющихся элементов исходной последовательности.

from random import random
import copy

num_list = []
for i in range(12):
    num = int(random() * 10)
    num_list.append(num)
print(num_list)
new_list = list(copy.deepcopy(num_list))
for i in new_list:
    while new_list.count(i) > 1:
        new_list.remove(i) 
print(new_list)
