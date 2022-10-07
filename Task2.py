# Задача2: Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
n = int(input('Введите натуральное число N: '))
prime_numbers = []

if n == 1:
    print('Простой множетель числа N -> 1')
 
d = 2    
while n >= 2:
    while n % d == 0:
        prime_numbers.append(d)
        n = n / d
    d += 1    
if n / d == 1:
    prime_numbers.append(d)    
print(prime_numbers)

y = set(prime_numbers)   
print(f'простыe множители числа N:', y)
