# Дан целочисленный список A размера 10. Вывести порядковый номер последнего из
# тех его элементов AK, которые удовлетворяют двойному неравенству A1 < AK < A10.
# Если таких элементов нет, то вывести 0.
from random import randint
b = []
for i in range(10):
    b.append(randint(0, 100))
x = 0
for k in range(1, 10):
    if (b[k] > b[0]) and (b[k] < b[9]):
        x = k
print(b)
print('Порядковый номер элемента удовлетворяющих неравенству = ', x)