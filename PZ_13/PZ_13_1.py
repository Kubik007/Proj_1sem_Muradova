# В матрице элементы кратные трём увеличить в 3 раза

import random

n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matr = [[random.randint(1, 10) for j in range(n)] for i in range(m)]

print('Начальная матрица: ')
for i in matr:
    print(*i)

print('Измененная матрица: ')
for i in matr:
    for j in i:
        if j % 3 == 0:
            j *= 3
        print(j, end=' ')
    print()