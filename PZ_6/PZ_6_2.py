# Дано число R и список размера N. Найти два различных элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания их
# индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной).
from random import randint
N = int(input('Введите размер списка'))
R = int(input('Введите R'))
x = []
sam = 0
index_1 = 0
index_2 = 0
v = 0
y = 100
for i in range(N):
    x.append(randint(0, 100))
print(x)
x.append(0)
for i in range(len(x) - 1):
    sam = x[i] + x[i+1]
    v = abs(R - sam)
    if v <= y:
        y = v
        index_1 = x[i]
        index_2 = x[i + 1]
print('Первый элемент', index_1)
print('Второй элемент', index_2)