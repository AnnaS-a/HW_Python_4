# Задача1: Вычислить число c заданной точностью d
# Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from random import random

import decimal
k = round(random() * 10)
print(k)
d = str(1 / 10 ** k)
print(d)

count = 0
for i in d:
    count += 1 
b = count - 2
num = round(decimal.Decimal(math.pi), k)

print(f'при заданной точности {d} число пи', num)
