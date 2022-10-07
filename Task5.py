# Задача5: Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def creat_coeff(numbers):
    numbers = numbers.strip().strip(' = 0')
    numbers= numbers.split(' + ')
    coeff = {}
    for i in numbers:
        a, *b = i.split(' * x ** ')
        if b:
            coeff[int(b[0])] = int(a)
        else:
            if i.endswith('x'):
                a, *b = i.split(' * x')
                coeff[1] = int(a)
            else:
                coeff[0] = int(i)
    return coeff

def sum_poly(c, coeff):
    for key in c:
        if not key in coeff:
            coeff[key] = 0
        coeff[key] += c[key] 
    return coeff

with open('task4_1.txt') as f:
    numbers1 = f.read()                           
with open('task4_2.txt') as f:
    numbers2 = f.read()  

coeff1 = creat_coeff(numbers1)    
coeff2 = creat_coeff(numbers2)  
coeff = {}
coeff = sum_poly(numbers1, coeff)
coeff = sum_poly(numbers2, coeff)
result = ''
max_num = max(coeff.keys())
for i, j in coeff.items():
    result += str(j)
    if i != 0 and j != 0 and i != 1:
        result += ' * x ** '
        result += str(i)
        result += ' + '
    elif j == 0:
        continue
    elif i == 1:
        result += ' * x * '
    else:
        result += ' = 0'
print(result)                 
def write_file(st):
    with open('task5_1.txt', 'w') as data:
        data.write(st)
