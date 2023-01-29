# -*- coding: utf8 -*-
# В последовательности на n целых элементов найти произведение элементов средней трети.
from random import randint

n = int(input("Введите количество целых элементов: "))
list_1 = []
for i in range(int(n)):
    list_1.append(randint(0, 10))
