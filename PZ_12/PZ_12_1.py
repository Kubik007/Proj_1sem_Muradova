# В последовательности на n целых элементов найти произведение элементов средней трети.
from random import randint

n = 3 * randint(1, 3)
list_1 = []
for i in range(int(n)):
    list_1.append(randint(0, 10))
print("Целые числа: ", list_1)

list_2 = [i for i in list_1[n // 3:n // 3 * 2]]
new_list = 1
for i in range (len(list_2)):
    new_list *= list_2[i]
print("Произведение элементов средней трети = ", new_list)