
from itertools import *
from random import randint
import os
os.system("cls")


k = randint(2, 7) 
print('k = ', k)


def get_ratios(k):
    ratios = [randint(1, 9) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 9)
    return ratios


def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)


with open('poly_1.txt', 'w') as data:
    data.writelines(polynom1)
    data.writelines('\n')


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k)
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('poly_2.txt', 'w') as data:  # добавляем запись в файл
    data.write(polynom2)



with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')
    sum_of_poly = (list_of_poly_1) + (list_of_poly_2),

    if len(poly_1) > len(poly_2):
        help_poly = poly_1
        poly_1 = poly_2
        poly_2=help_poly
    poly_1 = poly_1.split(' + ')
    poly_2 = poly_2.split(' + ')
    print(poly_1,poly_2)

    count1 =0
    count2=len(poly_2)-len(poly_1)
    new_poly = ''
    for i in range(count2):
        new_poly += poly_2[i] + '+'

    ind1 = ''
    ind2 = ''

    for i in range(len(poly_2) - len(poly_1), len(poly_2)):
        result = 0
        if i == len(poly_2) - 1:
            result += int(poly_1[-1][:-4] + poly_2[-1][:-4])
            new_poly += str(result) + poly_1[-1][-4:]

        else:
            result += int(poly_1[count1][:-4] + poly_2[count2][:-4])
            new_poly += str(result) + poly_1[count1][-4:] + ' + '
            count1 += 1
            count2 += 2
    print(new_poly)
